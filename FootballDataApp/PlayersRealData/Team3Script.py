import pymongo
import requests
import json
import re

a, b = 'áãàéíóøöúüćčşÁÉÍÓÚÜ-', 'aaaeiooouuccsAEIOUU '
trans = str.maketrans(a, b)

teamId = 3
team = "Atletico Madrid"
id = 530
url = "https://api-football-v1.p.rapidapi.com/v3/players"

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
collection = db["PlayersRealData"]

pages = [1,2,3]

for i in pages:
    querystring = {"team": id, "season": "2021", "page": i}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "540a7d464amsh7e228715712a1aap1b0786jsnfd802be74253"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.text
    parse_json = json.loads(data)

    jsonResponse = parse_json['response']

    for j in range(len(jsonResponse)):
        playerId = jsonResponse[j]['player']['id']
        dateAux1 = jsonResponse[j]['player']['birth']['date']
        dateAux2 = dateAux1.split("-")
        date = dateAux2[2] + "/" + dateAux2[1] + "/" + dateAux2[0]
        nameAux1 = jsonResponse[j]['player']['name']
        firstnameAux = jsonResponse[j]['player']['firstname']
        lastnameAux = jsonResponse[j]['player']['lastname']
        fullnameAux = firstnameAux + " " + lastnameAux
        nameAux2 = str(nameAux1.translate(trans)).replace("\'", "")
        name = ""
        nameAux2pos1 = nameAux2.find(".")
        if nameAux2pos1 == -1:
            name = nameAux2
        else:
            name = str(nameAux2)[nameAux2pos1 + 2:len(nameAux2)]
        firstname = str(firstnameAux.translate(trans)).replace("\'", "")
        lastname = str(lastnameAux.translate(trans)).replace("\'", "")
        fullname = str(fullnameAux.translate(trans)).replace("\'", "")
        age = jsonResponse[j]['player']['age']
        nationality = jsonResponse[j]['player']['nationality']
        height = jsonResponse[j]['player']['height']
        weight = jsonResponse[j]['player']['weight']
        isInjured = jsonResponse[j]['player']['injured']
        if not isInjured:
            isInjured = 'No'
        else:
            isInjured = 'Yes'
        photo = jsonResponse[j]['player']['photo']
        statistics = jsonResponse[j]['statistics'][0]
        position = statistics['games']['position']
        rating = statistics['games']['rating']
        if rating is None:
            rating = 0
        totalShots = statistics['shots']['total']
        if totalShots is None:
            totalShots = 0
        shotsOn = statistics['shots']['on']
        if shotsOn is None:
            shotsOn = 0
        goals = statistics['goals']['total']
        if goals is None:
            goals = 0
        concededGoals = statistics['goals']['conceded']
        if concededGoals is None:
            concededGoals = 0
        assists = statistics['goals']['assists']
        if assists is None:
            assists = 0
        saves = statistics['goals']['saves']
        if saves is None:
            saves = 0
        passes = statistics['passes']['total']
        if passes is None:
            passes = 0
        keyPasses = statistics['passes']['key']
        if keyPasses is None:
            keyPasses = 0
        passesAccuracy = statistics['passes']['accuracy']
        if passesAccuracy is None:
            passesAccuracy = 0
        tackles = statistics['tackles']['total']
        if tackles is None:
            tackles = 0
        blocks = statistics['tackles']['blocks']
        if blocks is None:
            blocks = 0
        interceptions = statistics['tackles']['interceptions']
        if interceptions is None:
            interceptions = 0
        totalDuels = statistics['duels']['total']
        if totalDuels is None:
            totalDuels = 0
        duelsWon = statistics['duels']['won']
        if duelsWon is None:
            duelsWon = 0
        dribblesAttempts = statistics['dribbles']['attempts']
        if dribblesAttempts is None:
            dribblesAttempts = 0
        dribblesSuccess = statistics['dribbles']['success']
        if dribblesSuccess is None:
            dribblesSuccess = 0
        foulsDrawn = statistics['fouls']['drawn']
        if foulsDrawn is None:
            foulsDrawn = 0
        foulsCommitted = statistics['fouls']['committed']
        if foulsCommitted is None:
            foulsCommitted = 0
        yellowCards = statistics['cards']['yellow']
        if yellowCards is None:
            yellowCards = 0
        yellowredCards = statistics['cards']['yellowred']
        if yellowredCards is None:
            yellowredCards = 0
        redCards = statistics['cards']['red']
        if redCards is None:
            redCards = 0
        penaltiesWon = statistics['penalty']['won']
        if penaltiesWon is None:
            penaltiesWon = 0
        penaltiesCommited = statistics['penalty']['commited']
        if penaltiesCommited is None:
            penaltiesCommited = 0
        penaltiesScored = statistics['penalty']['scored']
        if penaltiesScored is None:
            penaltiesScored = 0
        penaltiesMissed = statistics['penalty']['missed']
        if penaltiesMissed is None:
            penaltiesMissed = 0
        penaltiesSaved = statistics['penalty']['saved']
        if penaltiesSaved is None:
            penaltiesSaved = 0
        playerUpdate = {"playerId": playerId, "firstname": firstname, "lastname": lastname, "date": date,
                        "fullname": fullname,
                        "age": age, "nationality": nationality,
                        "height": height, "weight": weight, "isInjured": isInjured,
                        "photo": photo, "position": position, "rating": rating, "totalShots": totalShots,
                        "shotsOn": shotsOn,
                        "goals": goals, "concededGoals": concededGoals, "assists": assists, "saves": saves,
                        "passes": passes,
                        "keyPasses": keyPasses, "passesAccuracy": passesAccuracy, "tackles": tackles, "blocks": blocks,
                        "interceptions": interceptions, "totalDuels": totalDuels, "duelsWon": duelsWon,
                        "dribblesAttempts": dribblesAttempts, "dribblesSuccess": dribblesSuccess,
                        "foulsDrawn": foulsDrawn,
                        "foulsCommitted": foulsCommitted, "yellowCards": yellowCards, "yellowredCards": yellowredCards,
                        "redCards": redCards, "penaltiesWon": penaltiesWon, "penaltiesSaved": penaltiesSaved,
                        "penaltiesMissed": penaltiesMissed, "penaltiesScored": penaltiesScored,
                        "penaltiesCommited": penaltiesCommited}
        query1 = collection.find_one(
            {"date": {"$regex": re.compile(date, re.IGNORECASE)}, "team": team, "teamId": teamId})
        if query1 != None:
            query1Filter = {"date": date,"team":team,"teamId":teamId}
            newvalues1 = {"$set": playerUpdate}
            collection.update_one(query1Filter, newvalues1)
            continue

        query2 = collection.find_one(
            {"name": {"$regex": re.compile(name, re.IGNORECASE)}, "team": team, "teamId": teamId})
        if query2 != None:
            query2Filter = {"name": {"$regex": re.compile(name, re.IGNORECASE)},"team":team,"teamId":teamId}
            newvalues2 = {"$set": playerUpdate}
            collection.update_one(query2Filter, newvalues2)
            continue

        query3 = collection.find_one(
            {"nickname": {"$regex": re.compile(name, re.IGNORECASE)}, "team": team, "teamId": teamId})
        if query3 != None:
            query3Filter = {"nickname": {"$regex": re.compile(name, re.IGNORECASE)},"team":team,"teamId":teamId}
            newvalues3 = {"$set": playerUpdate}
            collection.update_one(query3Filter, newvalues3)
            continue
