import pymongo
import requests
from bs4 import BeautifulSoup

a, b = 'áãàéíóúüćşÁÉÍÓÚÜ-', 'aaaeiouucsAEIOUU '
trans = str.maketrans(a, b)

teamId = 18
team = "Sevilla"
url = "https://www.lapreferente.com/E4253C13125-1/sevilla-fc"

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
collection = db["PlayersRealData"]

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
div = soup.find("div", {"id": "jugadoresEquipo"})
table = div.find("table", {"id": "tablePlantilla"})
team_players = table.find_all("tr",{"class":""})

for team_player in team_players:
    number = team_player.find("span", {"id": "plantillaDorsal"}).text
    nameAux1 = team_player.find("a")
    nameAux2 = nameAux1.find_all("span")
    nameAux3 = nameAux2[1].text
    name = nameAux3.translate(trans)
    nicknameAux = nameAux2[0].text
    nickname = nicknameAux.translate(trans)
    player = {"team":team, "teamId": teamId, "number": number, "name": name, "nickname": nickname}
    collection.insert_one(player)