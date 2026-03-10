# poster.py

import random

# -----------------------------
# Filter leveraged tokens
# -----------------------------
BLOCKED_KEYWORDS = ["UP", "DOWN", "BULL", "BEAR"]

def is_valid_symbol(symbol):
    """
    Allow only normal USDT spot coins
    """
    if not symbol.endswith("USDT"):
        return False

    for word in BLOCKED_KEYWORDS:
        if word in symbol:
            return False

    return True


# -----------------------------
# Message generator
# -----------------------------
def generate_signal_message(coin, entry, sl, tp1, tp2, tp3, trade_type="LONG", confidence=85):

    coin_name = coin.replace("USDT", "")

    entry_low = entry * 0.995
    entry_high = entry * 1.005

    message = f"""
Guy! ${coin_name} just flashed momentum.

💹 ${coin_name} — {trade_type}

Entry: {entry_low:.8f} – {entry_high:.8f}
SL: {sl:.8f}
TP1: {tp1:.8f}
TP2: {tp2:.7f}
TP3: {tp3:.6f}

— Follow for more signal —
Like and comment Please

Why this setup?
• {confidence}% Confidence
• Trend & volume confirmed. Trend is our friend and believe in volume that you make you millionnaire.
• However, {coin_name} just broke out of its consolidation range with a strong {'bullish' if trade_type=='LONG' else 'bearish'} candle. 
• Price reclaimed the {entry:.6f} level, showing {'buyers' if trade_type=='LONG' else 'sellers'} stepping back in after weeks of sideways action. 
• If {'bulls' if trade_type=='LONG' else 'bears'} hold above {entry_low:.6f}, the next liquidity sits around {tp1:.6f}+.
• DYOR before execute trade 

Trade here 👇${coin_name}
"""

    return message


# -----------------------------
# Fake signal generator
# (replace with your real logic)
# -----------------------------
def generate_signal(symbol):

    trade_type = random.choice(["LONG", "SHORT"])

    entry = random.uniform(0.01, 100)
    sl = entry * 0.97
    tp1 = entry * 1.02
    tp2 = entry * 1.04
    tp3 = entry * 1.06
    confidence = random.randint(50, 95)

    return generate_signal_message(symbol, entry, sl, tp1, tp2, tp3, trade_type, confidence)


# -----------------------------
# Example posting loop
# -----------------------------
def run_bot(symbols):

    for symbol in symbols:

        # Skip leveraged tokens
        if not is_valid_symbol(symbol):
            continue

        signal_message = generate_signal(symbol)

        if signal_message:

            trade_type = "LONG" if "— LONG" in signal_message else "SHORT"
            print(f"Posting: {symbol} {trade_type}")

            # Here you will send to Telegram / Binance Square
            print(signal_message)


# -----------------------------
# Example list (replace with API)
# -----------------------------
if __name__ == "__main__":

    example_symbols = [
        "BTCUSDT",
        "ETHUSDT",
        "ADAUSDT",
        "SOLUSDT",
        "BNBUSDT",
        "BTCUPUSDT",
        "BTCDOWNUSDT",
        "BNBBULLUSDT",
        "BNBBEARUSDT"
    ]

    run_bot(example_symbols)
