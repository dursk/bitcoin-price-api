import datetime
from decimal import Decimal

import dateutil.parser
import requests

from exchanges.base import Exchange, FuturesExchange, date_stamp, time_stamp
from exchanges.helpers import get_response, get_datetime


class OKCoin(Exchange):

    TICKER_URL = 'https://www.okcoin.com/api/ticker.do?ok=1'

    @classmethod
    def _current_price_extractor(cls, data):
        return data.get('ticker', {}).get('last')

    @classmethod
    def _current_bid_extractor(cls, data):
        return data.get('ticker', {}).get('buy')

    @classmethod
    def _current_ask_extractor(cls, data):
        return data.get('ticker', {}).get('sell')


class OKCoinFutures(Exchange):

    @classmethod
    def get_current_data(cls):
        symbols = []
        dates = []
        bids = []
        asks = []
        last = []
        contract = []
        for i in ['this_week', 'next_week', 'month', 'quarter']:
            response = requests.get(
                'https://www.okcoin.com/api/future_ticker.do',
                params={
                    'symbol': 'btc_usd',
                    'contractType': i
                }
            )
            data = response.json()['ticker'][0]
            d = datetime.date(
                int(str(data['contractId'])[0:4]),
                int(str(data['contractId'])[4:6]),
                int(str(data['contractId'])[6:8])
            )
            dates.append(date_stamp(d))
            bids.append(data['buy'])
            asks.append(data['sell'])
            last.append(data['last'])
            contract.append('XBT')

        return {
            'contract' : contract,
            'dates': dates,
            'bids' : [Decimal(str(x)) for x in bids],
            'asks' : [Decimal(str(x)) for x in asks],
            'last' : [Decimal(str(x)) for x in last]
        }
