from Télénet.Minitel import Minitel
class Test:
    async def run(reader, writer):
        minitel = Minitel(reader, writer)
        minitel.init()


        minitel.setPos(0, 1)
        minitel.setColor(fg = 'GREEN', bg = 'RED')
        minitel.print(f"£°àâäèéêëîïôöùûüç←↑→↓¼½¡—|")
        #ligne = await minitel.textInput(x=2, y=2, fg = 'BLUE', bg = 'GREEN', maxSize=3)
        minitel.setPos(0, 2)
        minitel.setSize('NORMAL')
        minitel.print(f"NORMAL SIZE")
        minitel.setPos(0, 4)
        minitel.setSize('DOUBLE_HEIGHT')
        minitel.print(f"DOUBLE HEIGHT")
        minitel.setPos(0, 5)
        minitel.setSize('DOUBLE_WIDTH')
        minitel.print(f"DOUBLE WIDTH")
        minitel.setPos(0, 7)
        minitel.setSize('DOUBLE')
        minitel.print(f"DOUBLE")
