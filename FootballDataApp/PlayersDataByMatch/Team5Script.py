import pymongo
import requests
import json
import re

a, b = 'áãàéíóøöúüćčşšÁÉÍÓÚÜ-', 'aaaeiooouuccssAEIOUU '
trans = str.maketrans(a, b)

teamId = 5
team = "Real Betis"
id = 543
localFixturesIds = []
awayFixturesIds = []

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
byMatch = db["PlayersDataByMatch"]
matches = db["TeamsMatches"]
playersRealData = db['PlayersRealData']

localFixtures = matches.find({"homeTeamId":543})
for fixture in localFixtures:
    localFixturesIds.append(fixture['fixtureId'])

awayFixtures = matches.find({"awayTeamId":543})
for fixture in awayFixtures:
    awayFixturesIds.append(fixture['fixtureId'])

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

for localFixtureId in localFixturesIds:
    querystring = {"id": localFixtureId}

    headers = {
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "7f1b7f02e4msh6f4cc603145fa9ap11c86ajsn8b65db684d74"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    parse_json = json.loads(data)
    jsonResponse = parse_json['response'][0]
    round = int(str(jsonResponse['league']['round']).split(" ")[3])
    players = jsonResponse['players'][0]['players']
    for player in players:
        playerId = player['player']['id']
        query = playersRealData.find_one({"playerId":playerId,"teamId":teamId})
        if query == None:
            continue
        playerName = player['player']['name']
        playerPhoto = player['player']['photo']
        playerStats = player['statistics'][0]
        minutes = playerStats['games']['minutes']
        if minutes == None:
            minutes = 0
        offsides = playerStats['offsides']
        if offsides == None:
            offsides = 0
        totalShots = playerStats['shots']['total']
        if totalShots == None:
            totalShots = 0
        shotsOn = playerStats['shots']['on']
        if shotsOn == None:
            shotsOn = 0
        totalGoals = playerStats['goals']['total']
        if totalGoals == None:
            totalGoals = 0
        concededGoals = playerStats['goals']['conceded']
        if concededGoals == None:
            concededGoals = 0
        assists = playerStats['goals']['assists']
        if assists == None:
            assists = 0
        saves = playerStats['goals']['saves']
        if saves == None:
            saves = 0
        totalPasses = playerStats['passes']['total']
        if totalPasses == None:
            totalPasses = 0
        keyPasses = playerStats['passes']['key']
        if keyPasses == None:
            keyPasses = 0
        passesAccuracy = playerStats['passes']['accuracy']
        if passesAccuracy == None:
            passesAccuracy = '0%'
        totalTackles = playerStats['tackles']['total']
        if totalTackles == None:
            totalTackles = 0
        blockTackles = playerStats['tackles']['blocks']
        if blockTackles == None:
            blockTackles = 0
        interceptionTackles = playerStats['tackles']['blocks']
        if interceptionTackles == None:
            interceptionTackles = 0
        totalDuels = playerStats['duels']['total']
        if totalDuels == None:
            totalDuels = 0
        duelsWon = playerStats['duels']['won']
        if duelsWon == None:
            duelsWon = 0
        dribblesAttempts = playerStats['dribbles']['attempts']
        if dribblesAttempts == None:
            dribblesAttempts = 0
        dribblesSuccess = playerStats['dribbles']['success']
        if dribblesSuccess == None:
            dribblesSuccess = 0
        dribblesPast = playerStats['dribbles']['past']
        if dribblesPast == None:
            dribblesPast = 0
        foulsDrawn = playerStats['fouls']['drawn']
        if foulsDrawn == None:
            foulsDrawn = 0
        foulsCommitted = playerStats['fouls']['committed']
        if foulsCommitted == None:
            foulsCommitted = 0
        yellowCards = playerStats['cards']['yellow']
        if yellowCards == None:
            yellowCards = 0
        redCards = playerStats['cards']['red']
        if redCards == None:
            redCards = 0
        penaltiesWon = playerStats['penalty']['won']
        if penaltiesWon == None:
            penaltiesWon = 0
        penaltiesCommitted = playerStats['penalty']['commited']
        if penaltiesCommitted == None:
            penaltiesCommitted = 0
        penaltiesScored = playerStats['penalty']['scored']
        if penaltiesScored == None:
            penaltiesScored = 0
        penaltiesMissed = playerStats['penalty']['missed']
        if penaltiesMissed == None:
            penaltiesMissed = 0
        penaltiesSaved = playerStats['penalty']['saved']
        if penaltiesSaved == None:
            penaltiesSaved = 0
        rivalTeam = jsonResponse["teams"]["away"]["name"]
        rivalTeamId = jsonResponse["teams"]["away"]["id"]
        winnerId = -1
        winnerLocal = jsonResponse["teams"]["home"]["winner"]
        winnerAway = jsonResponse["teams"]["away"]["winner"]
        if winnerLocal == True:
            winnerId = id
        elif winnerAway == True:
            winnerId = rivalTeamId
        homeGoals = str(jsonResponse['goals']['home'])
        awayGoals = str(jsonResponse['goals']['away'])
        score = homeGoals + '-' + awayGoals
        playerToAdd = {'fixtureId': localFixtureId, 'round': round, 'team': team, 'teamId': id, 'rivalTeam': rivalTeam,
                       'rivalTeamId': rivalTeamId, 'playerId': playerId, 'playerName': playerName,
                       'playerPhoto': playerPhoto, 'minutes': minutes,
                       'offsides': offsides, 'totalShots': totalShots, 'shotsOn': shotsOn, 'totalGoals': totalGoals,
                       'concededGoals': concededGoals,
                       'assists': assists, 'saves': saves, 'totalPasses': totalPasses, 'keyPasses': keyPasses,
                       'passesAccuracy': passesAccuracy,
                       'totalTackles': totalTackles, 'blockTackles': blockTackles,
                       'interceptionTackles': interceptionTackles, 'totalDuels': totalDuels,
                       'duelsWon': duelsWon, 'dribblesAttempts': dribblesAttempts, 'dribblesSuccess': dribblesSuccess,
                       'dribblesPast': dribblesPast,
                       'foulsDrawn': foulsDrawn, 'foulsCommitted': foulsCommitted, 'yellowCards': yellowCards,
                       'redCards': redCards, 'penaltiesWon': penaltiesWon,
                       'penaltiesCommitted': penaltiesCommitted, 'penaltiesScored': penaltiesScored,
                       'penaltiesMissed': penaltiesMissed, 'penaltiesSaved': penaltiesSaved, 'winnerId': winnerId, 'score': score
                       }
        query = byMatch.find_one({"fixtureId": localFixtureId, "playerId": playerId})
        if query == None:
            byMatch.insert_one(playerToAdd)
            continue
        else:
            update = {"$set": playerToAdd}
            byMatch.update_one(query, update)
            continue
for awayFixtureId in awayFixturesIds:
    querystring = {"id": awayFixtureId}

    headers = {
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "7f1b7f02e4msh6f4cc603145fa9ap11c86ajsn8b65db684d74"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    parse_json = json.loads(data)
    jsonResponse = parse_json['response'][0]
    round = int(str(jsonResponse['league']['round']).split(" ")[3])
    players = jsonResponse['players'][1]['players']
    for player in players:
        playerId = player['player']['id']
        query = playersRealData.find_one({"playerId": playerId, "teamId": teamId})
        if query == None:
            continue
        playerName = player['player']['name']
        playerPhoto = player['player']['photo']
        playerStats = player['statistics'][0]
        minutes = playerStats['games']['minutes']
        if minutes == None:
            minutes = 0
        offsides = playerStats['offsides']
        if offsides == None:
            offsides = 0
        totalShots = playerStats['shots']['total']
        if totalShots == None:
            totalShots = 0
        shotsOn = playerStats['shots']['on']
        if shotsOn == None:
            shotsOn = 0
        totalGoals = playerStats['goals']['total']
        if totalGoals == None:
            totalGoals = 0
        concededGoals = playerStats['goals']['conceded']
        if concededGoals == None:
            concededGoals = 0
        assists = playerStats['goals']['assists']
        if assists == None:
            assists = 0
        saves = playerStats['goals']['saves']
        if saves == None:
            saves = 0
        totalPasses = playerStats['passes']['total']
        if totalPasses == None:
            totalPasses = 0
        keyPasses = playerStats['passes']['key']
        if keyPasses == None:
            keyPasses = 0
        passesAccuracy = playerStats['passes']['accuracy']
        if passesAccuracy == None:
            passesAccuracy = '0%'
        totalTackles = playerStats['tackles']['total']
        if totalTackles == None:
            totalTackles = 0
        blockTackles = playerStats['tackles']['blocks']
        if blockTackles == None:
            blockTackles = 0
        interceptionTackles = playerStats['tackles']['blocks']
        if interceptionTackles == None:
            interceptionTackles = 0
        totalDuels = playerStats['duels']['total']
        if totalDuels == None:
            totalDuels = 0
        duelsWon = playerStats['duels']['won']
        if duelsWon == None:
            duelsWon = 0
        dribblesAttempts = playerStats['dribbles']['attempts']
        if dribblesAttempts == None:
            dribblesAttempts = 0
        dribblesSuccess = playerStats['dribbles']['success']
        if dribblesSuccess == None:
            dribblesSuccess = 0
        dribblesPast = playerStats['dribbles']['past']
        if dribblesPast == None:
            dribblesPast = 0
        foulsDrawn = playerStats['fouls']['drawn']
        if foulsDrawn == None:
            foulsDrawn = 0
        foulsCommitted = playerStats['fouls']['committed']
        if foulsCommitted == None:
            foulsCommitted = 0
        yellowCards = playerStats['cards']['yellow']
        if yellowCards == None:
            yellowCards = 0
        redCards = playerStats['cards']['red']
        if redCards == None:
            redCards = 0
        penaltiesWon = playerStats['penalty']['won']
        if penaltiesWon == None:
            penaltiesWon = 0
        penaltiesCommitted = playerStats['penalty']['commited']
        if penaltiesCommitted == None:
            penaltiesCommitted = 0
        penaltiesScored = playerStats['penalty']['scored']
        if penaltiesScored == None:
            penaltiesScored = 0
        penaltiesMissed = playerStats['penalty']['missed']
        if penaltiesMissed == None:
            penaltiesMissed = 0
        penaltiesSaved = playerStats['penalty']['saved']
        if penaltiesSaved == None:
            penaltiesSaved = 0
        rivalTeam = jsonResponse["teams"]["home"]["name"]
        rivalTeamId = jsonResponse["teams"]["home"]["id"]
        winnerId = -1
        winnerLocal = jsonResponse["teams"]["home"]["winner"]
        winnerAway = jsonResponse["teams"]["away"]["winner"]
        if winnerLocal == True:
            winnerId = rivalTeamId
        elif winnerAway == True:
            winnerId = id
        homeGoals = str(jsonResponse['goals']['home'])
        awayGoals = str(jsonResponse['goals']['away'])
        score = homeGoals + '-' + awayGoals
        playerToAdd = {'fixtureId': awayFixtureId, 'round': round, 'team': team, 'teamId': id, 'rivalTeam': rivalTeam,
                       'rivalTeamId': rivalTeamId, 'playerId': playerId, 'playerName': playerName,
                       'playerPhoto': playerPhoto, 'minutes': minutes,
                       'offsides': offsides, 'totalShots': totalShots, 'shotsOn': shotsOn, 'totalGoals': totalGoals,
                       'concededGoals': concededGoals,
                       'assists': assists, 'saves': saves, 'totalPasses': totalPasses, 'keyPasses': keyPasses,
                       'passesAccuracy': passesAccuracy,
                       'totalTackles': totalTackles, 'blockTackles': blockTackles,
                       'interceptionTackles': interceptionTackles, 'totalDuels': totalDuels,
                       'duelsWon': duelsWon, 'dribblesAttempts': dribblesAttempts, 'dribblesSuccess': dribblesSuccess,
                       'dribblesPast': dribblesPast,
                       'foulsDrawn': foulsDrawn, 'foulsCommitted': foulsCommitted, 'yellowCards': yellowCards,
                       'redCards': redCards, 'penaltiesWon': penaltiesWon,
                       'penaltiesCommitted': penaltiesCommitted, 'penaltiesScored': penaltiesScored,
                       'penaltiesMissed': penaltiesMissed, 'penaltiesSaved': penaltiesSaved, 'winnerId': winnerId, 'score': score
                       }
        query = byMatch.find_one({"fixtureId": awayFixtureId, "playerId": playerId})
        if query == None:
            byMatch.insert_one(playerToAdd)
            continue
        else:
            update = {"$set": playerToAdd}
            byMatch.update_one(query, update)
            continue