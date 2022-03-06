import pymongo
import os

db_host = os.getenv('MONGO_DB_CZECHITAS')
client = pymongo.MongoClient(db_host)
db_name = "andywaltlova"
db = client[db_name]


kolekce = db["goodreads"]

# 1. Z předem připravené kolekce goodreads, která obsahuje knihy a jejich hodnocení na webu Goodreads.com, načti první dostupný dokument pomocí funkce find_one().
# vysledek = kolekce.find_one()
# print(vysledek)

# 2. Najdi knihu, jejíž ISBN (isbn) je 038551641X.
# dotaz = {"isbn": "038551641X"}
# vysledek = kolekce.find_one(dotaz)
# print(vysledek)

# 3. Napiš dotaz na knihy, jejichž autorem (authors) je spisovatel “Robert Graves”. Načti všechny knihy dle daného dotazu a vypiš informace o nich na obrazovku.
# dotaz = {"authors": "Robert Graves"}
# vysledek = kolekce.find(dotaz)

# for dokument in vysledek:
#     print(dokument)

# 4. U knih, které napsal Robert Graves, vypiš pouze název a hodnocení (average_rating).
# for dokument in vysledek:
#     print(dokument["title"], dokument["average_rating"])

# 5. Vypiš informace o všech knihách, které získaly více než 2 milion hodnocení (ratings_count). Kolik takových knih je?
# dotaz = {"ratings_count": {"$gt": 2_000_000}}
# vysledek = kolekce.find(dotaz)
# for dokument in vysledek:
#     print(dokument)
# print(kolekce.count_documents(dotaz))

# 6. Vypiš informace o všech knihách, které alespoň 40 000 textových hodnocení (text_reviews_count) a současně mají průměrné hodnocení větší než 4.
# dotaz = {
#     "text_reviews_count": {"$gt": 40_000},
#     "average_rating": {"$gt": 4}
# }

# vysledek = kolekce.find(dotaz)
# for dokument in vysledek:
#     print(dokument['average_rating'], dokument['text_reviews_count'])

# 7. Vypiš informace o všech knihách, jejímiž autory jsou Jared Diamond nebo Joseph A. Tainter (zde využij operátor in).
dotaz = {"authors": {"$in": ["Jared Diamond", "Joseph A. Tainter"]}}
vysledek = kolekce.find(dotaz)

for dokument in vysledek:
    print(dokument)

# Všimni si, v jakém formátu je zadané datum vydání (publication_date). Jde o americký formát, který má ze záhadných důvodů na prvním místě měsíc a na druhém den.
