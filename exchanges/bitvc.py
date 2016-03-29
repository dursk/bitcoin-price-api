import datetime
from decimal import Decimal

import dateutil.parser
import requests

from exchanges.base import FuturesExchange, date_stamp, time_stamp
from exchanges.helpers import get_response, get_datetime


def weekly_expiry():
    d = datetime.date.today()
    while d.weekday() != 5:
        d += datetime.timedelta(1)
    return d


def weekly_expiry():
    d = datetime.date.today()
    while d.weekday() != 5:
        d += datetime.timedelta(1)
    return d


def quarter_expiry():
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


expiry = {}
expiry['week'] = weekly_expiry()
expiry['next_week'] = weekly_expiry() + datetime.timedelta(7)
expiry['quarter'] = quarter_expiry()


class BitVc(FuturesExchange):
    def __init__(self, *args, **kwargs):
        super(BitVc,self).__init__(*args, **kwargs)
    def get_current_data(self):
        dates= []
        bids = []
        asks = []
        last = []
        contract = []
        for i in ['week', 'next_week', 'quarter']:
            data = requests.get(
                'http://market.bitvc.com/futures/ticker_btc_' + i + '.js'
            ).json()
            dates.append(date_stamp(expiry[i]))
            bids.append(data['buy'])
            asks.append(data['sell'])
            last.append(data['last'])
            contract.append('XBT')

        return {
            'dates':dates,
            'bids' : [Decimal(str(x)) for x in bids],
            'asks' : [Decimal(str(x)) for x in asks],
            'last' : [Decimal(str(x)) for x in last],
            'contract' : contract
        }
