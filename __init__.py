from dotenv import load_dotenv
from database.seed_mongo import seed_database
import os

load_dotenv('.env')
mongo_url = f'mongodb://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}'
print(mongo_url)
db_name = os.getenv('DB_NAME')
collection_name = os.getenv('DB_COL_NAME')
seed_database(mongo_url, db_name, collection_name)

