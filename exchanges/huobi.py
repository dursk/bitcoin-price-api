from decimal import Decimal
from helpers import *

TICKER_URL = 'https://market.huobi.com/staticmarket/ticker_btc_json.js'

def get_current_price():
        data = get_response(TICKER_URL)
        price = data['ticker']['last']
        return Decimal(price)

def get_current_bid():
        data = get_response(TICKER_URL)
        price = data['ticker']['buy']
        return Decimal(price)

def get_current_ask():
        data = get_response(TICKER_URL)
        price = data['ticker']['sell']
        return Decimal(price)
