import pymongo
import requests
import json
import re

a, b = 'áãàéíóøöúüćčşšÁÉÍÓÚÜ-', 'aaaeiooouuccssAEIOUU '
trans = str.maketrans(a, b)

teamId = 12
team = "Levante"
id = 539
url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
collection = db["TeamsData"]

querystring = {"league": "140", "season": "2021", "team": id}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "b831264599msh2c6c731267260fcp1fd535jsne2d2f2c847fb"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.text
parse_json = json.loads(data)

jsonResponse = parse_json['response']

teamId = jsonResponse['team']['id']
teamName = jsonResponse['team']['name']
logoURL = jsonResponse['team']['logo']

yellowCards0to15 = jsonResponse['cards']['yellow']['0-15']['total']
if yellowCards0to15 == None:
    yellowCards0to15 = 0
else:
    yellowCards0to15 = int(yellowCards0to15)

yellowCards16to30 = jsonResponse['cards']['yellow']['16-30']['total']
if yellowCards16to30 == None:
    yellowCards16to30 = 0
else:
    yellowCards16to30 = int(yellowCards16to30)

yellowCards31to45 = jsonResponse['cards']['yellow']['31-45']['total']
if yellowCards31to45 == None:
    yellowCards31to45 = 0
else:
    yellowCards31to45 = int(yellowCards31to45)

yellowCards46to60 = jsonResponse['cards']['yellow']['46-60']['total']
if yellowCards46to60 == None:
    yellowCards46to60 = 0
else:
    yellowCards46to60 = int(yellowCards46to60)

yellowCards61to75 = jsonResponse['cards']['yellow']['61-75']['total']
if yellowCards61to75 == None:
    yellowCards61to75 = 0
else:
    yellowCards61to75 = int(yellowCards61to75)

yellowCards76to90 = jsonResponse['cards']['yellow']['76-90']['total']
if yellowCards76to90 == None:
    yellowCards76to90 = 0
else:
    yellowCards76to90 = int(yellowCards76to90)

yellowCards91to105 = jsonResponse['cards']['yellow']['91-105']['total']
if yellowCards91to105 == None:
    yellowCards91to105 = 0
else:
    yellowCards91to105 = int(yellowCards91to105)

yellowCards106to120 = jsonResponse['cards']['yellow']['106-120']['total']
if yellowCards106to120 == None:
    yellowCards106to120 = 0
else:
    yellowCards106to120 = int(yellowCards106to120)

totalYellowCards = yellowCards0to15 + yellowCards16to30 + yellowCards31to45 + yellowCards46to60 + yellowCards61to75 + yellowCards76to90 + yellowCards91to105 + yellowCards106to120

redCards0to15 = jsonResponse['cards']['red']['0-15']['total']
if redCards0to15 == None:
    redCards0to15 = 0
else:
    redCards0to15 = int(redCards0to15)

redCards16to30 = jsonResponse['cards']['red']['16-30']['total']
if redCards16to30 == None:
    redCards16to30 = 0
else:
    redCards16to30 = int(redCards16to30)

redCards31to45 = jsonResponse['cards']['red']['31-45']['total']
if redCards31to45 == None:
    redCards31to45 = 0
else:
    redCards31to45 = int(redCards31to45)

redCards46to60 = jsonResponse['cards']['red']['46-60']['total']
if redCards46to60 == None:
    redCards46to60 = 0
else:
    redCards46to60 = int(redCards46to60)

redCards61to75 = jsonResponse['cards']['red']['61-75']['total']
if redCards61to75 == None:
    redCards61to75 = 0
else:
    redCards61to75 = int(redCards61to75)

redCards76to90 = jsonResponse['cards']['red']['76-90']['total']
if redCards76to90 == None:
    redCards76to90 = 0
else:
    redCards76to90 = int(redCards76to90)

redCards91to105 = jsonResponse['cards']['red']['91-105']['total']
if redCards91to105 == None:
    redCards91to105 = 0
else:
    redCards91to105 = int(redCards91to105)

redCards106to120 = jsonResponse['cards']['red']['106-120']['total']
if redCards106to120 == None:
    redCards106to120 = 0
else:
    redCards106to120 = int(redCards106to120)

totalRedCards = redCards0to15 + redCards16to30 + redCards31to45 + redCards46to60 + redCards61to75 + redCards76to90 + redCards91to105 + redCards106to120

homeCleanSheets = jsonResponse['clean_sheet']['home']
awayCleanSheets = jsonResponse['clean_sheet']['away']

homeFailedToScore = jsonResponse['failed_to_score']['home']
awayFailedToScore = jsonResponse['failed_to_score']['away']

totalWins = jsonResponse['fixtures']['wins']['total']
totalLoses = jsonResponse['fixtures']['loses']['total']
totalDraws = jsonResponse['fixtures']['draws']['total']

homeGoalsForAverage = float(jsonResponse['goals']['for']['average']['home'])
awayGoalsForAverage = float(jsonResponse['goals']['for']['average']['away'])
totalGoalsForAverage = float(jsonResponse['goals']['for']['average']['total'])

homeGoalsAgainstAverage = float(jsonResponse['goals']['against']['average']['home'])
awayGoalsAgainstAverage = float(jsonResponse['goals']['against']['average']['away'])
totalGoalsAgainstAverage = float(jsonResponse['goals']['against']['average']['total'])

homeGoalsFor = jsonResponse['goals']['for']['total']['home']
awayGoalsFor = jsonResponse['goals']['for']['total']['away']
totalGoalsFor = jsonResponse['goals']['for']['total']['total']

homeGoalsAgainst = jsonResponse['goals']['against']['total']['home']
awayGoalsAgainst = jsonResponse['goals']['against']['total']['away']
totalGoalsAgainst = jsonResponse['goals']['against']['total']['total']

scoredPenaltiesPercentage = jsonResponse['penalty']['scored']['percentage']
scoredPenalties = jsonResponse['penalty']['scored']['total']
missedPenaltiesPercentage = jsonResponse['penalty']['missed']['percentage']
missedPenalties = jsonResponse['penalty']['missed']['total']

team = {"id":teamId,"name":teamName,"logo":logoURL,"totalYellowCards":totalYellowCards,"totalRedCards":totalRedCards,
        "homeCleanSheets":homeCleanSheets,"awayCleanSheets":awayCleanSheets,"homeFailedToScore":homeFailedToScore,
        "awayFailedToScore":awayFailedToScore,"totalWins":totalWins,"totalLoses":totalLoses,"totalDraws":totalDraws,
        "homeGoalsForAverage":homeGoalsForAverage,"awayGoalsForAverage":awayGoalsForAverage,"totalGoalsForAverage":totalGoalsForAverage,
        "homeGoalsAgainstAverage":homeGoalsAgainstAverage,"awayGoalsAgainstAverage":awayGoalsAgainstAverage,"totalGoalsAgainstAverage":totalGoalsAgainstAverage,
        "homeGoalsFor":homeGoalsFor,"awayGoalsFor":awayGoalsFor,"totalGoalsFor":totalGoalsFor,"homeGoalsAgainst":homeGoalsAgainst,
        "awayGoalsAgainst":awayGoalsAgainst,"totalGoalsAgainst":totalGoalsAgainst,"scoredPenaltiesPercentage":scoredPenaltiesPercentage,
        "scoredPenalties":scoredPenalties,"missedPenaltiesPercentage":missedPenaltiesPercentage,"missedPenalties":missedPenalties}
collection.insert_one(team)