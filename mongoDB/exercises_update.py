import pymongo
import os

db_host = os.getenv('MONGO_DB_CZECHITAS')
client = pymongo.MongoClient(db_host)

db_name = "andywaltlova"
databaze = client[db_name]

# 1. Expres na západ

# Načti z kolekce `hry` informace o hře Expres na západ, kterou jsi uložila v předchozím bloku cvičení.
# Doplň k této hře datum premiéry 2015-11-10.
# Ověř, že byla data správně uložena.


# 2. Oprava chyby

# U dat je často nutné kontrolovat jejich správnost. Například datum může být uvedeno v nesprávném formátu nebo může být zadaný den, který neexistuje.
# V kolekci je `goodreads` jedna kniha, která má jako datum vydání (`publication_date`) nastavenou podivnou hodnotu 6/31/1982, tedy 31. června 1986.
# Zjisti, o jakou knihu jde. Uprav hodnotu na "7/1/1982". Zkontroluj, že se hodnota správně uložila.



# 3. Změna názvu nakladatele

# Uvažuj, že se nakladatel (`publisher`) "Ballantine Books" přejmenoval na "Johnnie Walker Books".
# Uprav hodnotu pole `publisher` u všech knih, které mají jako nakladatele "Ballantine Books".
