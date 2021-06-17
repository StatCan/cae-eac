_[Français](../../fr/DataLake)_

# Data Lake

Azure Data Lake is a set of capabilities dedicated to big data analytics, built on top of Azure Blob Storage, with enhanced performance, management, and security.

## Microsoft Documentation
- [Introduction to Azure Data Lake Storage Gen2](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction)

# Delta Lake

Delta Lake is an open-source storage layer that runs on top of an existing data lake, adding the capabilities of ACID (atomicity, consistency, isolation, durability) properties and transactions. Delta Lake is fully compatible with Apache Spark.

Azure Data Lake is _not_ ACID compliant, so Delta Lake should be used wherever data integrity and reliability are essential, or when there is a risk of bad data.

A delta lake is basically a folder inside the data lake containing a log file and data files (stored in parquet format) for each version of a table. As long as the log and data files exist, you can use the time travel feature to query previous versions of a delta table, and view the history of that table.

Delta works at the table level, so multi-table queries and joins are not supported.

## Time Travel

You can use time travel to query an older snapshot of a table, either by version number or timestamp. By default, data files are stored for 30 days.

Example:

**SQL**
```
SELECT * FROM example_table TIMESTAMP AS OF '2018-10-18T22:15:12.013Z'
SELECT * FROM delta.`/delta/example_table` VERSION AS OF 12
```

**Python**
```
df1 = spark.read.format("delta").option("timestampAsOf", 2020-03-13).load("/delta/example_table")
df2 = spark.read.format("delta").option("timestampAsOf", 2019-01-01T00:00:00.000Z).load("/delta/example_table")
df3 = spark.read.format("delta").option("versionAsOf", version).load("/delta/example_table")
```

To remove old data files (not log files) that are no longer referenced by a delta table, you can run the **vacuum** command.

Example:

**SQL**
```
VACUUM example_table   -- vacuum files not required by versions older than the default retention period

VACUUM '/data/example_table' -- vacuum files in path-based table

VACUUM delta.`/data/example_table/`

VACUUM delta.`/data/example_table/` RETAIN 100 HOURS  -- vacuum files not required by versions more than 100 hours old

VACUUM example_table DRY RUN    -- do dry run to get the list of files to be deleted
```

**Python**
```
from delta.tables import *

deltaTable = DeltaTable.forPath(spark, pathToTable)

deltaTable.vacuum()        # vacuum files not required by versions older than the default retention period

deltaTable.vacuum(100)     # vacuum files not required by versions more than 100 hours old
```

**Scala**
```
import io.delta.tables._

val deltaTable = DeltaTable.forPath(spark, pathToTable)

deltaTable.vacuum()        // vacuum files not required by versions older than the default retention period

deltaTable.vacuum(100)     // vacuum files not required by versions more than 100 hours old
```

### Official Documentation
- [Query an older snapshot of a table (time travel)](https://docs.delta.io/latest/delta-batch.html#-deltatimetravel)
- [Remove files no longer referenced by a delta table](https://docs.delta.io/latest/delta-utility.html#-delta-vacuum)

## Using Delta in Databricks

Databricks has native support for Delta Lake, and can run queries using Python, R, Scala, and SQL.

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

### Microsoft Documentation
- [Delta Lake Quickstart](https://docs.microsoft.com/en-us/azure/databricks/delta/quick-start)

## Using Delta in Azure Synapse

Delta Lake is compatible with Azure Synapse. Delta tables can be created and queried within Synapse notebooks similarly to Databricks, with language support for PySpark, Scala, and .NET (C#). Note that SQL is *not* supported with the current version.

1. Read in your data file.
```
data = spark.read.format('csv').options(header='true', inferSchema='true', multiline='true').load('abfss://public-data@statsconviddsinternal.dfs.core.windows.net/incoming/data_duplicate.csv')
```
2. Write to delta format and save to your delta table directory.
```
data.write.format("delta").save(delta_table_path)
```
3. Create your SQL table using delta:
```
spark.sql("CREATE TABLE example USING DELTA LOCATION '{0}'".format(delta_table_path))
```
4. Now you can run queries on your data.

### Microsoft Documentation
- [Work With Delta Lake](https://docs.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-delta-lake-overview?pivots=programming-language-python)

## Using Delta in Data Factory

You can use Azure Data Factory to copy data to and from a delta lake stored in Azure Data Lake.

### Example: Copy Data to Delta Lake
1. Create a new dataflow and add a source.
2. Under the **Source Settings** tab, add the dataset that you want to copy from. Configure any other relevant settings.
3. Click the plus button to the right of your source and add a sink.
4. Under the **Sink** tab, choose **Inline** as the Sink type, and **Delta** as the Inline dataset type.
5. Under the **Settings** tab, set the **folder path** (the path to where your delta files will be stored).

### Microsoft Documentation
- [Delta Format in Azure Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/format-delta)

## Power BI

_TO DO: How does delta lake work in Power BI?_

## Microsoft Documentation
- [What is Delta Lake](https://docs.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-what-is-delta-lake)
- [Delta Lake on Azure](https://techcommunity.microsoft.com/t5/analytics-on-azure/delta-lake-on-azure/ba-p/1869746)




# Change Display Language
See [Language](Language.md) page to find out how to change the display language.