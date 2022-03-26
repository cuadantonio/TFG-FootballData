import pymongo
import requests
import json
import re

a, b = 'áãàéíóøöúüćčşšÁÉÍÓÚÜ-', 'aaaeiooouuccssAEIOUU '
trans = str.maketrans(a, b)

teamId = 1
team = "Alaves"
id = 542
url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
collection = db["TeamsMatches"]

querystring = {"league":"140","season":"2021","team":id,"status":"FT"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "107c6e209amsh4c71238714f1793p1c06ecjsn222ae5091f9b"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.text
parse_json = json.loads(data)

jsonResponse = parse_json['response']
for j in range(len(jsonResponse)):
    fixtureId = jsonResponse[j]['fixture']['id']
    homeTeam = jsonResponse[j]['teams']['home']['name']
    homeTeamId = jsonResponse[j]['teams']['home']['id']
    isHomeTeamWinner = jsonResponse[j]['teams']['home']['winner']
    awayTeam = jsonResponse[j]['teams']['away']['name']
    awayTeamId = jsonResponse[j]['teams']['away']['id']
    isAwayTeamWinner = jsonResponse[j]['teams']['away']['winner']
    winner = ''
    if isHomeTeamWinner:
        winner = homeTeam
    elif isAwayTeamWinner:
        winner = awayTeam
    else:
        winner = 'Tie'
    homeGoals = jsonResponse[j]['goals']['home']
    awayGoals = jsonResponse[j]['goals']['away']
    match = {"fixtureId":fixtureId,"homeTeam":homeTeam,"homeTeamId":homeTeamId,"awayTeam":awayTeam,"awayTeamId":awayTeamId,
             "winner":winner,"homeGoals":homeGoals,"awayGoals":awayGoals}
    collection.insert_one(match)
