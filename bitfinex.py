from decimal import Decimal
from helpers import *
import requests

TICKER_URL = 'https://api.bitfinex.com/v1/pubticker/btcusd'

def get_current_price():
    data = get_response(TICKER_URL)
    price = data['last_price']
    return Decimal(price)

def get_current_bid():
    data = get_response(TICKER_URL)
    price = data['bid']
    return Decimal(price)

def get_current_ask():
    data = get_response(TICKER_URL)
    price = data['ask']
    return Decimal(price)
