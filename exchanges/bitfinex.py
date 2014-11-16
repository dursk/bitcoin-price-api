from exchange import Exchange

class Bitfinex(Exchange):
    class Meta:
        api_url = 'https://api.bitfinex.com/v1/pubticker/btcusd'
        api_map = {
            'price': 'last_price',
            'bid': 'bid',
            'ask': 'ask'
        }