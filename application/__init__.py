import os

from flask import Flask
from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv('.env')
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
spark = SparkSession.builder.appName("books3000").getOrCreate()
spark_dataframe = spark.read.parquet(os.getenv("BOOKS_3000_PATH"))

import application.routes
