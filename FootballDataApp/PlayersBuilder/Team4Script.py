import pymongo
import requests
from bs4 import BeautifulSoup
import re

a, b = 'áãàéíóøöúüćčşšÁÉÍÓÚÜ-', 'aaaeiooouuccssAEIOUU '
trans = str.maketrans(a, b)

teamId = 4
team = "Barcelona"
url = "https://www.lapreferente.com/E6164C13125-1/fc-barcelona"
prefix = "https://www.lapreferente.com/"
urls = []

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
    suffix = nameAux1["href"]
    playerUrl = prefix+suffix
    urls.append(playerUrl)
    player = {"team":team, "teamId": teamId, "number": number, "name": name, "nickname": nickname}
    collection.insert_one(player)

for playerUrl in urls:
    page2 = requests.get(playerUrl)
    soup2 = BeautifulSoup(page2.content, "html.parser")
    playerNameAux = soup2.find("span",{"style":"font-style:italic;position:absolute;width:100%"}).text
    playerName = playerNameAux.translate(trans)
    dateAux = soup2.find_all("font")
    pos = -1
    for i in range(len(dateAux)):
        if dateAux[i].text == "FECHA DE NACIMIENTO: ":
            pos = i
            break
    dateAux2 = dateAux[pos+1].text
    query = collection.find_one({"name": {"$regex": re.compile(playerName, re.IGNORECASE)}, "team": team, "teamId": teamId})
    queryFilter = {"name": playerName}
    playerUpdate = {"date":dateAux2}
    newValues = {"$set": playerUpdate}
    collection.update_one(queryFilter, newValues)