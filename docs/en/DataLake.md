_[Français](../../fr/DataLake)_

# Data Lake

Azure Data Lake is a set of capabilities dedicated to big data analytics, built on top of Azure Blob Storage, with enhanced performance, management, and security.

## Microsoft Documentation
- [Introduction to Azure Data Lake Storage Gen2](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction)

# Delta Lake

Delta Lake is an open-source storage layer that runs on top of an existing data lake, adding the capabilities of ACID (atomicity, consistency, isolation, durability) properties and transactions.

Delta Lake is fully compatible with Apache Spark, and supports all languages available in Databricks or Azure Synapse.

Azure Data Lake is _not_ ACID compliant, so Delta Lake should be used wherever data integrity and reliability are essential, or when there is a risk of bad data.


## How to Use Delta in Databricks
1. You first need to create a directory to store the delta log files, and keep note of the path to this directory.
2. Read in your data file, then write it to "delta" format and save it in the directory created above.
```
# read data file
testData = spark.read.format('json').options(header='true', inferSchema='true', multiline='true').load('/mnt/public-data/incoming/covid_tracking.json')

# write to delta format
testData.write.format("delta").mode("overwrite").save("/mnt/public-data/delta")
```
3. Create your SQL table using delta:
```
spark.sql("CREATE TABLE sample_table USING DELTA LOCATION '/mnt/public-data/delta/'")
```
4. Now you can run SQL queries on your delta table, including querying by version number or timestamp to "time travel" to previous versions of your data.
```
%sql
SELECT * FROM sample_table VERSION AS OF 0
```

## How to Use Delta in Azure Synapse

_Content goes here._


## How to Use Delta in Data Factory

_Write stuff here._

## Microsoft Documentation
- [What is Delta Lake](https://docs.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-what-is-delta-lake)
- [Delta Lake Quickstart (Databricks)](https://docs.microsoft.com/en-us/azure/databricks/delta/quick-start)
- [Work With Delta Lake (Synapse)](https://docs.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-delta-lake-overview?pivots=programming-language-python)
- [Delta Format in Azure Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/format-delta)



# Change Display Language
See [Language](Language.md) page to find out how to change the display language.