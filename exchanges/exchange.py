from helpers import get_datetime, get_response
from decimal import Decimal

class Exchange(object):
    def resolve_api_call(self, url=None, attrs=[], key=None):
        url = url if url else self.api_url

        json = get_response(url)

        if key:
            attrs = self.api_map[key]

        attrs = attrs if isinstance(attrs, list) else [attrs]
        for attr in attrs:
            json = json[attr]
        return json

    def get_current_price(self):
        return Decimal(self.resolve_api_call(key='price'))

    def get_current_bid(cls):
        return Decimal(self.resolve_api_call(key='bid'))

    def get_current_ask(cls):
        return Decimal(self.resolve_api_call(key='ask'))