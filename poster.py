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
