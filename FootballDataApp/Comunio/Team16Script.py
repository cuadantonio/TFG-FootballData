import pymongo
import requests
from bs4 import BeautifulSoup
import re

a, b = 'áãàéíóøöúüćčşÁÉÍÓÚÜ-', 'aaaeiooouuccsAEIOUU '
trans = str.maketrans(a, b)

team = "Real Madrid"
url = "https://www.comuniazo.com/comunio-apuestas/equipos/real-madrid"

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersRealData = db["PlayersRealData"]
comunio = db["ComunioData"]
comunio.delete_many({})

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
playersAux = soup.find("div", {"class": "player-list"})
players = playersAux.find_all("li")
for teamplayer in players:
    playerCell = teamplayer.find("div", {"class":"cell"})
    playerName = str(playerCell.find("strong").text).translate(trans)
    playerPointsAndPrice = playerCell.find("div").text
    playerPointsPos = int(str(playerPointsAndPrice).find(" "))
    playerPricePos = int(str(playerPointsAndPrice).find("−")+2)
    playerPoints = str(playerPointsAndPrice)[0:playerPointsPos]
    playerPrice = str(playerPointsAndPrice)[playerPricePos:len(str(playerPointsAndPrice))]
    player = {"name":playerName, "team":team, "points":playerPoints, "price": playerPrice,"comunioFound":False}
    comunio.insert_one(player)

allPlayers = playersRealData.find({"team": team})
for eachPlayer in allPlayers:
    playerNickname = eachPlayer["nickname"]
    playerName = eachPlayer["name"]

    query1 = comunio.find_one({"name": {"$regex": re.compile(playerNickname, re.IGNORECASE)}, "team": team,"comunioFound":False})
    if query1 != None:
        playerUpdate = {"comunioPoints": query1["points"],"comunioPrice":query1["price"]}
        newvalues1 = {"$set": playerUpdate}
        playerUpdateComunio = {"comunioFound": True}
        newValuesComunio = {"$set" :playerUpdateComunio}
        playersRealData.update_one(eachPlayer, newvalues1)
        comunio.update_one(query1,newValuesComunio)
        continue
    nicknameList = str(playerNickname).split(" ")
    if(len(nicknameList)!=1):
        nicknameAux = nicknameList[1]
        query2 = comunio.find_one({"name": {"$regex": re.compile(nicknameAux, re.IGNORECASE)}, "team": team,"comunioFound":False})
        if query2 != None:
            playerUpdate = {"comunioPoints": query2["points"], "comunioPrice": query2["price"]}
            newvalues2 = {"$set": playerUpdate}
            playerUpdateComunio = {"comunioFound": True}
            newValuesComunio = {"$set": playerUpdateComunio}
            playersRealData.update_one(eachPlayer, newvalues2)
            comunio.update_one(query2, newValuesComunio)
            continue