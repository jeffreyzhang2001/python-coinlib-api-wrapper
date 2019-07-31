# coinlibcore.py
import requests

class Coinlib():
    BASE_URL = "https://coinlib.io/api/v1"
    def __init__(self, api_key): # A Coinlib API key. More info at: https://coinlib.io/apidocs.
        self.api_key = api_key

    def get_url(self, endpoint, symbol, pref_currency="USD"):
        url = f"{self.BASE_URL}{endpoint}?key={self.api_key}&pref={pref_currency}&symbol={symbol}"
        return(url)
        #api_response_json = (requests.get(url)).json()
        #return(api_response_json["price"]+f" {symbol}")