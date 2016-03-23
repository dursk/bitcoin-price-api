from exchanges.base import FuturesExchange, date_stamp, time_stamp
from exchanges.helpers import get_response, get_datetime
from decimal import Decimal
import dateutil.parser
import requests
import datetime
def weekly_expiry():
    d = datetime.date.today()
    while d.weekday() != 5:
        d += datetime.timedelta(1)
    return d

class Futures796(FuturesExchange):
    TICKER_URL = "http://api.796.com/v3/futures/ticker.html?type=weekly"
    def __init__(self, *args, **kwargs):
        super(Futures796,self).__init__(*args, **kwargs)
    def get_data(self):
        self.refresh()
        data = self.data['ticker']
        return {'dates':[date_stamp(weekly_expiry())],
                          "contract" : ["XBT"],
                          "bids" : [ Decimal(data['buy'])],
                          "asks" : [ Decimal(data['sell'])],
                          "last" : [ Decimal(data['last'])]}
