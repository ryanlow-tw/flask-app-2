from application import spark_dataframe
from pyspark.sql import functions as f


class PySparkFilter:

    spark_df = spark_dataframe
    average_rating = spark_df.select(f.avg("average_rating")).collect()[0][0]
    average_rating_2sf = float(f"{average_rating:.2f}")

    @staticmethod
    def get_average_rating():
        return {"mean": PySparkFilter.average_rating_2sf}


