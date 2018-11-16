from pyspark.conf import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession

from settings import DATA_FOLDER, SPARK_CONFIGURE_INPUT, DB_HOST, DB_NAME

SANITIZED_DATA_FILE_PATH = DATA_FOLDER / "sanitized_2014_Green_Taxi_Trip_Data.csv"
DB_TABLE = "taxi_info"


def transform_data(df):
    """
        Structures data to store in Dynamo db
    :param df: Spark dataframe to be structured
    :return:
    """
    return df


def write_df_to_mongodb(df):
    """
        Write pyspark dataframe to dynamo db table
    :param df: pyspark df
    """
    df.write.format("com.mongodb.spark.sql.DefaultSource").mode("append").save()


def read_csv(spark):
    """
        Reads sanitized csv into spark dataframe
    :return: spark dataframe
    """

    df = spark.read.csv(str(SANITIZED_DATA_FILE_PATH), header=True)

    return df


def configure_spark():
    """
        Configure dynamo db
    :return:
    """
    spark = SparkSession \
        .builder \
        .appName("myApp") \
        .config(SPARK_CONFIGURE_INPUT,
                "mongodb://{}/{}.{}".format(DB_HOST, DB_NAME, DB_TABLE)) \
        .getOrCreate()

    return spark


if __name__ == '__main__':

    spark = configure_spark()
    df = read_csv(spark)
    write_df_to_mongodb(spark)
