import pymongo
import requests
import json
import re

a, b = 'áãàéíóøöúüćčşšÁÉÍÓÚÜ-', 'aaaeiooouuccssAEIOUU '
trans = str.maketrans(a, b)

teamId = 18
team = "Sevilla"
id = 536
localFixturesIds = []
awayFixturesIds = []

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
byMatch = db["TeamsDataByMatch"]
matches = db["TeamsMatches"]

localFixtures = matches.find({"homeTeamId":536})
for fixture in localFixtures:
    localFixturesIds.append(fixture['fixtureId'])

awayFixtures = matches.find({"awayTeamId":536})
for fixture in awayFixtures:
    awayFixturesIds.append(fixture['fixtureId'])

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

for localFixtureId in localFixturesIds:
    querystring = {"id": localFixtureId}

    headers = {
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "4ca02a97b7msh6060da568552d3bp13d4bejsn549a57cbd0a8"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    parse_json = json.loads(data)
    jsonResponse = parse_json['response'][0]
    round = int(str(jsonResponse['league']['round']).split(" ")[3])
    statistics = jsonResponse['statistics'][0]['statistics']
    shotsOnGoal = statistics[0]['value']
    shotsOffGoal = statistics[1]['value']
    totalShots = statistics[2]['value']
    blockedShots = statistics[3]['value']
    shotsInsidebox = statistics[4]['value']
    shotsOutsidebox = statistics[5]['value']
    fouls = statistics[6]['value']
    corners = statistics[7]['value']
    offsides = statistics[8]['value']
    ballPossession = statistics[9]['value']
    yellowCards = statistics[10]['value']
    redCards = statistics[11]['value']
    goalkeeperSaves = statistics[12]['value']
    totalPasses = statistics[13]['value']
    passesAccurate = statistics[14]['value']
    passesPercentage = statistics[15]['value']
    rivalTeam = jsonResponse['teams']['away']['name']
    rivalTeamId = jsonResponse['teams']['away']['id']
    homeGoals = str(jsonResponse['goals']['home'])
    awayGoals = str(jsonResponse['goals']['away'])
    score = homeGoals+'-'+awayGoals
    winnerLocal = jsonResponse['teams']['home']['winner']
    winnerAway = jsonResponse['teams']['away']['winner']
    winnerId = -1
    if winnerLocal == True:
        winnerId = id
    elif winnerAway == True:
        winnerId = rivalTeamId
    localFixtureToAdd = {"fixtureId": localFixtureId, "round": round, "teamId": id, "teamName": team, "side": "Home",
                         "rivalTeam": rivalTeam, "rivalTeamId": rivalTeamId,
                         "score": score, "shotsOnGoal": shotsOnGoal, "shotsOffGoal": shotsOffGoal,
                         "totalShots": totalShots, "blockedShots": blockedShots,
                         "shotsInsidebox": shotsInsidebox, "shotsOutsidebox": shotsOutsidebox, "fouls": fouls,
                         "corners": corners,
                         "offsides": offsides, "ballPossession": ballPossession, "yellowCards": yellowCards,
                         "redCards": redCards,
                         "goalkeeperSaves": goalkeeperSaves, "totalPasses": totalPasses,
                         "passesAccurate": passesAccurate,
                         "passesPercentage": passesPercentage, "winnerId": winnerId}
    query = byMatch.find_one({"fixtureId":localFixtureId, "teamId":id})
    if query == None:
        byMatch.insert_one(localFixtureToAdd)
        continue
    else:
        update = {"$set":localFixtureToAdd}
        byMatch.update_one(query,update)
        continue

for awayFixtureId in awayFixturesIds:
    querystring = {"id": awayFixtureId}

    headers = {
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "4ca02a97b7msh6060da568552d3bp13d4bejsn549a57cbd0a8"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    parse_json = json.loads(data)
    jsonResponse = parse_json['response'][0]
    round = int(str(jsonResponse['league']['round']).split(" ")[3])
    statistics = jsonResponse['statistics'][1]['statistics']
    shotsOnGoal = statistics[0]['value']
    shotsOffGoal = statistics[1]['value']
    totalShots = statistics[2]['value']
    blockedShots = statistics[3]['value']
    shotsInsidebox = statistics[4]['value']
    shotsOutsidebox = statistics[5]['value']
    fouls = statistics[6]['value']
    corners = statistics[7]['value']
    offsides = statistics[8]['value']
    ballPossession = statistics[9]['value']
    yellowCards = statistics[10]['value']
    redCards = statistics[11]['value']
    goalkeeperSaves = statistics[12]['value']
    totalPasses = statistics[13]['value']
    passesAccurate = statistics[14]['value']
    passesPercentage = statistics[15]['value']
    rivalTeam = jsonResponse['teams']['home']['name']
    rivalTeamId = jsonResponse['teams']['home']['id']
    homeGoals = str(jsonResponse['goals']['home'])
    awayGoals = str(jsonResponse['goals']['away'])
    score = homeGoals+'-'+awayGoals
    winnerLocal = jsonResponse['teams']['home']['winner']
    winnerAway = jsonResponse['teams']['away']['winner']
    winnerId = -1
    if winnerLocal == True:
        winnerId = rivalTeamId
    elif winnerAway == True:
        winnerId = id
    awayFixtureToAdd = {"fixtureId": awayFixtureId, "round": round, "teamId": id, "teamName": team, "side": "Away",
                        "rivalTeam": rivalTeam, "rivalTeamId": rivalTeamId,
                        "score": score, "shotsOnGoal": shotsOnGoal, "shotsOffGoal": shotsOffGoal,
                        "totalShots": totalShots, "blockedShots": blockedShots,
                        "shotsInsidebox": shotsInsidebox, "shotsOutsidebox": shotsOutsidebox, "fouls": fouls,
                        "corners": corners,
                        "offsides": offsides, "ballPossession": ballPossession, "yellowCards": yellowCards,
                        "redCards": redCards,
                        "goalkeeperSaves": goalkeeperSaves, "totalPasses": totalPasses,
                        "passesAccurate": passesAccurate,
                        "passesPercentage": passesPercentage, "winnerId": winnerId}
    query = byMatch.find_one({"fixtureId":awayFixtureId, "teamId":id})
    if query == None:
        byMatch.insert_one(awayFixtureToAdd)
        continue
    else:
        update = {"$set":awayFixtureToAdd}
        byMatch.update_one(query,update)
        continue