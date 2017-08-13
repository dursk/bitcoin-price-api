from decimal import Decimal

from exchanges.helpers import get_datetime, get_response


class CoinDesk(object):

    @classmethod
    def get_current_price(cls, currency='USD'):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/{}.json'.format(
            currency
        )
        data = get_response(url)
        price = data['bpi'][currency]['rate_float']
        return Decimal(price)

    @classmethod
    def get_past_price(cls, date):
        data = cls._get_historical_data(date)
        price = data['bpi'][date]
        return Decimal(str(price))

    @classmethod
    def get_historical_data_as_dict(cls, start='2013-09-01', end=None):
        if not end:
            end = get_datetime()
        data = cls._get_historical_data(start, end)
        prices = data['bpi']
        prices = {k: Decimal(str(v)) for (k,v) in prices.iteritems()}
        return prices

    @classmethod
    def get_historical_data_as_list(cls, start='2013-09-01', end=None):
        if not end:
            end = get_datetime()
        data = cls._get_historical_data(start, end)
        dates = data['bpi']
        ret = [
            {'date': k, 'price': Decimal(str(v))} for (k,v) in dates.iteritems()
        ]
        ret.sort()
        return ret

    @classmethod
    def _get_historical_data(cls, start, end=None):
        if not end:
            end = start
        url = (
            'https://api.coindesk.com/v1/bpi/historical/close.json'
            '?start={}&end={}'.format(
                start, end
            )
        )
        return get_response(url)
