import pymongo
import requests
from bs4 import BeautifulSoup
import re

a, b = 'áãàéíóøöúüćčşšÁÉÍÓÚÜ-', 'aaaeiooouuccssAEIOUU '
trans = str.maketrans(a, b)

months = {"enero":"01","febrero":"02","marzo":"03","abril":"04","mayo":"05","junio":"06","julio":"07","agosto":"08","septiembre":"09","octubre":"10","noviembre":"11","diciembre":"12"}
days = {"1":"01","2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09","10":"10","11":"11","12":"12","13":"13","14":"14","15":"15","16":"16","17":"17","18":"18","19":"19","20":"20","21":"21","22":"22","23":"23","24":"24","25":"25","26":"26","27":"27","28":"28","29":"29","30":"30","31":"31"}

team = "Almeria"
url = "https://biwenger.as.com/blog/equipos/almeria/"
urls = []

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersRealData = db["PlayersRealData"]
biwenger = db["BiwengerData"]
biwenger.delete_many({})

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
playersAux = soup.find_all("div", {"class": "player-info"})

for playerAux in playersAux:
    name = str(playerAux.find_all("div")[4].find("a").text).translate(trans)
    urlAux = playerAux.find_all("div")[4].find("a")["href"]
    price = playerAux.find_all("div")[4].find("div",{"class":"price"}).text
    points = playerAux.find_all("div")[2].find("div",{"class":"player-points"}).text
    page2 = requests.get(urlAux)
    soup2 = BeautifulSoup(page2.content, "html.parser")
    infoAux1 = soup2.find("div", {"class": "player-profile-leftside"})
    dateAux = infoAux1.find_all("span")[7]
    dateSplit = str(dateAux.text).split(" ")
    if len(dateSplit) != 1:
        month = months[dateSplit[1]]
        date = days[dateSplit[0]] + "/" + month + "/" + dateSplit[2]
    else:
        date = "00/00/0000"
    player = {"name": name, "team": team, "points": points, "price": price, "date":date, "biwengerFound": False}
    biwenger.insert_one(player)

allPlayers = playersRealData.find({"team": team})
for eachPlayer in allPlayers:
    playerDate = eachPlayer["date"]
    query1 = biwenger.find_one({"date": {"$regex": re.compile(playerDate, re.IGNORECASE)}, "team": team,"biwengerFound":False})
    if query1 != None:
        playerUpdate = {"biwengerPoints": query1["points"],"biwengerPrice":query1["price"]}
        newvalues1 = {"$set": playerUpdate}
        playerUpdateBiwenger = {"biwengerFound": True}
        newValuesBiwenger = {"$set": playerUpdateBiwenger}
        playersRealData.update_one(eachPlayer, newvalues1)
        biwenger.update_one(query1, newValuesBiwenger)
        continue

    playerNickname = eachPlayer["nickname"]
    query2 = biwenger.find_one(
        {"name": {"$regex": re.compile(playerNickname, re.IGNORECASE)}, "team": team, "biwengerFound": False})
    if query2 != None:
        playerUpdate = {"biwengerPoints": query2["points"], "biwengerPrice": query2["price"]}
        newvalues2 = {"$set": playerUpdate}
        playerUpdateBiwenger = {"biwengerFound": True}
        newValuesBiwenger = {"$set": playerUpdateBiwenger}
        playersRealData.update_one(eachPlayer, newvalues2)
        biwenger.update_one(query2, newValuesBiwenger)
        continue

    nickNameList = playerNickname.split(" ")
    if len(nickNameList) != 1:
        nickNameAux = nickNameList[1]
        query3 = biwenger.find_one(
            {"name": {"$regex": re.compile(nickNameAux, re.IGNORECASE)}, "team": team, "biwengerFound": False})
        if query3 != None:
            playerUpdate = {"biwengerPoints": query3["points"], "biwengerPrice": query3["price"]}
            newvalues3 = {"$set": playerUpdate}
            playerUpdateBiwenger = {"biwengerFound": True}
            newValuesBiwenger = {"$set": playerUpdateBiwenger}
            playersRealData.update_one(eachPlayer, newvalues3)
            biwenger.update_one(query3, newValuesBiwenger)
            continue



