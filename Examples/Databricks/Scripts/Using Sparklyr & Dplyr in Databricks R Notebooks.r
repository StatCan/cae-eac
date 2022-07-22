# Databricks notebook source
# MAGIC %md
# MAGIC # Sparklyr: R interface for Apache Spark
# MAGIC # Dplyr: Easy Data Manipulation
# MAGIC The notebook was created from:
# MAGIC - https://docs.databricks.com/spark/latest/sparkr/sparklyr.html
# MAGIC - https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html
# MAGIC - https://mdporter.github.io/ST597/lectures/10-relational.pdf

# COMMAND ----------

# MAGIC %md
# MAGIC **What is Sparklyr**: Sparklyr is an R package that lets you use **Spark** to analyze data while using **familiar tools in R**. Sparklyr supports a complete backend for dplyr, a popular tool for working with data frame objects both in memory and out of memory. sparklyr translates R to SQL. You can use dplyr to translate R code into Spark SQL. Refer to https://spark.rstudio.com/reference/index.html for the sparklyr api reference page.
# MAGIC 
# MAGIC **Dplyr Data Manipulation**: Using dplyr, data can be manipulated using the following verbs (from dplyr.tidyverse.org):
# MAGIC - mutate(): adds new variables that are functions of existing variables
# MAGIC - select(): picks variables based on their names
# MAGIC - filter(): picks cases based on their values
# MAGIC - summarise(): reduces multiple values down to a single summary.
# MAGIC - arrange() changes the ordering of the rows.
# MAGIC 
# MAGIC All verbs combine naturally with **group_by()** which allows you to perform any operation "by group".

# COMMAND ----------

# MAGIC %md ## Install `sparklyr`
# MAGIC 
# MAGIC The following cell installs the latest version of [sparklyr from CRAN](https://cran.r-project.org/web/packages/sparklyr/index.html).
# MAGIC Installation takes a few minutes, as the package requires several dependencies.

# COMMAND ----------

# Install the latest version of Rcpp
install.packages("Rcpp") 

if (!require("sparklyr")) {
  install.packages("sparklyr")  
}

# COMMAND ----------

# MAGIC %md ## Load `sparklyr` package

# COMMAND ----------

library(sparklyr)

# COMMAND ----------

# MAGIC %md ## Create a `sparklyr` connection
# MAGIC 
# MAGIC Use `"databricks"` as the connection method in `spark_connect()`.
# MAGIC No additional parameters to ``spark_connect()`` are required. You do not need to call `spark_install()` as Spark is already installed on the Databricks cluster.
# MAGIC 
# MAGIC Note that `sc` is a special name for `sparklyr` connection. When you use that variable name, the notebook automatically displays Spark progress bars and built-in Spark UI viewers.

# COMMAND ----------

sc <- spark_connect(method = "databricks")

# COMMAND ----------

# MAGIC %md ## Use `sparklyr` and `dplyr` APIs
# MAGIC 
# MAGIC After setting up the `sparklyr` connection, you can use the `sparklyr` API.
# MAGIC You can import and combine `sparklyr` with `dplyr` or `MLlib`.  
# MAGIC If you use an extension package that includes third-party JARs, you may need to install those JARs as libraries in your workspace ([AWS](https://docs.databricks.com/libraries/workspace-libraries.html#workspace-libraries)|[Azure](https://docs.microsoft.com/azure/databricks/libraries/workspace-libraries#workspace-libraries)).

# COMMAND ----------

library(dplyr)

# COMMAND ----------

# Copy a local data frame to a remote src
iris_tbl <- copy_to(sc, iris)
# List all tbls provided by a source
src_tbls(sc)

iris_tbl %>% count

# COMMAND ----------

# MAGIC %md ## Aggregate and visualize data

# COMMAND ----------

iris_summary <- iris_tbl %>% 
  mutate(Sepal_Width = ROUND(Sepal_Width * 2) / 2) %>% # Bucketizing Sepal_Width
  group_by(Species, Sepal_Width) %>% 
  summarize(count = n(), Sepal_Length_Mean = mean(Sepal_Length), stdev = sd(Sepal_Length)) %>% collect

# COMMAND ----------

library(shiny)
runExample("01_hello")

# COMMAND ----------

library(ggplot2)

# Change the default plot height 
options(repr.plot.height = 600)

ggplot(iris_summary, aes(Sepal_Width, Sepal_Length_Mean, color = Species)) + 
  geom_line(size = 1.2) +
  geom_errorbar(aes(ymin = Sepal_Length_Mean - stdev, ymax = Sepal_Length_Mean + stdev), width = 0.05) +
  geom_text(aes(label = count), vjust = -0.2, hjust = 1.2, color = "black") +
  theme(legend.position="top")

# COMMAND ----------

# MAGIC %md
# MAGIC # Using Dplyr
# MAGIC 
# MAGIC ### Verbs
# MAGIC 
# MAGIC **Rows**:
# MAGIC - filter() chooses rows based on column values.
# MAGIC - slice() chooses rows based on location.
# MAGIC - arrange() changes the order of the rows.
# MAGIC 
# MAGIC <br/>
# MAGIC **Columns**:
# MAGIC - select() changes whether or not a column is included.
# MAGIC - rename() changes the name of columns.
# MAGIC - mutate() changes the values of columns and creates new columns.
# MAGIC - relocate() changes the order of the columns.
# MAGIC 
# MAGIC <br/>
# MAGIC **Groups of rows**:
# MAGIC - summarise() collapses a group into a single row.

# COMMAND ----------

# DBTITLE 1,Use a New Dataset
#Copy the flights dataset from R into the Spark c
install.packages(c("nycflights13","Lahman"))
flights_tbl <- copy_to(sc, nycflights13::flights, "flights") #Copy an R data.frame to Spark
airlines_tbl <- copy_to(sc, nycflights13::flights, "airlines") #Copy an R data.frame to Spark
dplyr::src_tbls(sc)

# COMMAND ----------

#dplyr verbs examples
c1 <- select(flights_tbl, year:day, arr_delay, dep_delay)      #select verb
c2 <- flights_tbl %>% filter(dep_delay == 2)                   #filter verb
c3 <- arrange(flights_tbl, desc(dep_delay))                    #arrange verb
c4 <- summarise(flights_tbl, mean_dep_delay = mean(dep_delay)) #summarise verb
c5 <- mutate(flights_tbl, speed = distance / air_time * 60)    #mutate verb
c1

# COMMAND ----------

# MAGIC %md
# MAGIC ##Pipeing
# MAGIC You can use magrittr pipes to write cleaner syntax. The magrittr pipe-like operator is, **%>%**, with which you may use to pipe a value forward into an expression or function call; something along the lines of x %>% f, rather than f(x). We can use pipeing to perform a series of dplyr data manipulation operations with one command.

# COMMAND ----------

c4 <- flights_tbl %>%
  filter(month == 5, day == 17, carrier %in% c('UA', 'WN', 'AA', 'DL')) %>%
  select(carrier, dep_delay, air_time, distance) %>%
  arrange(carrier) %>%
  mutate(air_time_hours = air_time / 60)
c4

# COMMAND ----------

# DBTITLE 1,Group By
c4 <- flights_tbl %>%
  group_by(carrier) %>%
  summarize(count = n(), mean_dep_delay = mean(dep_delay))

# COMMAND ----------

# DBTITLE 1,Joins
flights_tbl %>% left_join(airlines_tbl) 

## same as:
# flights_tbl %>% left_join(airlines_tbl, by = "carrier")
# flights_tbl %>% left_join(airlines_tbl, by = c("carrier", "carrier"))

# COMMAND ----------

# DBTITLE 1,Example
delay <- flights_tbl %>%
  group_by(tailnum) %>%
  summarise(count = n(), dist = mean(distance), delay = mean(arr_delay)) %>%
  filter(count > 20, dist < 2000, !is.na(delay)) %>%
  collect

# plot delays
library(ggplot2)
ggplot(delay, aes(dist, delay)) +
  geom_point(aes(size = count), alpha = 1/2) +
  geom_smooth() +
  scale_size_area(max_size = 2)
