import pymongo
import requests
from bs4 import BeautifulSoup
import re

a, b = 'áãàéíóøöúüćčşšÁÉÍÓÚÜ-', 'aaaeiooouuccssAEIOUU '
trans = str.maketrans(a, b)

team = "Sevilla"
url = "https://mister.mundodeportivo.com/teams/17/"

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersRealData = db["PlayersRealData"]
misterfantasy = db["ComunioData"]
misterfantasy.delete_many({})

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
playersAux = soup.find_all("ul", {"class": "player-list"})
players = playersAux[1].find_all("div",{"class":"player-row"})
for player in players:
    name = str(player.find("a")["data-title"]).translate(trans)
    points = player.find("div",{"class":"points"}).text
    priceAux = player.find("div",{"class":"player-btns"})
    price = priceAux.find("button").text
    player = {"name": name, "team": team, "points": points, "price": price, "misterFantasyFound": False}
    misterfantasy.insert_one(player)

allPlayers = playersRealData.find({"team": team})
for eachPlayer in allPlayers:
    playerNickname = eachPlayer["nickname"]
    playerName = eachPlayer["name"]
    query1 = misterfantasy.find_one({"name": {"$regex": re.compile(playerNickname, re.IGNORECASE)}, "team": team,"misterFantasyFound":False})
    if query1 != None:
        playerUpdate = {"misterFantasyPoints": query1["points"],"misterFantasyPrice":query1["price"]}
        newvalues1 = {"$set": playerUpdate}
        playerUpdateMisterFantasy = {"misterFantasyFound": True}
        newValuesMisterFantasy = {"$set": playerUpdateMisterFantasy}
        playersRealData.update_one(eachPlayer, newvalues1)
        misterfantasy.update_one(query1, newValuesMisterFantasy)
        continue
    nicknameList = str(playerNickname).split(" ")
    if (len(nicknameList) != 1):
        nicknameAux = nicknameList[1]
        query2 = misterfantasy.find_one(
            {"name": {"$regex": re.compile(nicknameAux, re.IGNORECASE)}, "team": team, "misterFantasyFound": False})
        if query2 != None:
            playerUpdate = {"misterFantasyPoints": query2["points"], "misterFantasyPrice": query2["price"]}
            newvalues2 = {"$set": playerUpdate}
            playerUpdateMisterFantasy = {"misterFantasyFound": True}
            newValuesMisterFantasy = {"$set": playerUpdateMisterFantasy}
            playersRealData.update_one(eachPlayer, newvalues2)
            misterfantasy.update_one(query2, newValuesMisterFantasy)
            continue

    else:
        nameList = str(playerName).split(" ")
        nameAux = nameList[0]+" "+nameList[2]
        query3 = misterfantasy.find_one(
            {"name": {"$regex": re.compile(nameAux, re.IGNORECASE)}, "team": team, "misterFantasyFound": False})
        if query3 != None:
            playerUpdate = {"misterFantasyPoints": query3["points"], "misterFantasyPrice": query3["price"]}
            newvalues3 = {"$set": playerUpdate}
            playerUpdateMisterFantasy = {"misterFantasyFound": True}
            newValuesMisterFantasy = {"$set": playerUpdateMisterFantasy}
            playersRealData.update_one(eachPlayer, newvalues3)
            misterfantasy.update_one(query3, newValuesMisterFantasy)
            continue