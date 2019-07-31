# Python Coinlib API Wrapper
This is a Python package that simplifies access to [Coinlib's REST API](https://coinlib.io/apidocs) by directly routing all endpoints and parameters through Python objects.

Coinlib is a cryptocurrency data interface that aggregates real-time market data from over 30 exchanges.

## Installation
(The only dependency included is `requests`). You can install this package using:
`pip install git+https://github.com/jeffreyzhang2001/python-coinlib-api-wrapper.git`

## Quickstart
### API Key
You will need a Coinlib API key, which can be generated at https://coinlib.io/ with an account.
## Usage
With this requirement satisfied, you can instantiate an instance of the Coinlib API Wrapper as follows:
`coinlib = Coinlib('API_KEY_GOES_HERE')`

> With this lazy `coinlib` instance, you are able to access Coinlib's data in 3 main routes: **global data, data sorted by metrics, and individual coin data** (details in Documentation section). 
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
`2.14`


## Documentation
WIP

These aforementioned 3 routes **(global, sorted, individual)** are accessed by instantiating on the initially generated lazy `coinlib` object:

Note that delta values may vary with different fiat currencies due to the availability of said currencies on different exchanges.

1. `coin_instance = coinlib.coin('symbol')`
2. `market_instance = coinlib.global('arguments WIP')`
3. `coin_instance = coinlib.coin('arguments WIP')`
