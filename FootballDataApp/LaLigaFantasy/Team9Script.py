import pymongo
import requests
import json
import re

def priceConverter(price):
    x = []
    x[:0] = str(price)
    w = []
    cont = 0
    for i  in range(len(x)-1,-1,-1):
        cont = cont+1
        if cont==3:
            cont=0
            w.insert(0,x[i])
            if i != 0:
                w.insert(0,".")
        else:
            w.insert(0, x[i])
    return "".join(w)

a, b = 'áãàéíóøöúüćčşšÁÉÍÓÚÜ-', 'aaaeiooouuccssAEIOUU '
trans = str.maketrans(a, b)

team = "Espanyol"
slug = "rcd-espanyol"
url = "https://api.laligafantasymarca.com/api/v3/players"
baseUrl = "https://api.laligafantasymarca.com/api/v3/player/"
ids = []

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersRealData = db["PlayersRealData"]
laliga = db["LaLigaFantasyData"]
laliga.delete_many({})

response = requests.request("GET", url)

data = response.text
parse_json = json.loads(data)
json_Response = parse_json

for i in range(len(json_Response)):
    playeraux = json_Response[i]
    if playeraux["team"]["slug"]==slug:
        id = str(playeraux["id"])
        ids.append(id)


for id in ids:
    newUrl = baseUrl+id
    response2 = requests.request("GET", newUrl)

    data2 = response2.text
    parse_json2 = json.loads(data2)
    json_Response2 = parse_json2

    name = str(json_Response2["name"]).translate(trans)
    nickname = str(json_Response2["nickname"]).translate(trans)
    points = str(json_Response2["points"])
    priceAux = json_Response2["marketValue"]
    price = priceConverter(priceAux)
    player = {"name": name, "nickname":nickname, "team": team, "points": points, "price": price, "laligaFound": False}
    laliga.insert_one(player)

allPlayers = playersRealData.find({"team": team})
for eachPlayer in allPlayers:
    playerNickname = eachPlayer["nickname"]
    playerName = eachPlayer["name"]
    query1 = laliga.find_one({"nickname": {"$regex": re.compile(playerNickname, re.IGNORECASE)}, "team": team,"laligaFound":False})
    if query1 != None:
        playerUpdate = {"laligaPoints": query1["points"],"laligaPrice":query1["price"]}
        newvalues1 = {"$set": playerUpdate}
        playerUpdateLaLiga = {"laligaFound": True}
        newValuesLaLiga = {"$set": playerUpdateLaLiga}
        playersRealData.update_one(eachPlayer, newvalues1)
        laliga.update_one(query1, newValuesLaLiga)
        continue
    nicknameList = str(playerNickname).split(" ")
    if (len(nicknameList) != 1):
        nicknameAux = nicknameList[1]
        query2 = laliga.find_one(
            {"nickname": {"$regex": re.compile(nicknameAux, re.IGNORECASE)}, "team": team, "laligaFound": False})
        if query2 != None:
            playerUpdate = {"laligaPoints": query2["points"], "laligaPrice": query2["price"]}
            newvalues2 = {"$set": playerUpdate}
            playerUpdateLaLiga = {"laligaFound": True}
            newValuesLaLiga = {"$set": playerUpdateLaLiga}
            playersRealData.update_one(eachPlayer, newvalues2)
            laliga.update_one(query2, newValuesLaLiga)
            continue
        nicknameAux = nicknameList[0]
        query3 = laliga.find_one(
            {"nickname": {"$regex": re.compile(nicknameAux, re.IGNORECASE)}, "team": team, "laligaFound": False})
        if query3 != None:
            playerUpdate = {"laligaPoints": query3["points"], "laligaPrice": query3["price"]}
            newvalues3 = {"$set": playerUpdate}
            playerUpdateLaLiga = {"laligaFound": True}
            newValuesLaLiga = {"$set": playerUpdateLaLiga}
            playersRealData.update_one(eachPlayer, newvalues3)
            laliga.update_one(query3, newValuesLaLiga)
            continue
    else:
        query4 = laliga.find_one(
            {"name": {"$regex": re.compile(playerName, re.IGNORECASE)}, "team": team, "laligaFound": False})
        if query4 != None:
            playerUpdate = {"laligaPoints": query4["points"], "laligaPrice": query4["price"]}
            newvalues4 = {"$set": playerUpdate}
            playerUpdateLaLiga = {"laligaFound": True}
            newValuesLaLiga = {"$set": playerUpdateLaLiga}
            playersRealData.update_one(eachPlayer, newvalues4)
            laliga.update_one(query4, newValuesLaLiga)
            continue

        query5 = laliga.find_one(
            {"name": {"$regex": re.compile(playerNickname, re.IGNORECASE)}, "team": team, "laligaFound": False})
        if query5 != None:
            playerUpdate = {"laligaPoints": query5["points"], "laligaPrice": query5["price"]}
            newvalues5 = {"$set": playerUpdate}
            playerUpdateLaLiga = {"laligaFound": True}
            newValuesLaLiga = {"$set": playerUpdateLaLiga}
            playersRealData.update_one(eachPlayer, newvalues5)
            laliga.update_one(query5, newValuesLaLiga)
            continue