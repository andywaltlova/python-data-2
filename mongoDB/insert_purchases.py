import pymongo
import os

db_host = os.getenv('MONGO_DB_CZECHITAS')
client = pymongo.MongoClient(db_host)

db_name = "andywaltlova"
databaze = client[db_name]

kolekce = databaze["nakupy"]

purchases = [
    {
        "Jméno": "Petr",
        "Věc": "Toaletní papír",
        "Částka v korunách": 65,
        "Počet rolí": 6,
    },
    {
        "Jméno": "Libor",
        "Věc": "Pivo na kolaudačku",
        "Částka v korunách": 124,
        "Vratná záloha": 20,
        "Datum": "2020-03-01",
        "Poznámka": "Vrátit otvírák sousedům",
    },
    {
        "Jméno": "Petr",
        "Věc": "Pytel na odpadky",
        "Částka v korunách": 75,
        "Objem pytle": 10,
        "Upozornění": "Příště koupit větší!!!",
    },
    {
        "Jméno": "Míša",
        "Věc": "Utěrky na nádobí",
        "Částka v korunách": 130,
        "Barva": "modrá",
        "Počet kusů v balení": 10,
    },
    {
        "Jméno": "Ondra",
        "Věc": "Toaletní papír",
        "Částka v korunách": 120,
        "Počet rolí": 15,
        "Běžná cena": 150,
    },
    {
        "Jméno": "Míša",
        "Věc": "Pečící papír",
        "Částka v korunách": 30,
        "Místo nákupu": "Albert",
        "Délka v metrech": 30,
        "Poznámka": "Peče celá země",
    },
    {
        "Jméno": "Zuzka",
        "Věc": "Savo",
        "Částka v korunách": 80,
        "Poznámka": "Dokoupit rukavice",
    },
    {
        "Jméno": "Pavla",
        "Věc": "Máslo",
        "Částka v korunách": 50,
        "Datum trvanlivosti": "2020-05-01",
    },
    {
        "Jméno": "Ondra",
        "Věc": "Káva",
        "Částka v korunách": 300,
        "Počet kusů": 2,
        "Značka": "Davidoff",
        "Poznámka": "Nejvíc vypila Míša",
    },
]

# kolekce.insert_many(purchases)

# results = collection.find()
# for record in results:
#     print(record)

kolekce = databaze["nakupy"]
dotaz = {"Částka v korunách": {"$gt": 100}}
vysledek = kolekce.find(dotaz)

for dokument in vysledek:
    print(dokument)