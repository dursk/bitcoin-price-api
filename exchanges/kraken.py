from decimal import Decimal

from exchanges.base import Exchange
from exchanges.helpers import get_response


class Kraken(Exchange):

    TICKER_URL = 'https://api.kraken.com/0/public/Trades?pair=%s'
    DEPTH_URL = 'https://api.kraken.com/0/public/Depth?pair=%s'

    @classmethod
    def get_current_price(cls, pair='XXBTZUSD'):
        data = get_response(cls.TICKER_URL %  pair)
        price = data['result'][pair][-1][0]
        return Decimal(str(price))

    @classmethod
    def get_current_bid(cls, pair='XXBTZUSD'):
        data = get_response(cls.DEPTH_URL % pair)
        price = data['result'][pair]['bids'][0][0]
        return Decimal(str(price))

    @classmethod
    def get_current_ask(cls, pair='XXBTZUSD'):
        data = get_response(cls.DEPTH_URL % pair)
        price = data['result'][pair]['asks'][0][0]
        return Decimal(str(price))
