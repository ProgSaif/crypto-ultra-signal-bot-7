# 💹 Ultra Crypto Signal Bot

A **fully automated crypto signal bot** for USDT trading pairs on Binance.
Generates professional **LONG/SHORT signals** using **RSI, EMA, ATR, and volume spike analysis**, and posts directly to your **Telegram channel**.

This version is fully tested and **ready to deploy on Replit**.

---

## **Features**

* Scans **all USDT trading pairs** automatically.
* Uses **RSI + EMA + ATR + Volume Spike** for robust signal generation.
* Generates **entry, stop-loss, and 3 take-profit levels** for each signal.
* **Debug logs** to monitor skipped coins and errors.
* **Telegram integration** for automatic posting.
* **Retry logic** for stable network calls.
* Fully configurable with `.env`.
* Optimized for **Replit deployment**, runs 24/7 with uptime hacks.

---

## **Repo Structure**

```
crypto-ultra-signal-bot/
│
├─ .env
├─ Procfile
├─ requirements.txt
├─ main.py
├─ signals.py
├─ scanner.py
└─ poster.py
```

---

## **Setup Instructions for Replit**

### 1️⃣ Create a Replit project

* Go to [Replit](https://replit.com/) → **New Repl** → Python
* Name it `crypto-ultra-signal-bot` (or any name you like).

### 2️⃣ Add files

* Copy all files (`main.py`, `signals.py`, `scanner.py`, `poster.py`) into the Replit project.
* Add `.env`, `requirements.txt`, and `Procfile`.

### 3️⃣ Set `.env`

Create a file `.env` in Replit and add:

```
BOT_TOKEN=your_telegram_bot_token
CHANNEL_ID=@your_telegram_channel
```

> Replace `your_telegram_bot_token` with your bot token and `@your_telegram_channel` with your channel ID.

### 4️⃣ Install dependencies

In Replit shell:

```bash
pip install -r requirements.txt
```

Dependencies:

* python-telegram-bot==20.7
* requests
* pandas
* numpy
* python-dotenv

### 5️⃣ Run the bot

In Replit shell:

```bash
python main.py
```

You should see:

```
🚀 ULTRA SCANNER BOT STARTED
```

The bot will scan all USDT pairs and post signals automatically.

---

## **How it Works**

1. **Fetch Binance USDT pairs** automatically via API.
2. **Retrieve historical price data** for each coin.
3. **Analyze trends**:

   * EMA (fast/slow) for trend direction
   * RSI for overbought/oversold detection
   * ATR for volatility
   * Volume spike detection
4. **Generate signal**:

   * LONG or SHORT
   * Entry, SL, TP1, TP2, TP3
   * Confidence score
5. **Send to Telegram channel**.

---

## **poster.py Example**

```python
def generate_signal_message(coin, entry, sl, tp1, tp2, tp3, trade_type="LONG", confidence=85):
    # Remove 'USDT' from coin if it's there
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
However, {coin_name} just broke out of its consolidation range with a strong {'bullish' if trade_type=='LONG' else 'bearish'} candle.
Price reclaimed the {entry:.6f} level, showing {'buyers' if trade_type=='LONG' else 'sellers'} stepping back in after weeks of sideways action.
If {'bulls' if trade_type=='LONG' else 'bears'} hold above {entry_low:.6f}, the next liquidity sits around {tp1:.6f}+.
DYOR

Trade here 👇${coin_name} 
"""
    return message

```

---

## **Notes**

* Signals are **automated**, always **DYOR** (Do Your Own Research).
* The bot prints **debug info** for skipped coins and errors.
* Adjust **EMA, RSI, ATR, and thresholds** in `signals.py` to fit your strategy.
* **Safe for Replit**, but you may need a **Replit uptime hack** or paid plan for 24/7 continuous running.

---

## **License**

MIT License – free to use and modify.

