from helpers import get_datetime, get_response
from decimal import Decimal

class Exchange(object):
    @classmethod
    def resolve_simple_api_call(cls, url, attrs):
        resp = get_response(url)
        attrs = attrs if isinstance(attrs, list) else [attrs]
        for attr in attrs:
            resp = resp[attr]
        return resp

    @classmethod
    def get_current_price(cls):
        return Decimal(cls.resolve_simple_api_call(cls.Meta.api_url, cls.Meta.api_map['price']))

    @classmethod
    def get_current_bid(cls):
        return Decimal(cls.resolve_simple_api_call(cls.Meta.api_url, cls.Meta.api_map['bid']))

    @classmethod
    def get_current_ask(cls):
        return Decimal(cls.resolve_simple_api_call(cls.Meta.api_url, cls.Meta.api_map['ask']))