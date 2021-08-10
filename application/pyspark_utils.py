from application import spark_dataframe
from pyspark.sql import functions as f
import ast


class PySparkFilter:
    spark_df = spark_dataframe
    average_rating = spark_df.select(f.avg("average_rating")).collect()[0][0]
    average_rating_2dp = float(f"{average_rating:.2f}")

    @staticmethod
    def get_average_rating():
        return {"mean": PySparkFilter.average_rating_2dp}

    @staticmethod
    def get_book_ratings(query_strings):

        ratings_functions = {
            "average": PySparkFilter.get_average_rating,
            "highly-rated": PySparkFilter.get_high_ratings,
            "less-rated": PySparkFilter.get_low_ratings
        }

        query_string_ratings = query_strings["param"]

        if query_string_ratings not in ratings_functions:
            return {}

        return ratings_functions[query_string_ratings]()

    @staticmethod
    def get_high_ratings():
        results = spark_dataframe.filter(
            spark_dataframe["average_rating"] >= PySparkFilter.average_rating
        ).toJSON().collect()
        return {"highly-rated": [ast.literal_eval(row) for row in results]}

    @staticmethod
    def get_low_ratings():
        results = spark_dataframe.filter(
            spark_dataframe["average_rating"] < PySparkFilter.average_rating
        ).toJSON().collect()
        return {"less-rated": [ast.literal_eval(row) for row in results]}
