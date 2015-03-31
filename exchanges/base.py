from decimal import Decimal

from helpers import get_response, get_datetime


class Exchange(object):

    TICKER_URL = None

    @classmethod
    def _current_price_extractor(cls, data):
        raise NotImplementedError

    @classmethod
    def _current_bid_extractor(cls, data):
        raise NotImplementedError

    @classmethod
    def _current_ask_extractor(cls, data):
        raise NotImplementedError

    @classmethod
    def get_current_price(cls):
        data = get_response(cls.TICKER_URL)
        price = cls._current_price_extractor(data)
        return Decimal(price)

    @classmethod
    def get_current_bid(cls):
        data = get_response(cls.TICKER_URL)
        price = cls._current_bid_extractor(data)
        return Decimal(price)

    @classmethod
    def get_current_ask(cls):
        data = get_response(cls.TICKER_URL)
        price = cls._current_ask_extractor(data)
        return Decimal(price)
