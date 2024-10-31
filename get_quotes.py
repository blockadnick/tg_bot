import requests

def get_quotes(symbol):
    symbol = symbol.upper() + "USDT"
    payload = {}
    headers = {}
    url = f"https://api.bybit.com/v5/market/orderbook?category=spot&symbol={symbol}"

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    price = data["result"]["a"][0][0]
    result: str = f"{symbol} price is: {price}"
    return result
