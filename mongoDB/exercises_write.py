import pymongo

db_host = os.getenv('MONGO_DB_CZECHITAS')
client = pymongo.MongoClient(db_host)
db_name = "andywaltlova"
databaze = client[db_name]

# 1. Každý má svou pravdu
# Uvažujme data o dvou divadelních hrách, která jsou v následující tabulce.

# Představení	            Délka v minutách	Premiéra	Derniéra
# Modrovous	                              70	2018-12-15
# Každý má svou pravdu		                    2020-02-08
# Expres na západ	120		                                2019-11-13

# Splň následující úkoly.
# Přepiš tato data to dvou slovníků. Pokud nějaký sloupec nemá hodnotu, vynech ho.
# Vlož jednotlivé slovníky postupně do své databáze do kolekce hry.
# Nech si na obrazovku vypsat ID alespoň jednoho vloženého dokumentu.

hry = []


# 2. Knihovna
# Níže jsou informace o třech různých knihách.

# První kniha:
# Název: Smrt bere jackpot
# Autor: Vincent McEveety
# Počet stran: 542

# Druhá kniha:
# Název: Zaklínač I. - Poslední přání
# Autor: Andrzej Sapkowski
# Počet povídek: 8
# Počet stran: 274
# Přepiš informace do slovníků a tyto slovníky vlož do jednoho seznamu. Tento seznam pak vlož najednou do kolekce knihy funkcí insert_many().

kolekce = databaze["knihy"]

knihy = []





