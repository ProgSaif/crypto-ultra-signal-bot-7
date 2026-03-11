import pandas as pd
import numpy as np

# ===== PARAMETERS =====
EMA_FAST = 9
EMA_SLOW = 21
RSI_PERIOD = 14
PRICE_MOVE_THRESHOLD = 0.001      # 0.1% price move
VOLUME_MULTIPLIER = 0.1           # realistic spike detection: Signal only when volume is 1.5x higher than average.
RSI_LONG_MAX = 60                 #This catches trend earlier: RSI_LONG_MAX = 60 RSI_SHORT_MIN = 40
RSI_SHORT_MIN = 40
CONFIDENCE_THRESHOLD = 20         # Strong signals: CONFIDENCE_THRESHOLD = 50
MIN_DAILY_VOLUME = 1            # Only coins with $5M+ daily volume: MIN_DAILY_VOLUME = 5000000
ATR_MULTIPLIER = 3                # ✅ Good for TP/SL calculation: Many traders use 2–3

# ===== HELPER FUNCTIONS =====
def calculate_rsi(df, period=RSI_PERIOD):
    if df is None or len(df) < period:
        return None
    delta = df['close'].diff()
    gain = np.where(delta>0, delta, 0)
    loss = np.where(delta<0, -delta, 0)
    avg_gain = pd.Series(gain).rolling(period).mean()
    avg_loss = pd.Series(loss).rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1] if not rsi.empty else None

def calculate_ema_trend(df, fast=EMA_FAST, slow=EMA_SLOW):
    if df is None or len(df) < slow:
        return None
    ema_fast = df['close'].ewm(span=fast, adjust=False).mean()
    ema_slow = df['close'].ewm(span=slow, adjust=False).mean()
    if ema_fast.iloc[-1] > ema_slow.iloc[-1]:
        return "up"
    elif ema_fast.iloc[-1] < ema_slow.iloc[-1]:
        return "down"
    else:
        return "flat"

def calculate_atr(df, period=14):
    if df is None or len(df) < period:
        return None
    high_low = df["high"] - df["low"]
    high_close = np.abs(df["high"] - df["close"].shift())
    low_close = np.abs(df["low"] - df["close"].shift())
    tr = pd.DataFrame({"hl": high_low, "hc": high_close, "lc": low_close}).max(axis=1)
    atr = tr.rolling(period).mean()
    return atr.iloc[-1] if not atr.empty else None

def detect_volume_spike(df, multiplier=VOLUME_MULTIPLIER):
    if df is None or len(df) < 20:
        return False
    avg_volume = df['volume'].rolling(20).mean().iloc[-1]
    current_volume = df['volume'].iloc[-1]
    return current_volume > (avg_volume * multiplier)

# ===== SIGNAL CALCULATION =====
def calculate_signal(symbol, df):
    if df is None or len(df) < 15:
        print(symbol, "skipped: insufficient data")
        return None

    rsi = calculate_rsi(df)
    ema_trend = calculate_ema_trend(df)
    atr = calculate_atr(df)
    volume_spike = detect_volume_spike(df)
    last_price = df['close'].iloc[-1]
    change = (df['close'].iloc[-1] - df['close'].iloc[0]) / df['close'].iloc[0]

    # Debug info
    print(symbol, "-> RSI:", rsi, "Trend:", ema_trend, "Volume Spike:", volume_spike, "Change:", round(change,4), "Volume:", round(df['volume'].iloc[-1],2))

    # Signal logic
    trade_type = None
    if change > PRICE_MOVE_THRESHOLD and ema_trend=="up" and (rsi is None or rsi < RSI_LONG_MAX) and volume_spike:
        trade_type = "LONG"
    elif change < -PRICE_MOVE_THRESHOLD and ema_trend=="down" and (rsi is None or rsi > RSI_SHORT_MIN) and volume_spike:
        trade_type = "SHORT"

    if not trade_type:
        return None

    # TP / SL
    if atr is None:
        atr = last_price*0.01
    if trade_type=="LONG":
        entry = last_price
        sl = entry - atr*ATR_MULTIPLIER
        tp1 = entry + atr*ATR_MULTIPLIER
        tp2 = entry + atr*ATR_MULTIPLIER*2
        tp3 = entry + atr*ATR_MULTIPLIER*3
    else:
        entry = last_price
        sl = entry + atr*ATR_MULTIPLIER
        tp1 = entry - atr*ATR_MULTIPLIER
        tp2 = entry - atr*ATR_MULTIPLIER*2
        tp3 = entry - atr*ATR_MULTIPLIER*3

    confidence = int(abs(change)*100) + (20 if volume_spike else 0)
    confidence = min(confidence, 100)
    if confidence < CONFIDENCE_THRESHOLD:
        return None

    return {
        "coin": symbol,
        "entry": entry,
        "sl": sl,
        "tp1": tp1,
        "tp2": tp2,
        "tp3": tp3,
        "trade_type": trade_type,
        "confidence": confidence
    }
