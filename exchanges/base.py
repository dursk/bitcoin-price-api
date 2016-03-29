import datetime
from decimal import Decimal

from exchanges.helpers import get_response, get_datetime


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
    return d.strftime('%Y-%m-%d')


def time_stamp(d):
    return d.strftime('%H:%M:%S')


class ExchangeBase(object):

    TICKER_URL = None

    def __init__(self, *args, **kwargs):
        self.data = None
        self.ticker_url = self.TICKER_URL

    def get_data(self):
        if self.data == None:
            self.refresh()

    def refresh(self, callback=None, client_data=None):
        self.data = get_response(self.ticker_url)
        if callback is not None:
            callback(self, client_data)

class Exchange(ExchangeBase):

    def _current_price_extractor(self, data):
        raise NotImplementedError

    def _current_bid_extractor(self, data):
        raise NotImplementedError

    def _current_ask_extractor(self, data):
        raise NotImplementedError

    def get_current_data(self):
        return {'last': self.get_current_price(),
                'bid' : self.get_current_bid(),
                'ask' : self.get_current_ask()}

    def get_current_price(self):
        self.get_data()
        price = self._current_price_extractor(self.data)
        return Decimal(price)

    def get_current_bid(self):
        self.get_data()
        price = self._current_bid_extractor(self.data)
        return Decimal(price)

    def get_current_ask(self):
        self.get_data()
        price = self._current_ask_extractor(self.data)
        return Decimal(price)


class FuturesExchange(ExchangeBase):

    def get_current_data(cls):
        raise NotImplementedError
