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
    return f"""
💹 ${coin} – {trade_type}

Entry: {entry:.8f}
SL: {sl:.8f}
TP1: {tp1:.8f}
TP2: {tp2:.8f}
TP3: {tp3:.8f}

Why this setup?
• Confidence: {confidence}%
• Trend & volume confirmed

Please like and comment your PNL
— Follow for more updates —
DYOR
#{coin}
"""
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

