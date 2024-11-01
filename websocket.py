import asyncio
import websockets
import json


BYBIT_SPOT_WEBSOCKET_URL = "wss://stream.bybit.com/v5/public/spot"

async def listen_to_orderbook(symbol):
    symbol = str(symbol.upper()) + "USDT"
    subscription_message = {
        "op": "subscribe",
        "args": [f"orderbook.50.{symbol}"]
    }

    async with websockets.connect(BYBIT_SPOT_WEBSOCKET_URL) as websocket:
        await websocket.send(json.dumps(subscription_message))
        print("Subscribed to orderbook")
        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                try:
                    price = data['data']['a']
                    try:
                        print(price[0])
                    except:
                        pass
                except KeyError:
                    pass
            except Exception as e:
                print("Error:", e)
                break

asyncio.get_event_loop().run_until_complete(listen_to_orderbook('mnt'))