from exchange import Exchange

class OKCoin(Exchange):
    class Meta:
        api_url = 'https://www.okcoin.com/api/ticker.do?ok=1'
        api_map = {
            'price': ['ticker', 'last'],
            'bid': ['ticker', 'buy'],
            'ask': ['ticker', 'sell']
        }