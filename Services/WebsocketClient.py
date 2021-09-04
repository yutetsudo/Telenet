from Télénet.Minitel import Minitel
import asyncio
import websockets

mt = None
ws = None

class WebsocketClient:
    async def run(reader, writer, uri):
        global mt, ws
        mt = Minitel(reader, writer)
        ws = await websockets.connect(uri, ping_interval=None, ping_timeout=None)

    async def w2m():
        while True:
            data = await ws.recv()
            mt.sendData(data)

    async def m2w():
        while True:
            key = await mt.reciveData()
            if key != None:
                await ws.send(key)
                key = None
            else:
                await asyncio.sleep(0.1)