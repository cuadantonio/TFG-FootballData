import pymongo
import requests
from bs4 import BeautifulSoup

team = "Valencia"
url = "https://www.comuniazo.com/comunio-apuestas/equipos/valencia"

client = pymongo.MongoClient("mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
collection = db["ComunioData"]

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
div = soup.find("div", {"class": "player-list"})
team_players = div.find_all("li")

for team_player in team_players:
    playeraux = team_player.find("div", class_="cell")
    name = playeraux.find_all("strong")[0].text
    pointsAndPrice = playeraux.find_all("div")[0].text
    pos = str(pointsAndPrice).find('−')
    points = str(pointsAndPrice)[0:pos-8]
    price = str(pointsAndPrice)[pos+2:len(str(pointsAndPrice))]
    player = {"name": name, "price":price, "points":points, "team": team}
    collection.insert_one(player)