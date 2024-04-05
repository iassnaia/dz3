from clickhouse_driver import Client
from mongoDB_01 import collection

# Подключение к ClickHouse
clickhouse_client = Client(host='localhost', port=9000, database='books')

# Создание таблицы для хранения данных
clickhouse_client.execute('''
    CREATE TABLE IF NOT EXISTS books_data (
        id UUID DEFAULT generateUUID(),
        title String,
        price Float64,
        stock String,
        description String
    ) ENGINE = MergeTree()
    ORDER BY id
''')


# Загрузка данных из MongoDB и вставка их в ClickHouse
def load_data_to_clickhouse():
    books_data = collection.find({}, {'_id': 0})
    for book in books_data:
        clickhouse_client.execute('''
            INSERT INTO books_data (title, price, stock, description) VALUES
            (%(title)s, %(price)s, %(stock)s, %(description)s)
        ''', book)


# Вызов функции для загрузки данных
load_data_to_clickhouse()
clickhouse_client.book
