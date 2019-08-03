'''
coin_data.py
Model is for /coin API endpoint
'''

class CoinData():
    def __init__(self, api_response_json):
        self.api_response_json = api_response_json

    def name(self):
        return self.api_response_json['name']

    def price(self):
        return float(self.api_response_json['price'])

    def rank(self):
        return self.api_response_json['rank']

    def market_cap(self):
        return float(self.api_response_json['market_cap'])

    def total_volume_24h(self):
        return float(self.api_response_json['total_volume_24h'])

    def high_24h(self):
        return float(self.api_response_json['high_24h'])

    def low_24h(self):
        return float(self.api_response_json['low_24h'])

    def delta_1h(self):
        return float(self.api_response_json['delta_1h'])

    def delta_24h(self):
        return float(self.api_response_json['delta_24h'])

    def delta_7d(self):
        return float(self.api_response_json['delta_7d'])

    def delta_30d(self):
        return float(self.api_response_json['delta_30d'])