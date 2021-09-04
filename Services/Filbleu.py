from Télénet.Minitel import Minitel
import requests

minitel = None

class Filbleu:
    async def run(reader, writer):
        global minitel
        minitel = Minitel(reader, writer)
        minitel.init()
        minitel.read('SERVICE/VDT/FILBLEU/HOME.vdt')
        await Filbleu.getLine()


    async def getLine():       
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        ligne = await minitel.textInput(x=27, y=11, maxSize=3)
        request_body = {
                "option": "com_infosvoyageurs",
                "view": "tempsreel",
                "format": "json",
                "task": "tempsreel.getVehiclesOnLine",
                "id_ligne": f"{ligne}",
                "direction_ligne": "0"
        }
        response = requests.post('https://www.filbleu.fr/horaires-et-trajet/vehicule-temps-reel', data=request_body, headers=headers)
        if not response.json()['data']:
            minitel.printStatus("Cette ligne n'existe pas")
            await Filbleu.getLine()
        elif not response.json()['data']['vehicles']:
            minitel.printStatus("Aucun véhicule sur cette ligne")
            await Filbleu.getLine()
        else:
            await Filbleu.VTR(response.json()['data'])


    async def VTR(response):
        minitel.clearAll()
        minitel.read('SERVICE/VDT/FILBLEU/VTR.vdt')
        minitel.setPos(10, 5)
        minitel.print(response['line'])
        minitel.setPos(16, 5)
        minitel.print(response['end'])
        y = 10
        for vehicle in response['vehicles']:
            if y <= 20:
                minitel.setPos(2, y)
                minitel.print(str(vehicle['ref']))
                minitel.setPos(9, y)
                minitel.print(vehicle['trip']['line']['arrivals'][0]['stoppoint']['label'])
                y = y + 2

        loop = True
        while loop:
            key = await minitel.getKey()
            if key == "SOMMAIRE":
                loop = False
                await Filbleu.run(minitel)
            elif key == "REPETITION":
                loop = False
                await Filbleu.VTR(response)
            else:
                minitel.printStatus("Touche sans effet")

