def generate_signal_message(coin, entry, sl, tp1, tp2, tp3, trade_type="LONG", confidence=85):
    # Remove 'USDT' from coin if it's there
    coin_name = coin.replace("USDT", "")
    
    return f"""
💹 ${coin_name} – {trade_type}

Entry: {entry:.8f}
SL: {sl:.8f}
TP1: {tp1:.8f}
TP2: {tp2:.8f}
TP3: {tp3:.8f}


Please like and comment 
— Follow for more updates —

Why this setup?
• Confidence: {confidence}%
• Trend & volume confirmed


DYOR
#{coin_name}
"""
