import pymongo
import matplotlib.pyplot as plt

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersRealData = db["PlayersRealData"]
players = playersRealData.find()

positionsDef = ["Attacker","Defender","Goalkeeper","Midfielder"]
positionsValues = [0,0,0,0]

nationalitiesDef = ["Albania","Algeria","Argentina","Austria","Belgium","Bosnia and Herzegovina","Brazil","Cameroon","Canada","Central African Republic","Chile","Colombia","Congo DR","Croatia","Côte d'Ivoire","Denmark","Dominican Republic","Ecuador","France","Georgia","Germany","Ghana","Guadeloupe","Guinea","Honduras","Italy","Japan","Korea Republic","Kosovo","Mali","Mexico","Montenegro","Morocco","Mozambique","Netherlands","Nigeria","North Macedonia","Norway","Paraguay","Peru","Poland","Portugal","Republic of Ireland","Senegal","Serbia","Slovakia","Slovenia","Spain","Sweden","Switzerland","Togo","Türkiye","USA","Ukraine","Uruguay","Venezuela","Zimbabwe"]
nationalitiesValues = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

agesDef = ["Less than 25","Between 25 and 35","More than 35"]
agesValues = [0,0,0]

for player in players:
    position = player["position"]
    indexPosition = positionsDef.index(position)
    positionsValues[indexPosition] = positionsValues[indexPosition] + 1

    nationality = player["nationality"]
    indexNationality = nationalitiesDef.index(nationality)
    nationalitiesValues[indexNationality] = nationalitiesValues[indexNationality] + 1

    age = player["age"]
    if age < 25:
        agesValues[0] = agesValues[0] + 1
    elif age >= 25 and age <= 35:
        agesValues[1] = agesValues[1] + 1
    elif age > 35:
        agesValues[2] = agesValues[2] + 1

print(positionsValues)
print(nationalitiesValues)
print(agesValues)

fig1, ax1 = plt.subplots()
ax1.bar(x = agesDef, height = agesValues)

fig2,ax2 = plt.subplots()
ax2.bar(x=positionsDef, height=positionsValues)

fig3,ax3 = plt.subplots()
ax3.barh(nationalitiesDef, width=nationalitiesValues)
plt.show()