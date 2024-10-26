import websockets
import asyncio
from random import randint

message_to_send = ""

def random_num() -> int:
    num = randint(1, 20)
    return num

async def send_message(ws, message):
    await ws.send(message)
    print("Message sent:", message)

async def receive_message(ws):
    msg = await ws.recv()
    print(msg)
    return msg

async def listen():
    url = 'wss://echo.websocket.org/'

    async with websockets.connect(url) as ws:
        while True:
            message_to_send = "Test message " + str(random_num())
            received_msg = await receive_message(ws) 
            await send_message(ws, message_to_send)
            await asyncio.sleep(0.3)
            if received_msg == "Test message 20":
                break

asyncio.run(listen())
