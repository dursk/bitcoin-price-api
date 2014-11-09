from decimal import Decimal
from helpers import get_datetime, get_response

TICKER_URL = 'https://bitstamp.net/api/ticker/'

def get_current_price():
    data = get_response(TICKER_URL)
    price = data['last']
    return Decimal(price)

def get_current_bid():
    data = get_response(TICKER_URL)
    price = data['bid']
    return Decimal(price)

def get_current_ask():
    data = get_response(TICKER_URL)
    price = data['ask']
    return Decimal(price)
