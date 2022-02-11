import pymongo
import requests
import json

team = "Espanyol"
url = "https://api.laligafantasymarca.com/api/v3/player/team/8"

client = pymongo.MongoClient("mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
collection = db["LaLigaFantasyData"]

response = requests.request("GET", url)

data = response.text
parse_json = json.loads(data)
json_Response = parse_json['players']

for i in range(len(json_Response)):
    playeraux = json_Response[i]
    name = playeraux['nickname']
    price = playeraux['marketValue']
    points = playeraux['points']
    player = {"name": name, "price": price, "points": points, "team": team}
    collection.insert_one(player)