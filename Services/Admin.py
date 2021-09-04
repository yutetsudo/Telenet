from Télénet.Minitel import Minitel
import os

class Admin:
    async def run(reader, writer):
        minitel = Minitel(reader, writer)
        pass