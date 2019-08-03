# Python Coinlib API Wrapper
This is a Python package that simplifies access to [Coinlib's REST API](https://coinlib.io/apidocs) by directly routing all endpoints and parameters through Python objects.

Coinlib is a cryptocurrency data interface that aggregates real-time market data from over 30 exchanges.

## Installation
Python 3 is required. You can install this package using:

`pip install git+https://github.com/jeffreyzhang2001/python-coinlib-api-wrapper.git`

## Quickstart
### API Key
You will need a Coinlib API key, which can be generated at https://coinlib.io/ with an account.
## Usage
With this requirement satisfied, you can instantiate an instance of the Coinlib API Wrapper as follows:

`coinlib = Coinlib('API_KEY_GOES_HERE')`

> With this lazy `coinlib` instance, you are able to access Coinlib's data through 3 main API endpoints: **individual coin data, sorted coin data, and global market data** (details in Documentation section). 
---
**For example**, let's say you wanted to find out the % change for BTC over the last 24h, across all major exchanges. You would create a coin instance as follows: 

`coin_instance = coinlib.coin('symbol')`

Then, you would simply call the following function on `coin_instance` to store the value as a percentage in `24h_change`:

`24h_change = coin_instance.delta_24h()`

---
**Sample Code**
```
coinlib = Coinlib('API_KEY_GOES_HERE')
coin_instance = coinlib.coin('symbol')
24h_change = coin_instance.delta_24h()
print(24h_change)
```

**Sample Output**
```2.14```


## Documentation

### Notes
> Delta values may vary with different fiat currencies set as the `pref_currency` due to the availability of certain currencies on some exchanges, thus yielding different average deltas.

> An API key must be generated to use this API wrapper. You can find one for free on your profile by signing up for an account at https://coinlib.io.

> A full list of supported exchanges can be found at: https://coinlib.io/exchanges.

> The `pref_currency` argument will accept any standard fiat alphabetic code (e.g. USD, CAD, JPY) or any supported cryptocurrency abbreviation - even the obscure ones (e.g. BTC, ETH, LTC).

To use this wrapper, a Coinlib object should first be initialized as follows:
```coinlib = Coinlib('API_KEY_GOES_HERE')```

Following, the 3 Coinlib API endpoints **(/coin, /coinlist, and /global)** are accessed by further instantiating on the lazy `coinlib` object:


## Individual Data
> Instantiate a coin instance to call the following methods on:
`coin_instance = coinlib.coin('coin_symbol', 'pref_currency')`
This instance is assigned a specific cryptocurrency, and all method calls on it will return information on this cryptocurrency.

E.g. `coin_instance.name()`

| Method  | Functionality |
| ------------- | ------------- |
| name() | Returns the full name of the cryptocurrency as a string. |
| price() | Returns the current market price of the cryptocurrency, as a float (in `pref_currency`)  |
| rank() | Returns the relative 'rank' of the coin in terms of market cap, as an integer. (Lower is better.)|
| market_cap()  | Returns the total market cap of the cryptocurrency, as a float (in `pref_currency`).  |
| total_volume_24h() | Returns the total volume of the cryptocurrency traded across all supported exchanges in the last 24 hours, as a float (`in pref_currency`). |
| high_24h()  | Returns the highest recorded market price of the cryptocurrency in the last 24 hours, as a float (`in pref_currency`). |
| low_24h() | Returns the lowest recorded market price of the cryptocurrency in the last 24 hours, as a float (`in pref_currency`).  |
| delta_1h()  | Returns the percentage change of the cryptocurrency's average market price in the last hour, as a float. `E.g. Returning 2.03 would indicate a +2.03% change in the market price. -2.03 would indicate a -2.03% change.`  |
| delta_24h() | Returns the percentage change of the cryptocurrency's average market price in the last 24 hours, as a float. `E.g. Returning 2.03 would indicate a +2.03% change in the market price.` |
| delta_7d()  | Returns the percentage change of the cryptocurrency's average market price in the last 7 days, as a float. `E.g. Returning 2.03 would indicate a +2.03% change in the market price.` |
| delta_30d() | Returns the percentage change of the cryptocurrency's average market price in the last 30 days, as a float. `E.g. Returning 2.03 would indicate a +2.03% change in the market price.` |



## Sorted Data
> Instantiate a coinlist instance to call the following methods on:
`coinlist_instance = coinlib.coinlist('pref_currency', 'sort_type')`

E.g. `market_instance.num_coins()`

| Method  | Functionality |
| ------------- | ------------- |
| WIP | WIP  |


## Global Market Data
> Instantiate a global market instance to call the following methods on:
`market_instance = coinlib.globalmarket('pref_currency')`

E.g. `market_instance.num_coins()`

| Method  | Functionality |
| ------------- | ------------- |
| num_coins() | Returns the total number of cryptocurrencies listed across all supported exchanges as an integer. |
| num_market() | Returns the total number of trade pairs across all supported exchanges as an integer.  |
| total_market_cap() | Returns the total market cap of every cryptocurrency listed on all supported exchanges, **combined**, as a float (in `pref_currency`).  |
| total_volume_24h() | Returns the total volume of all cryptocurrencies traded across all supported exchanges in the last 24 hours, as a float (in `pref_currency`). |