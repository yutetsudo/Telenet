from Télénet.Minitel import Minitel
class Tavie:
    async def run(reader, writer):
        minitel = Minitel(reader, writer)
        minitel.init()
        minitel.read('SERVICE/VDT/TAVIE/HOME.vdt')

        user = await minitel.textInput(x=10, y=11)
        print(f"User: {user}")
        