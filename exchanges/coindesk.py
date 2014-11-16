from exchange import Exchange

from decimal import Decimal
from helpers import get_datetime, get_response

class Coindesk(Exchange):
    def get_current_price(self, currency='USD'):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/{}.json'.format(
            currency
        )
        price = self.resolve_api_call(url=url, attrs=['bpi', currency, 'rate'])
        return Decimal(price)

    def get_past_price(self, date):
        url = self._get_historical_data_url(date)
        price = self.resolve_api_call(url=url, attrs=['bpi', date])
        return Decimal(str(price))

    def get_historical_data_as_dict(self, start='2013-09-01', end=None):
        if not end:
            end = get_datetime()
        url = self._get_historical_data_url(start, end)
        prices = self.resolve_api_call(url=url, attrs='bpi')
        prices = { k: Decimal(str(v)) for (k,v) in prices.iteritems() }
        return prices

    def get_historical_data_as_list(self, start='2013-09-01', end=None):
        if not end:
            end = get_datetime()
        url = self._get_historical_data_url(start, end)
        dates = self.resolve_api_call(url=url, attrs='bpi')
        ret = [ {'date': k, 'price': Decimal(str(v))} for (k,v) in dates.iteritems() ]
        ret.sort()
        return ret

    def _get_historical_data_url(self, start, end=None):
        if not end:
            end = start
        url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start={}&end={}'.format(
            start, end
        )
        return url