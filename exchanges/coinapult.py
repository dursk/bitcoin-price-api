from decimal import Decimal
from helpers import get_response

TICKER_URL = 'https://api.coinapult.com/api/ticker?market={}_BTC'
TICKER_LEVEL = [
    (50, 'small'),
    (250, 'medium'),
    (1000, 'large'),
    (2500, 'vip'),
    (5000, 'vip+')
]

def get_current_price(currency='USD'):
    url = TICKER_URL.format(currency)
    data = get_response(url)
    price = str(data['index'])
    return Decimal(price)

def get_current_bid(currency='USD', btc_amount=0.1):
    url = TICKER_URL.format(currency)
    data = get_response(url)
    level = _pick_level(btc_amount) if btc_amount > 0 else 'small'
    price = str(data[level]['bid'])
    return Decimal(price)

def get_current_ask(currency='USD', btc_amount=0.1):
    url = TICKER_URL.format(currency)
    data = get_response(url)
    level = _pick_level(btc_amount) if btc_amount > 0 else 'small'
    price = str(data[level]['ask'])
    return Decimal(price)

def _pick_level(btc_amount):
    """
    Choose between small, medium, large, ... depending on the
    amount specified.
    """
    for size, level in TICKER_LEVEL:
        if btc_amount < size:
            return level
    return TICKER_LEVEL[-1][1]
