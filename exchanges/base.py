from decimal import Decimal

from exchanges.helpers import get_response, get_datetime
import datetime
def weekly_expiry():
    d = datetime.date.today()
    while d.weekday() != 5:
        d += datetime.timedelta(1)
    return d

def  quarter_expiry():
    ref = datetime.date.today()
    if ref.month < 4:
        d = datetime.date(ref.year, 3, 31)
    elif ref.month < 7:
        d = datetime.date(ref.year, 6, 30)
    elif ref.month < 10:
        d = datetime.date(ref.year, 9, 30)
    else:
        d= datetime.date(ref.year, 12, 31)
    while d.weekday() != 5:
        d -= datetime.timedelta(1)
    return d

def date_stamp(d):
    return d.strftime("%Y-%m-%d")

def time_stamp(d):
    return d.strftime("%H:%M:%S")


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

class FuturesExchange(object):
    @classmethod
    def get_data(cls):
        raise NotImplementedError
