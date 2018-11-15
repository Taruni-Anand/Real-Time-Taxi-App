from pyspark.shell import sqlContext
from pyspark.sql import SparkSession
from pyspark import SparkContext

from settings import DATA_FOLDER

SANITIZED_DATA_FILE_PATH = DATA_FOLDER / "sanitized_2014_Green_Taxi_Trip_Data.csv"


def structure_data(df):
    """
        Structures data to store in Dynamo db
    :param df: Spark dataframe to be structured
    :return:
    """
    return df


def write_df_to_dynamodb(df):
    """
        Write pyspark dataframe to dynamo db table
    :param df: pyspark df
    """
    pass


def read_csv():
    """
        Reads sanitized csv into spark dataframe
    :return: spark dataframe
    """

    df = sqlContext.read.format('csv')\
        .options(header='true', inferSchema='true')\
        .load(SANITIZED_DATA_FILE_PATH)

    return df


if __name__ == '__main__':
    df = read_csv()
    df = structure_data(df)
    write_df_to_dynamodb(df)
