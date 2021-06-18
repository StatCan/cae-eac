_[Français](../../fr/BestPracticesFAQ)_

# Best Practices FAQ

## What is the best file format to use for large data files?
Recommend using newer format like Parquet because it does save larger datesets in a smaller file in comparison to a CSV file. If only accessing certain sections of the dataset, it is also faster using Parquet as it uses columnar storage format.

## Do I need a SQL database?
In many cases a SQL database is not needed, data can be saved in files to the datalake.

## Do I need a SQL database when using Power BI?
It is not needed to have an SQL datbase when using Power BI. You are able to read files from the Azure Storage. A database is only needed when you are using a more complex star-schema like system. 

To connect to the internal data lake with Power BI desktop, please refer to this link:
https://statcan.github.io/cae-eac/en/FAQ/#how-do-i-connect-to-the-internal-data-lake-with-power-bi-desktop

## How should we structure our projects data lake container?
There are 3 parts in which to structure your data lake container:

### **Bronze/Raw Zone**
This zone stores the original format of any files or files/data that is immutable. The data contained in this zone is usually locked and are only accessible to certain members or is read-only. This zone is also organised in different folders per source system, with each ingestion process having a write access to only their associated folder.

(Check if needed to talk about storage costs and lifecycle management)

### **Silver/Cleansed Zone**
This zone is where parts of data removes unnecessary columns from the data, validates, standarizes and harmonises that data within this zone. This zone is mainly a folder per project. Any data that must be accessed within this zone is usually granted read-only access.

### **Gold/Curated Zone**
This zone is mainly for analytics rather than data ingestion or processing. The data in the curated zone is stored in star schemas. The dimensional modelling is usually done using Spark or Data Factory instead of inside the database engine. But if the dimensional modelling is done outside of the lake then it is best to publish the model back to the lake. This zone is best suited to run for large-scale queries and analysis that do not have strict time-sensitive reporting needs.

### **Laboratory Zone**
This zone is mainly for experimentation and exploration. It is used for prototype and innovation mixing both your own data sets with data sets from production. This zone is not a replacement for a development or test data lake which is required for more careful development. Each wil data lake project would have their own laboratory area via a folder. Permissions in this zone are typically read and write for each user/project.


https://medium.com/microsoftazure/building-your-data-lake-on-adls-gen2-3f196fc6b430
https://www.mssqltips.com/sqlservertip/6807/design-azure-data-lake-store-gen2/
more links...

##  I get an out of memory exception in Databricks?

### **Option 1:**
The fastest and most expensive way to fix this is to increase the size of your cluster.

To increase the size of the cluster, you must find the cluster you are using, select edit and increase the max amount of workers.
![ClusterEdit](images/BestPracticesClusterEdit.png)

### **Option 2:**
For a more programtic answer, if you are using pandas, it is also a suggestion to switch over and use pySpark instead. PySpark does run faster than pandas, it has better benefits from using data ingestion pipelines abd also works efficiently as it runs parallel on different nodes in a cluster.

https://www.analyticsvidhya.com/blog/2016/10/spark-dataframe-and-operations/

### **Option 3:**
Consider to use a subset of your data when doing queries if possible. If you are working with only a certain section of the dataset but are quering through all of it, it is possible to use just the subset. 

### **Option 4:**
Consider changing the file format to something like Parquet or Avro which uses less space than a traditional CSV file.

Conversion from CSV to Parquet:
```python
%python

testConvert = spark.read.format('csv').options(header='true', inferSchema='true').load('/mnt/public-data/incoming/titanic.csv')
testConvert.write.parquet("/mnt/public-data/incoming/testingFile")
```

Conversion from CSV to Avro:
```python
%python

diamonds = spark.read.format('csv').options(header='true', inferSchema='true').load('/mnt/public-data/incoming/titanic.csv')
diamonds.write.format("avro").save("/mnt/public-data/incoming/testingFile")
```

## How can i easily convert SAS code to Python or R?
It is not possible to easily convert SAS code to Python or R automatically, the only known way to convert is to manually do the conversion. 

## How do I validate that I am developing my application in the most cost effective way in the cloud using Microsoft technologies (CAE)?
There are plenty of ways to validate that your development is the most cost effective it can be:

1. Take advantage of Spark in databricks.

    a. Spark is a great addition to databricks that runs faster and better especially for large data sets. Using Spark would cost less because it does take less time to do its task.
2. Make sure you cluster is running for the minimal amout of time.

    a. If the cluster is no longer needed or not being use, ensure that it is not running and only run when it is needed.
3. Ensure your databricks cluster is correctly sized.

    a. Make sure that you have to correct amount of workers in your cluster, too many clusters results in a higher cost.
4. Delete data files that you are not using.

    a. Ensure that any files that are no longer needed or not in use anymore are deleted from the container.
    
5. Try not to do processing on a cloud VM.
    
6. Ask for a review of your architecture.

7. Code review.

## How should data be structured if we plan to use Power BI?
Data should be structured using the Star Schema.

For more details about using Star Schema, click the link below for details about using Star Schema and the benefits with Power BI: 

https://docs.microsoft.com/en-us/power-bi/guidance/star-schema

##  How to read in an Excel file from Databricks?
Here is an example of how to read an Excel file using Python:

```python
%python
import pandas as pd
pd.read_excel("/dbfs/mnt/ccei-ccie-ext/Daily charts.xlsx", engine='openyxl')
```

##  Which file types are best to use when?
### Parquet  
It is good to use for very large datasets. It is also good to use if only a section of the dataset is needed which reads in the data in a faster rate.

Read:

```python
%python
data = spark.read.parquet("/tmp/testParquet")
display(data)
```

Write:

```python
%python
//Assumption that a dataframe has been created already

data.write.parquet("/tmp/tempFile")
```

### Avro
Just as Parquet, it is great for very large datasets. To compare, it is better used for editing/writing into a dataset and for querying all columns in the dataset.

Read:

```python
data = spark.read.format("avro").load("/tmp/test_dataset")
display(data)
```

Write:

```scala
%scala
val ex = Seq((132, "baseball"),
    (148, "softball"),
    (172, "slow pitch")).toDF("players", "sport")
ex.write.format("avro").save("/tmp/testExample")
```

### CSV
It is fine to use with marginally smaller datasets as CSV files do not load well when the file size is very large. But with smaller data sets, it is simple and human-readable. For writing within a CSV file, it is also good to note that you are able to edit the file with Office. 

Read:

```python
%python
data = spark.read.format('csv').options(header='true', inferSchema='true').load('/tmp/test_dataCSV.csv')
display(data)
```

### Excel
It is discouraged to use Excel as much as possible as it is a bigger sized file compared to CSV and is also slower to use.

## How to convert files (CSV, Text, JSON) to parquet using databricks?
The rule of thumb in converting a file to parquet is to first read in the file and then write a new file into parquet

CSV to Parquet: 
```python
%python

testConvert = spark.read.format('csv').options(header='true', inferSchema='true').load('/mnt/public-data/incoming/titanic.csv')
testConvert.write.parquet("/mnt/public-data/incoming/testingFile")
```

JSON to Parquet:
```python
%python

testConvert = spark.read.json('tmp/test.json')
testConvert.write.parquet('tmp/testingJson')
```

Text to Parquet:
```python
%python

testConvert = spark.read.text("/mnt/public-data/incoming/testing.txt")
testConvert.write.parquet("/mnt/public-data/incoming/testingFile")
```

## Can I read Word document in Databricks?
It is best practice to read Word documents via Office instead.

---------------------------------------------------Currently Working On---------------------------------------------------------------------

## When should we use a SQL database vs. Delta Lake?
Sabrina....

## How can i easily convert SAS files to another format?
You can use SAS on network A to convert the files. Other tools? SAS library? Example code in a notebook, could upload a sas file to data lake and put example notbook in github repo
website with SAS files - Danielle
possible to make a .dbd with notebooks + files? Meddell
https://stattransfer.com/
https://www.chicagobooth.edu/research/kilts/datasets/dominicks
In databricks, it may be possible to convert the SAS file (xpt) to a csv file
```R
xpt = sasxport.get("xpt/DEMO.xpt")
write.csv(xpt, file="demo.csv")
```

## When should we use ADF vs. Databricks for data ingestion?


https://www.mssqltips.com/sqlservertip/6438/azure-data-factory-vs-ssis-vs-azure-databricks/

## When is a good time to use Azure Synapse vs. ADF and Databricks?

###  Can\How I convert Word document to a notebook?

**ADF - unzip file example **

Web Scraping example: Databricks & Data Factory

## When to use Spark Dataframe or Spark Table?

(Ask Hubert)

## How to create Spark Table? Examples in R, Python, Scala SQL?

## What is the best way to get data files into Azure ML?
