import pymongo

db_host = os.getenv('MONGO_DB_CZECHITAS')
client = pymongo.MongoClient(db_host)
db_name = "andywaltlova"
databaze = client[db_name]

# 1. Každý má svou pravdu
# Vložení dvou her

kolekce = databaze["hry"]
play_1 = {
    "Představení": "Modrovous",
    "Délka v minutách": 70,
    "Premiéra": "2018-12-15"
}
play_2 = {
    "Představení": "Každý má svou pravdu",
    "Délka v minutách": None,
    "Premiéra": "2020-02-08"
}
hra_3 = {
    "Představení": "Expres na západ",
    "Délka v minutách": 120,
    "Premiéra": "2019-11-13"
}

# Vlozeni po jednom
play_1_id = kolekce.insert_one(play_1)
play_2_id = kolekce.insert_one(play_2)
play_3_id = kolekce.insert_one(hra_3)


print(play_1_id.inserted_id)

# Vlozeni for cyklem
# plays = [play_1, play_2]
# for play in plays:
#     inserted = kolekce.insert_one(play)
#     print(inserted.inserted_id)

# Vlozeni pomoci insert_many
# kolekce.insert_many([play_1, play_2])

print('Inserted: ')
documents = kolekce.find()
for record in documents:
    print(record.get('Délka v minutách', 'Delka neexistuje'))

####################################################
# print('After delete: ')

kolekce.delete_many({'Představení': 'Modrovous'})
kolekce.delete_many({'Představení': 'Každý má svou pravdu'})

# documents = kolekce.find()
# for record in documents:
#     print(record)

# 2. Knihovna

kolekce = databaze["knihy"]

knihy = [
    {
        "Název": "Smrt bere jackpot",
        "Autor": "Vincent McEveety",
        "Počet stran": 542
    },
    {
        "Název": "Zaklínač I. - Poslední přání",
        "Autor": "Andrzej Sapkowski",
        "Počet povídek": 8,
        "Počet stran": 274,
    }
]

# kolekce.insert_many(knihy)
# documents = kolekce.find()
# for record in documents:
#     print(record)





