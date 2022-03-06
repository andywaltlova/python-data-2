import pymongo
import os

db_host = os.getenv('MONGO_DB_CZECHITAS')
client = pymongo.MongoClient(db_host)

db_name = "andywaltlova"
databaze = client[db_name]

## Expres na západ

# Načti z kolekce `hry` informace o hře Expres na západ, kterou jsi uložila v předchozím bloku cvičení.
# Doplň k této hře datum premiéry 2015-11-10.
# Ověř, že byla data správně uložena.


kolekce = databaze["hry"]

# hra = {
#     "Představení": "Expres na západ",
#     "Délka v minutách": 120,
#     "Premiéra": "2019-11-13"
# }
# kolekce.insert_one(hra)

# dotaz = { "Představení": "Expres na západ" }

# nove_hodnoty = { "$set": { "Premiéra": "2015-11-10", 'Derniéra': '2019-11-13'} }
# kolekce.update_one(dotaz, nove_hodnoty)

# vysledek = kolekce.find_one(dotaz)
# print(vysledek)


## Oprava chyby

# U dat je často nutné kontrolovat jejich správnost. Například datum může být uvedeno v nesprávném formátu nebo může být zadaný den, který neexistuje.
# V kolekci je `goodreads` jedna kniha, která má jako datum vydání (`publication_date`) nastavenou podivnou hodnotu 6/31/1982, tedy 31. června 1986.
# Zjisti, o jakou knihu jde. Uprav hodnotu na "7/1/1982". Zkontroluj, že se hodnota správně uložila.


# kolekce = databaze["goodreads"]

# dotaz = { "publication_date": "6/31/1982" }
# nove_hodnoty = { "$set": { "publication_date": "7/1/1982" } }
# kolekce.update_one(dotaz, nove_hodnoty)

# vysledek = kolekce.find_one(dotaz)
# print(vysledek)

# dotaz = { "publication_date":  "7/1/1982" }
# vysledek = kolekce.find_one(dotaz)
# print(vysledek)


## Změna názvu nakladatele

# Uvažuj, že se nakladatel (`publisher`) "Ballantine Books" přejmenoval na "Johnnie Walker Books".
# Uprav hodnotu pole `publisher` u všech knih, které mají jako nakladatele "Ballantine Books".


kolekce = databaze["goodreads"]

dotaz = { "publisher": "Ballantine Books" }
nove_hodnoty = { "$set": { "publisher": "Johnnie Walker Books" } }
kolekce.update_many(dotaz, nove_hodnoty)

dotaz = { "publisher": "Johnnie Walker Books" }
vysledek = kolekce.find(dotaz)
# print(kolekce.count_documents(dotaz))
for dokument in vysledek:
    print(dokument['publisher'])