from pyspark.conf import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession

from settings import DATA_FOLDER

SANITIZED_DATA_FILE_PATH = DATA_FOLDER / "sanitized_2014_Green_Taxi_Trip_Data.csv"


def transform_data(df, spark):
    """
        Structures data to store in Dynamo db
    :param df: Spark dataframe to be structured
    :return:
    """

    df.createOrReplaceTempView("dataframe")
    spark.sql("INSERT OVERWRITE TABLE temp SELECT * FROM df")
    return df


def write_df_to_dynamodb(df):
    """
        Write pyspark dataframe to dynamo db table
    :param df: pyspark df
    """
    pass


def read_csv(spark):
    """
        Reads sanitized csv into spark dataframe
    :return: spark dataframe
    """

    df = spark.read.csv(str(SANITIZED_DATA_FILE_PATH), header=True)

    return df


def configure_dd(sc):
    """
        Configure dynamo db
    :return:
    """
    conf = {
        "dynamodb.servicename": "dynamodb",
        "dynamodb.input.tableName": "users",
        "dynamodb.endpoint": "https://dynamodb.eu-central-1.amazonaws.com",
        "dynamodb.regionid": "eu-central-1",
        "mapred.output.format.class": "org.apache.hadoop.dynamodb.write.DynamoDBOutputFormat",
        "mapred.input.format.class": "org.apache.hadoop.dynamodb.read.DynamoDBInputFormat"
    }

    sc.hadoopRDD(
        inputFormatClass='org.apache.hadoop.dynamodb.read.DynamoDBInputFormat',
        keyClass='org.apache.hadoop.io.Text',
        valueClass='org.apache.hadoop.dynamodb.DynamoDBItemWritable',
        conf=conf
    )


if __name__ == '__main__':

    sc = SparkSession.builder.appName('dbb').getOrCreate()
    # configure_dd(sc)
    df = read_csv(sc)
    # df = transform_data(df, sc)
    write_df_to_dynamodb(df)
