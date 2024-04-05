import pymongo
import json

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["books"]
collection = db["books_data"]


for doc in collection.find({'title': {'$regex': 'T'}}):
    print(doc)
# # Загрузка данных из JSON-файла в MongoDB
# def load_data_to_mongodb(filename='books.json'):
#     with open(filename, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         collection.insert_many(data)
#
# # Вызов функции для загрузки данных
# load_data_to_mongodb()
