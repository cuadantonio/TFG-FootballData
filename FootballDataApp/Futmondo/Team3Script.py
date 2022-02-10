import pymongo
import requests
from bs4 import BeautifulSoup

team = "Atletico Madrid"
url = "https://www.futmondo.com/team?team=504e581e4d8bec9a670000c8"

client = pymongo.MongoClient("mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
collection = db["FutmondoData"]

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
ul = soup.find("ul", {"class": "ulPlayers"})
team_players = ul.find_all("li")

for team_player in team_players:
    nameaux = team_player.find("a", {"class": "name"}).text
    namepos = str(nameaux).find("\n")
    name = str(nameaux)[0:namepos - 1]
    priceaux = team_player.find("article", {"class": "value"}).text
    pricepos = str(priceaux).find(" ")
    price = str(priceaux)[0:pricepos]
    points = team_player.find("article", {"class": "points"}).text
    player = {"name": name, "price":price, "points":points, "team": team}
    collection.insert_one(player)