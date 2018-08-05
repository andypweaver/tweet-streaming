from pyspark.sql import SparkSession


class SparkStream():

    def __init__(self):
        self.spark = SparkSession.builder.master("local")\
            .appName("twit-stream").getOrCreate()
        self.spark.sparkContext.setLogLevel('INFO')

    def start_stream(self):
        print('todo')
