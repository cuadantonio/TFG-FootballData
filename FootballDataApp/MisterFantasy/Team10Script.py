import pymongo
import requests
from bs4 import BeautifulSoup

team = "Getafe"
url = "https://mister.mundodeportivo.com/teams/9/getafe"

client = pymongo.MongoClient("mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
collection = db["MisterFantasyData"]

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
div = soup.find("div", {"class": "panel-team"})
team_players = div.find_all("div", {"class": "player-row"})

for team_player in team_players:
    name = team_player.find("a", {"class": "player"})["data-title"]
    price = team_player.find("button", {"class": "btn-white"}).text
    points = team_player.find("div", {"class": "points"}).text
    player = {"name": name, "price":price, "points":points, "team": team}
    collection.insert_one(player)