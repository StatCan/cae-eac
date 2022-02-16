# Collaborative Analytics Environment

## Data Storage

|Scenario  |Best Choice  |Other Choices  |
|---------|---------|---------|
|Relational data from SQL Server or mysql <br> Total size less than 4 TB with largest fact table < 60 millions   |   Azure SQL Database      |    Synapse SQL Pools or Data Lake (Parquet)    |
|Binary Files (images or similar)     |    Azure Data Lake     |         |
|Relational Data with lots of GeoSpatial queries <br> Requires builtin GeoSpatial functions <br> Less than 4TB and largest table < 60 million records      |   Azure Database for PostgreSQL      |         |
|Tabular files (CSV, Parquet...) to be used in ML training    |   Azure Data Lake      |    Azure SQL Database     |
|SQL Data warehouse <br> >10TB Storage with fact tables > 100 million records     |    Synapse SQL Pools     |         |

## Notebooks

|Scenario  |Best Choice  |Other Choices  |
|---------|---------|---------|
|Data manipulation using python with Pandas <br> Migrating from individual-machine-experience <br> Dataset < 10 GB (per dataframe)    |   Azure Machine Learning      |         |
|Must use Jupyter notebooks or Jupyter lab <br> Need access to the terminal of the VM     |    Azure Machine Learning     |         |
|Large dataset <br> Using Pyspark <br> Performance is the biggest concern <br> No dependancy on SQL Pools in Synapse    |    Azure Databricks     |     Azure Synapse Spark    |
|Use R on Spark     |    Azure Databricks     |         |
|Need to use Spark on single machine cluster     |    Azure Databricks     |         |
|Use .NET for Spark     |    Azure Synapse Spark     |         |
|Project that has SQL Pools, Pipelines and Spark <br> Prefer one UI     |    Azure Synapse Spark      |         |

## Data movement

|Scenario  |Best Choice  |Other Choices  |
|---------|---------|---------|
|Prefer no code or low code. Use relational database     |    Data Factory       |    Synapse Pipelines    |
|Prefer no code or low code. Use data lake     |    Synapse Pipelines     |    Data Factory      |
|Prefer Python, R     |    Azure Databricks     |         |
|Prefer SQL     |    Synapse Serverlerss SQL Pools      |         |



## UI apps

|Scenario  |Best Choice  |Other Choices  |
|---------|---------|---------|
|Desktop software (SQL Server Management Studio, VSCode, SAS Desktop)    |   Virtual Machines  / Azure Virtual Desktop    |         |
| R-Shiny Apps     | Azure Machine Learning compute + App service | Azure Databricks |




