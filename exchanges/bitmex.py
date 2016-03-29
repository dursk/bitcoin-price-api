from decimal import Decimal

import dateutil.parser

from exchanges.base import FuturesExchange, date_stamp, time_stamp
from exchanges.helpers import get_response, get_datetime


class Bitmex(FuturesExchange):

    TICKER_URL = 'https://www.bitmex.com:443/api/v1/instrument/active'

    def get_current_data(self):
        self.refresh()
        symbols = []
        dates = []
        bids = []
        asks = []
        last = []
        contract = []
        for contracttype in ['XBU', 'XBT']:
            for i in self.data:
                if i['rootSymbol'] == contracttype and i['buyLeg'] == '':
                    dates.append(
                        date_stamp(dateutil.parser.parse(i['expiry']))
                    )
                    symbols.append(i['symbol'])
                    bids.append(i['bidPrice'])
                    asks.append(i['askPrice'])
                    last.append(i['lastPrice'])
                    contract.append(contracttype)
        return {
            'contract' : contract,
            'dates': dates,
            'bids' : [Decimal(str(x)) for x in bids],
            'asks' : [Decimal(str(x)) for x in asks],
            'last' : [Decimal(str(x)) for x in last]
        }
