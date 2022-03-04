import pymongo
import requests
from bs4 import BeautifulSoup
import re

a, b = 'áãàéíóøöúüćčşšÁÉÍÓÚÜ-', 'aaaeiooouuccssAEIOUU '
trans = str.maketrans(a, b)

team = "Elche"
url = "https://www.futmondo.com/team?team=51b889b1e401a15f2c0000f0"

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersRealData = db["PlayersRealData"]
futmondo = db["FutmondoData"]
futmondo.delete_many({})

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
playersAux = soup.find("ul", {"class": "ulPlayers"})
players = playersAux.find_all("li")
for player in players:
    nameAux = player.find("figure",{"class":"photo"})
    name = str(nameAux.find("img")["title"]).translate(trans)
    priceAndPointsAux = player.find("article",{"class":"data"})
    points = priceAndPointsAux.find("article",{"class":"points"}).text
    priceAux = priceAndPointsAux.find("article",{"class":"value"}).text
    pricePos = str(priceAux).find("€")
    price = str(priceAux)[0:pricePos-1]
    player = {"name": name, "team": team, "points": points, "price": price, "futmondoFound": False}
    futmondo.insert_one(player)

allPlayers = playersRealData.find({"team": team})
for eachPlayer in allPlayers:
    playerNickname = eachPlayer["nickname"]
    playerName = eachPlayer["name"]

    query1 = futmondo.find_one({"name": {"$regex": re.compile(playerNickname, re.IGNORECASE)}, "team": team,"futmondoFound":False})
    if query1 != None:
        playerUpdate = {"futmondoPoints": query1["points"],"futmondoPrice":query1["price"]}
        newvalues1 = {"$set": playerUpdate}
        playerUpdateFutmondo = {"futmondoFound": True}
        newValuesFutmondo = {"$set" :playerUpdateFutmondo}
        playersRealData.update_one(eachPlayer, newvalues1)
        futmondo.update_one(query1,newValuesFutmondo)
        continue
    nicknameList = str(playerNickname).split(" ")
    if(len(nicknameList)!=1):
        nicknameAux = nicknameList[1]
        query2 = futmondo.find_one({"name": {"$regex": re.compile(nicknameAux, re.IGNORECASE)}, "team": team,"futmondoFound":False})
        if query2 != None:
            playerUpdate = {"futmondoPoints": query2["points"], "futmondoPrice": query2["price"]}
            newvalues2 = {"$set": playerUpdate}
            playerUpdateFutmondo = {"futmondoFound": True}
            newValuesFutmondo = {"$set": playerUpdateFutmondo}
            playersRealData.update_one(eachPlayer, newvalues2)
            futmondo.update_one(query2, newValuesFutmondo)
            continue