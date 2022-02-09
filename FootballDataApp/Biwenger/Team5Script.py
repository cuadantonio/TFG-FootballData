import pymongo
import requests
from bs4 import BeautifulSoup

team = "Real Betis"
url = "https://www.infobiwenger.com/equipos/betis"

client = pymongo.MongoClient("mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
collection = db["BiwengerData"]

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
team_players = soup.find_all("div", {"class": "datos"})

for team_player in team_players:
    nameaux = team_player.find("div",{"class": "equipo-col-jugador-datos"})
    name = nameaux.find("span").text
    priceaux = team_player.find("div",{"class": "equipo-col-jugador-valor"})
    price = priceaux.find_all("span")[0].text
    pointsaux = team_player.find("div",{"class": "equipo-col-jugador-puntos"})
    points = pointsaux.find("span").text
    player = {"name": name, "price":price, "points":points, "team": team}
    collection.insert_one(player)