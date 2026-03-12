import os
import asyncio
from telegram import Bot
from scanner import scan_market, get_klines
from poster import generate_signal_message
from dotenv import load_dotenv
import requests
import time

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not BOT_TOKEN or not CHANNEL_ID:
    raise ValueError("Missing BOT_TOKEN or CHANNEL_ID in .env")

bot = Bot(token=BOT_TOKEN)

async def send_message_safe(message, delete_after=0):
    for i in range(3):
        try:
            msg = await bot.send_message(chat_id=CHANNEL_ID, text=message)
            if delete_after>0:
                asyncio.create_task(delete_after_delay(msg.message_id, delete_after))
            return
        except Exception as e:
            print("Telegram error:", e)
            await asyncio.sleep(15)

async def delete_after_delay(message_id, delay):
    await asyncio.sleep(delay)
    try:
        await bot.delete_message(chat_id=CHANNEL_ID, message_id=message_id)
    except Exception as e:
        print("Delete message failed:", e)

def fetch_usdt_pairs():
    for i in range(3):
        try:
            resp = requests.get("https://api.binance.us/api/v3/exchangeInfo", timeout=10)
            data = resp.json()
            if 'symbols' not in data:
                print("Exchange info missing 'symbols':", data)
                time.sleep(5)
                continue
            usdt_pairs = [s['symbol'] for s in data['symbols'] if s['symbol'].endswith("USDT")]
            return usdt_pairs
        except Exception as e:
            print("Error fetching exchange info:", e)
            time.sleep(5)
    return []

async def run_bot():
    print("🚀 ULTRA SCANNER BOT STARTED")
    posted = set()
    while True:
        symbols = fetch_usdt_pairs()
        if not symbols:
            print("No symbols fetched, retrying in 60s...")
            await asyncio.sleep(60)
            continue
        signals = scan_market(symbols)
        for s in signals:
            key = f"{s['coin']}_{s['trade_type']}"
            if key not in posted:
                msg = generate_signal_message(
                    s['coin'], s['entry'], s['sl'], s['tp1'], s['tp2'], s['tp3'],
                    s['trade_type'], s['confidence']
                )
                print("Posting:", s['coin'], s['trade_type'])
                await send_message_safe(msg)
                posted.add(key)
                await asyncio.sleep(8)
        print("Cycle completed. 😌😌😌😌😌 Waiting 20 minutes for next scan...😌😌😌😌😌")
        await asyncio.sleep(1200)

asyncio.run(run_bot())
