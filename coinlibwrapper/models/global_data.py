'''
global_data.py
Model is for /global API endpoint
'''

class GlobalData():
    def __init__(self, api_response_json):
        self.api_response_json = api_response_json

    def num_coins(self):
        return self.api_response_json['coins']

    def num_markets(self):
        return self.api_response_json['markets']

    def total_market_cap(self): 
        return float(self.api_response_json['total_market_cap'])

    def total_volume_24h(self):
        return float(self.api_response_json['total_volume_24h'])