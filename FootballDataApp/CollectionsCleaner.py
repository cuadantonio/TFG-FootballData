import pymongo

client = pymongo.MongoClient("mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
biwenger = db["BiwengerData"]
comunio = db["ComunioData"]
futmondo = db["FutmondoData"]
misterfantasy = db["MisterFantasyData"]
laligafantasy = db["LaLigaFantasyData"]
playersrealdata = db["PlayersRealData"]

biwenger.delete_many({})
comunio.delete_many({})
futmondo.delete_many({})
misterfantasy.delete_many({})
laligafantasy.delete_many({})
playersrealdata.delete_many({})