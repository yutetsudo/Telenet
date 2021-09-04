from Télénet.Minitel import Minitel
from SERVICE import *
import asyncio, telnetlib3

PORT = 3615

async def main(reader, writer):
    minitel = Minitel(reader, writer)
    minitel.init()

    #await Test.run(reader, writer)

    minitel.printStatus("Télénet 3615 Ver : 1.0b")
    minitel.read('3615.vdt')
    minitel.clearStatus()

    async def getCode():
        code = await loop.create_task(minitel.textInput(x=18, y=15, maxSize=22))
        if code.lower() == "matrix" or code.lower() == "1":
            await Matrix.run(reader, writer)
        elif code.lower() == "filbleu" or code.lower() == "2":
            await Filbleu.run(reader, writer)
        elif code.lower() == "tavie" or code.lower() == "3":
            await Tavie.run(reader, writer)
        elif code.lower() == "hacker" or code.lower() == "4":
            await WebsocketClient.run(reader, writer, 'ws://mntl.joher.com:2018/?echo')
            await asyncio.gather(WebsocketClient.w2m(), WebsocketClient.m2w())
        elif code.lower() == "test":
            await Test.run(reader, writer)
        else:
            minitel.beep()
            minitel.printStatus('Code incorect')
            await getCode()

    await getCode()
    minitel.hang()


loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=PORT, shell=main)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())
