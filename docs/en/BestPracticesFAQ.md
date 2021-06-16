_[Français](../../fr/BestPracticesFAQ)_

# Best Practices FAQ

## What is the best file format to use for large data files?
Recommend using newer format like Parquet because....

## Do I need a SQL database?
In many cases a SQL database is not needed, data can be saved in files to the datalake.

## Do I need a SQL database when using Power BI?
No, you can load files locally into Power BI, you can also read files from Azure Storage. A database is only needed when you are using a more complex star-schema like system...

## When should we use a SQL database vs. Delta Lake?
Sabrina....

## How should we structure our projects data lake container? (1)
Bronze Silver Gold
Raw, Cleansed, Curated
https://medium.com/microsoftazure/building-your-data-lake-on-adls-gen2-3f196fc6b430
more links...

##  I get an out of memory exception in Databricks? (2)
(show screen shot)
The fastest and most expensive way to fix this is to increase the size of your cluster.
A more programmatic way to fix this would be to.... (use Spark, change file format, show examples with SQL, Python, R doing a simple query)...
Consider to use a subset of your data when doing queries (if possible)
Consider changing the file format to something like Parquet which uses less space than a traditional CSV file.

## How can i easily convert SAS code to Python or R?
Are there any tools they can use...

## How can i easily convert SAS files to another format? (3)
You can use SAS on network A to convert the files. Other tools? SAS library? Example code in a notebook, could upload a sas file to data lake and put example notbook in github repo
website with SAS files - Danielle
possible to make a .dbd with notebooks + files? Meddell
https://www.chicagobooth.edu/research/kilts/datasets/dominicks

## How do I validate that I am developing my application in the most cost effective way in the cloud using Microsoft technologies (CAE)?

take advantage of spark in databricks
make sure you cluster is running for the minimal amout of time
ensure your databricks cluster is correctly sized
delete data files that you are not using
try not to do processing on a cloud VM
ask for a review of your architecture
code review

## When should we use ADF vs. Databricks for data ingestion?
https://www.mssqltips.com/sqlservertip/6438/azure-data-factory-vs-ssis-vs-azure-databricks/

## When is a good time to use Azure Synapse vs. ADF and Databricks?

## How should data be structured if we plan to use Power BI?
https://docs.microsoft.com/en-us/power-bi/guidance/star-schema

## If we are using Power BI, do we need to use a SQL database?

##  How to read in an Excel file from Databricks? (6)
```python
%python
import pandas as pd
pd.read_excel("/dbfs/mnt/ccei-ccie-ext/Daily charts.xlsx", engine='openyxl')
```
Meddell Connor might have an example - make a DBF example or notebook

## How to convert files (CSV, text, JSON) to parquet using databricks?
https://sparkbyexamples.com/spark/spark-convert-csv-to-avro-parquet-json/

**Will have to write examples**

##  Which file types are best to use when? (4)
### Parquet  
It is good to use for very large datasets. It is also good to use if only a section of the dataset is needed which reads in the data in a faster rate.

AVRO -  Just as Parquet, it is great for very large datasets. To compare, it is better used for editing/writing into a dataset and for querying all columns in the dataset.

CSV - It is fine to use with marginally smaller datasets as CSV files do not load well when the file size is very large. But with smaller data sets, it is simple and human-readable.

Excel - try not to use :)

https://medium.com/ssense-tech/csv-vs-parquet-vs-avro-choosing-the-right-tool-for-the-right-job-79c9f56914a8
https://blog.clairvoyantsoft.com/big-data-file-formats-3fb659903271

###  Can I read Word document in Databricks? (5)


###  Can\How I convert Word document to a notebook?f (6)

**ADF - unzip file example **

I get an error message accessing data bricks (URL) error?

Web Scraping example: Databricks & Data Factory