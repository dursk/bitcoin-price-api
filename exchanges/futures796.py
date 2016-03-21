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
    @classmethod
    def getData(cls):
        data = requests.get("http://api.796.com/v3/futures/ticker.html?type=weekly").json()['ticker']
        print(data)
        return {'dates':[date_stamp(weekly_expiry())],
                          "contract" : ["XBT"],
                          "bids" : [ Decimal(data['buy'])],
                          "asks" : [ Decimal(data['sell'])],
                          "last" : [ Decimal(data['last'])]}
if __name__ == "__main__":
    print(Futures796().getData())
