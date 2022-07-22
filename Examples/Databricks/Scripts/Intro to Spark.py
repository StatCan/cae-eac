# Databricks notebook source
# MAGIC %md
# MAGIC # Intro to Apache Spark
# MAGIC Note: This notebook was found in the Databrick tech-talks Github repository (https://www.github.com/databricks/tech-talks). In the repository you can find many other great notebooks that can help you learn certain topics within Databricks.
# MAGIC <br/>
# MAGIC <br/>
# MAGIC * [Intro to Spark slides](https://github.com/databricks/tech-talks/blob/master/2020-04-29%20%7C%20Intro%20to%20Apache%20Spark/Intro%20to%20Spark.pdf)
# MAGIC * What is a Spark DataFrame?
# MAGIC   * Read in the [NYT data set](https://github.com/nytimes/covid-19-data) 
# MAGIC * How to perform a distributed count?
# MAGIC * Transformations vs. Actions
# MAGIC * Spark SQL
# MAGIC 
# MAGIC [Spark docs](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html)

# COMMAND ----------

# MAGIC %fs ls mnt/bdl-lde/examples/intro_to_spark/

# COMMAND ----------

# MAGIC %md
# MAGIC ## How do we represent this data?

# COMMAND ----------

# MAGIC %md
# MAGIC ![Unified Engine](https://files.training.databricks.com/images/105/unified-engine.png)
# MAGIC 
# MAGIC 
# MAGIC ####At first there were RDDs...
# MAGIC * **R**esilient: Fault-tolerant
# MAGIC * **D**istributed: Across multiple nodes
# MAGIC * **D**ataset: Collection of partitioned data
# MAGIC 
# MAGIC RDDs are immutable once created and keep track of their lineage to enable failure recovery.
# MAGIC 
# MAGIC ####... and then there were DataFrames
# MAGIC * Higher-level APIs
# MAGIC * User friendly
# MAGIC * Optimizations and performance improvements
# MAGIC 
# MAGIC ![RDD vs DataFrames](https://files.training.databricks.com/images/105/rdd-vs-dataframes.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Create a DataFrame from the NYT COVID data

# COMMAND ----------

covid_df = spark.read.csv("dbfs:/mnt/bdl-lde/examples/intro_to_spark/us-counties.csv")
covid_df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Let's look at the [Spark docs](https://spark.apache.org/docs/latest/index.html) to see what options we have to pass into the csv reader.

# COMMAND ----------

covid_df = spark.read.csv("dbfs:/mnt/bdl-lde/examples/intro_to_spark/us-counties.csv", header=True, inferSchema=True)
covid_df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ###How many records do we have?
# MAGIC * Instead of counting M&Ms, let's count the number of rows in the DataFrame
# MAGIC 
# MAGIC ###What do we expect our Spark job to look like?
# MAGIC * How many stages?

# COMMAND ----------

covid_df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Let's write some Spark code!
# MAGIC 
# MAGIC * I want to look at only the information for the county I live in (Los Angeles)
# MAGIC * I want the most recent information at the top

# COMMAND ----------

(covid_df
 .sort(covid_df["date"].desc()) 
 .filter(covid_df["county"] == "Los Angeles")) 

# COMMAND ----------

# MAGIC %md
# MAGIC **...nothing happened. Why?**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Transformations vs Actions
# MAGIC 
# MAGIC There are two types of operations in Spark: transformations and actions.
# MAGIC 
# MAGIC Fundamental to Apache Spark are the notions that
# MAGIC * Transformations are **LAZY**
# MAGIC * Actions are **EAGER**

# COMMAND ----------

# same operations as above
(covid_df
 .sort(covid_df["date"].desc()) 
 .filter(covid_df["county"] == "Los Angeles")) 

# COMMAND ----------

# MAGIC %md
# MAGIC Why isn't is showing me results? **Sort** and **filter** are `transformations`, which are lazily evaluated in Spark.
# MAGIC 
# MAGIC Laziness has a number of benefits
# MAGIC * Not forced to load all data in the first step
# MAGIC   * Technically impossible with **REALLY** large datasets.
# MAGIC * Easier to parallelize operations 
# MAGIC   * N different transformations can be processed on a single data element, on a single thread, on a single machine. 
# MAGIC * Most importantly, it allows the framework to automatically apply various optimizations
# MAGIC   * This is also why we use Dataframes!
# MAGIC   
# MAGIC There's a lot Spark's **Catalyst** optimizer can do. Let's focus on only this situation. For more information, read [this blog!](https://databricks.com/blog/2015/04/13/deep-dive-into-spark-sqls-catalyst-optimizer.html)
# MAGIC   
# MAGIC ![Catalyst](https://files.training.databricks.com/images/105/catalyst-diagram.png)

# COMMAND ----------

(covid_df
 .sort(covid_df["date"].desc()) 
 .filter(covid_df["county"] == "Los Angeles") 
 .show())  #action!

# COMMAND ----------

# MAGIC %md
# MAGIC ###We can see the optimizations in action!
# MAGIC * Go to the Spark UI
# MAGIC * Click on the SQL query associated with your Spark job
# MAGIC * See the logical and physical plans!
# MAGIC   * The filter and sort have been swapped

# COMMAND ----------

# MAGIC %md
# MAGIC ## Spark SQL

# COMMAND ----------

covid_df.createOrReplaceTempView("covid")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT * 
# MAGIC FROM covid
# MAGIC 
# MAGIC -- keys = date, grouping = county, values = cases

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT * 
# MAGIC FROM covid 
# MAGIC WHERE county = "Los Angeles"
# MAGIC 
# MAGIC -- keys = date, grouping = county, values = cases, deaths

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT max(cases) AS max_cases, max(deaths) AS max_deaths, county 
# MAGIC FROM covid 
# MAGIC GROUP BY county 
# MAGIC ORDER BY max_cases DESC
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %md
# MAGIC ###Try your own analysis!
# MAGIC * Here's an idea to get you started
# MAGIC * There's a lot more examples [here](https://databricks.com/blog/2020/04/14/covid-19-datasets-now-available-on-databricks.html)

# COMMAND ----------

# MAGIC %md
# MAGIC **This is census data taken from census.gov**
# MAGIC * It has enough information to be able to construct a fips code column that will correspond the the NYT data

# COMMAND ----------

# MAGIC %sh wget https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv && cp co-est2019-alldata.csv /dbfs/tmp

# COMMAND ----------

census_df = spark.read.csv("dbfs:/tmp/co-est2019-alldata.csv", header=True, inferSchema=True)

#display() is a Databricks only function. It displays the data, like show(), but also gives the visualization options we saw in the SQL section above
display(census_df)

# COMMAND ----------

# MAGIC %md
# MAGIC Let's tweak the DataFrame above to have a fips column that matches the NYT data. Here's the documentation on [user-defined functions (UDFs)](https://docs.databricks.com/spark/latest/spark-sql/udf-python.html).

# COMMAND ----------

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def make_fips(state_code, county_code):
  if len(str(county_code)) == 1:
    return str(state_code) + "00" + str(county_code)
  elif len(str(county_code)) == 2:
    return str(state_code) + "0" + str(county_code)
  else:
    return str(state_code) + str(county_code)

make_fips_udf = udf(make_fips, StringType())
  
census_df = census_df.withColumn("fips", make_fips_udf(census_df.STATE, census_df.COUNTY))

# COMMAND ----------

# MAGIC %md
# MAGIC Now that both the census and the covid data have an identical column, let's join the two DataFrames.

# COMMAND ----------

covid_with_census = (covid_df
                     .na.drop(subset=["fips"])
                     .join(census_df.drop("COUNTY", "STATE"), on=['fips'], how='inner'))

# COMMAND ----------

# MAGIC %md
# MAGIC What do the cases look like for the most populous counties?

# COMMAND ----------

display(covid_with_census.filter("POPESTIMATE2019 > 2000000").select("county", "cases", "date"))

# keys = date, grouping = county, values = cases

# COMMAND ----------

# MAGIC %md
# MAGIC Since the NYT dataset has a new row for every day, with cases increasing each day, let's grab only the most recent numbers for each county.
# MAGIC * Below we're using the `col` function to refer to columns. It's equivalent to something like `df["column_name"]`
# MAGIC * To get the most recent row per county,  we'll use a [window function](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=window#pyspark.sql.Window)

# COMMAND ----------

from pyspark.sql.functions import row_number, col
from pyspark.sql import Window

w = Window.partitionBy("fips").orderBy(col("date").desc())
current_covid_rates = (covid_with_census
                       .withColumn("row_num", row_number().over(w))
                       .filter(col("row_num") == 1)
                       .drop("row_num"))

# COMMAND ----------

# MAGIC %md
# MAGIC What counties are hardest hit when the cases are scaled with their population?

# COMMAND ----------

current_covid_rates = (current_covid_rates
                       .withColumn("case_rates_percent", 100*(col("cases")/col("POPESTIMATE2019")))
                       .sort(col("case_rates_percent").desc()))

#Look at the top 10 counties
display(current_covid_rates.select("county", "state", "cases", "POPESTIMATE2019", "case_rates_percent").limit(10))
