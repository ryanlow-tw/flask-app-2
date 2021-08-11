import os
from mongo_database.seed_mongo import seed_database
# mongo_url = f'mongodb://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/'
mongo_url = "mongodb://localhost:27017"
db_name = os.getenv('DB_NAME')
collection_name = os.getenv('DB_COL_NAME')
print(mongo_url)
collection = seed_database(mongo_url, db_name, collection_name)
