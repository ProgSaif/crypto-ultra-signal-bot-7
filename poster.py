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

Trade ${coin_name} here 👇
"""
    return message
