from exchanges.base import Exchange


class Poloniex(Exchange):

    TICKER_URL = 'https://poloniex.com/public?command=returnTicker'

    @classmethod
    def _current_price_extractor(cls, data):
        return data.get('USDT_BTC').get('last')

    @classmethod
    def _current_bid_extractor(cls, data):
        return data.get('USDT_BTC').get('highestBid')

    @classmethod
    def _current_ask_extractor(cls, data):
        return data.get('USDT_BTC').get('lowestAsk')
