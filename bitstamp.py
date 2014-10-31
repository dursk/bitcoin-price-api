from decimal import Decimal
from helpers import get_datetime, get_response

def get_current_price():
    url = 'https://bitstamp.net/api/ticker/'
    data = get_response(url)
    price = data['last']
    return Decimal(price)

def get_current_bid():
    url = 'https://bitstamp.net/api/ticker/'
    data = get_response(url)
    price = data['bid']
    return Decimal(price)

def get_current_ask():
    url = 'https://bitstamp.net/api/ticker/'
    data = get_response(url)
    price = data['ask']
    return Decimal(price)
