import pymongo

client = pymongo.MongoClient("mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
biwenger = db["BiwengerData"]
playersrealdata = db["PlayersRealData"]
teamsmatches = db["TeamsMatches"]
teamsdatabymatch = db["TeamsDataByMatch"]
playersdatabymatch = db["PlayersDataByMatch"]
teamsdata = db["TeamsData"]

biwenger.delete_many({})
playersrealdata.delete_many({})
teamsmatches.delete_many({})
teamsdatabymatch.delete_many({})
playersdatabymatch.delete_many({})
teamsdata.delete_many({})
