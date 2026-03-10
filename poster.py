def generate_signal_message(coin, entry, sl, tp1, tp2, tp3, trade_type="LONG", confidence=85):
    """
    Generates a Telegram-ready crypto signal message.

    Parameters:
    - coin: str, symbol e.g. "BSW"
    - entry: float, entry price
    - sl: float, stop-loss
    - tp1/tp2/tp3: float, target prices
    - trade_type: "LONG" or "SHORT"
    - confidence: int, confidence percentage

    Returns:
    - str: formatted Telegram message
    """

    return f"""💹 ${coin} – {trade_type}

Entry: {entry:.8f}
SL: {sl:.8f}
TP1: {tp1:.8f}
TP2: {tp2:.8f}
TP3: {tp3:.8f}

Please like and comment 
— Follow for more signal —

Why this setup?
• Confidence: {confidence}%
• Trend & volume confirmed

DYOR
#{coin}"""
