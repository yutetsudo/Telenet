from Télénet.Minitel import Minitel
class Matrix:
    async def run(reader, writer):
        minitel = Minitel(reader, writer)
        minitel.read('SERVICE/VDT/MATRIX/LOGIN.vdt')

        login = await minitel.textInput(x=16, y=12, maxSize=30)
        password = await minitel.textInput(x=16, y=15, passwordField=True)
        print(f"Login : {login}\nPassword : {password}")