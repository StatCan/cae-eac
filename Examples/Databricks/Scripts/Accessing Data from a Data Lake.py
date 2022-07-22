# Databricks notebook source
# MAGIC %md
# MAGIC # Accessing Data Lake Storage
# MAGIC 
# MAGIC This notebook will show you how to access data within an Azure data lake container. A data lake container can be accessed within a Databricks workspace by mounting (FUSE mount) the container onto a Databricks cluster. The mount is a pointer to a Blob storage container which provides a secure and virtual filesystem. This ultimately means mounting object storage to DBFS allows you to access objects in object storage as if they were on the local file system but the data within the container is never synced locally. Once a mount point is created through a cluster, users of that cluster can immediately access the mount point.
# MAGIC 
# MAGIC DBFS uses the credential that you provide when creating the mount point to access the mounted Blob storage container. In this case, we use a service principal to authorize to the container with read, write and execute permissions.
# MAGIC 
# MAGIC The mount point is created within the DBFS (Databricks File System). In particular, the mount point are created within the /dbfs/mnt directory and data written to mount point paths (/mnt) is stored outside of the DBFS root. For instance, a path to a mount point could be /dbfs/mnt/&lt;mount name&gt;. To list all of the mount points, execute the **display(dbutils.fs.mounts())** command.
# MAGIC 
# MAGIC Note: Almost all information in this notebook was copied from https://docs.databricks.com/data/databricks-file-system.html & https://docs.databricks.com/data/data-sources/azure/azure-storage.html#mount-azure-blob-storage-dbfs. See these web pages for more information. 

# COMMAND ----------

# MAGIC %md
# MAGIC In a Databricks cluster you can access DBFS objects using the Databricks file system utility, Spark APIs, or local file APIs. 
# MAGIC <br/>
# MAGIC 
# MAGIC - **Databricks File System Utility** <br/>
# MAGIC dbutils.fs provides file-system-like commands to access files in DBFS. To list the available commands, run dbutils.fs.help(). For example, you can list the file & directories within a mount point by executing the dbutils.fs.ls("/mnt/&lt;mount name&gt;") command. You can also use the %fs magic command to use dbutils filesystem commands. %fs and dbutils.fs read by default from root (dbfs:/). To read from the local filesystem, you must use file:/.
# MAGIC ```
# MAGIC dbutils.fs.ls("/mnt/<mount name>/")   #List the files within the /dbfs/mnt/<mount name> directory
# MAGIC ```
# MAGIC - **Spark APIs** <br/>
# MAGIC When you use the Spark APIs to access DBFS (for example, by calling spark.read), you must specify the full, absolute path to the target DBFS location. The path must start from the DBFS root, represented by / or dbfs:/, which are equivalent. An example of a command to read a CSV file into a Spark dataframe is the following:
# MAGIC ```
# MAGIC df = spark.read.csv('/mnt/<mount name>/<path to file>/<file name>.csv')
# MAGIC ```
# MAGIC 
# MAGIC - **Local File APIs** <br/>
# MAGIC The typical use case for the folloing local file APIs are if you are working with a single node.
# MAGIC   - %sh reads from the local filesystem by default. To access root or mounted paths in root with %sh, preface the path with /dbfs/. 
# MAGIC   ```
# MAGIC   %sh <command> /dbfs/mnt/<mount name>;
# MAGIC   %sh ls /dbfs/mnt/<mount name>;
# MAGIC   ```
# MAGIC   - You can use the **os** library in Python as to copy files, delete files, create files, etc:
# MAGIC   ```
# MAGIC   import os
# MAGIC   os.<command>('/dbfs/mnt/<mount name>')
# MAGIC   os.listdir('/dbfs/mnt/<mount name>')
# MAGIC   ```
# MAGIC   - The Pandas library in Python can also be used to perform data manipulation and analysis.
# MAGIC   ```
# MAGIC   import pandas as pd
# MAGIC   df = pd.read_csv('/dbfs/mnt/<mount name>/<path to file>/<file name>.csv') #Read data into Python dataframe
# MAGIC   ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## Accessing CODR Data from an Azure Data Lake
# MAGIC 
# MAGIC I believe the only way to load an entire CODR table into a dataframe is to first download the data into the DBFS. It may not be possible to load CODR data from a URL directly into a dataframe. As per the Statistics Canada web service for accessing data documentation (https://www.statcan.gc.ca/en/developers/wds), "users who require the full table/cube of extracted time series, a static file download is available in both CSV and SDMX (XML) formats. Both return a link to the ProductId (PID) supplied in the URL". To download a CSV file of a CODR table, the getFullTableDownloadCSV resource should be called.
# MAGIC 
# MAGIC An example of a process for loading a table into a dataframe would be the following:
# MAGIC 1. Call the https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/&lt;PID&gt;/en endpoint to download a CODR table as a CSV. The downloaded file will be a zip file which contains the table's data and some metadata. Extract and the zip file and copy it into the data lake. 
# MAGIC ```python
# MAGIC def downloadFullTableCSV2(PID):
# MAGIC     zipFileName = f"{folderName}.zip"
# MAGIC     
# MAGIC     #Fetch the URL to the specified table. Store the URL within the fileURL variable.
# MAGIC     response = requests.get(f"https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{PID}/en")
# MAGIC     fileURL = response.json()['object']
# MAGIC     
# MAGIC     r = requests.get(fileURL)
# MAGIC     z = zipfile.ZipFile(io.BytesIO(r.content))
# MAGIC     z.extractall("./")
# MAGIC ```
# MAGIC 2. Load the data into a dataframe from the location of the file within the data lake. 
# MAGIC 
# MAGIC Currently all the CODR data specified for this project was download into the /dbfs/mnt/bdl-lde/statcan directory. Within this directory, the data is organized by the tables theme.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Accessing External Data Sources
# MAGIC If the data source has a endpoint to download the data as a file, the data does not need to be ingested into the data lake first. Often one might to ingest the data anyways in the case the data source dissapears and we want to maintain full reproducibility & tracebility of the data. 
# MAGIC 
# MAGIC An example of loading data into a Python or Spark dataframe from the data lake: 
# MAGIC - **Python dataframe**
# MAGIC   ```
# MAGIC   import pandas as pd
# MAGIC   df = pd.read_csv('/dbfs/mnt/bdl-lde/bronze/job_postings_tracker/CA/provincial_postings_ca.csv')
# MAGIC   ```
# MAGIC - **R dataframe**
# MAGIC   ```
# MAGIC   df <- read.csv("/dbfs/mnt/bdl-lde/bronze/job_postings_tracker/CA/provincial_postings_ca.csv", header = TRUE)
# MAGIC   ```
# MAGIC - **Spark dataframe**
# MAGIC   ```
# MAGIC   df = spark.read.option("header",True).csv("/mnt/bdl-lde/bronze/job_postings_tracker/CA/provincial_postings_ca.csv")
# MAGIC   ```
# MAGIC   
# MAGIC An example of loading data into a Python or Spark dataframe directly from a URL:
# MAGIC 
# MAGIC - **Python dataframe**
# MAGIC   ```
# MAGIC   df = pd.read_csv(https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/CA/provincial_postings_ca.csv)
# MAGIC   ```
# MAGIC - **R dataframe**
# MAGIC   ```
# MAGIC   df <- read.csv("https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/CA/provincial_postings_ca.csv)
# MAGIC   ```
# MAGIC - **Spark dataframe** <br>
# MAGIC   Loading data from an URL that returns a file seems to not be supported by the Spark API. One may need to download the file first, and then load the file into a Spark dataframe.
# MAGIC 
# MAGIC Note: the FQDN of the external data source must be whitelisted on the firewall for this to work.

# COMMAND ----------

# DBTITLE 1,Display the Contents Within the Data Lake
# MAGIC %python
# MAGIC dbutils.fs.ls("/mnt/bdl-lde/bronze/")

# COMMAND ----------

# DBTITLE 1,Example of Displaying Ingested CODR Data
# MAGIC %python
# MAGIC import pandas as pd
# MAGIC import os
# MAGIC 
# MAGIC fileSize = os.path.getsize("/dbfs/mnt/bdl-lde/bronze/statcan/labour-market/Download Employment by establishment size, monthly, unadjusted for seasonality/14100067.csv")
# MAGIC print('File size: ' + str(round(fileSize / (1024 * 1024 * 1024), 3)) + ' Gigabytes')
# MAGIC 
# MAGIC df = spark.read.option("header",True).csv("/mnt/bdl-lde/bronze/statcan/labour-market/Download Employment by establishment size, monthly, unadjusted for seasonality/14100067.csv")
# MAGIC display(df)

# COMMAND ----------

# DBTITLE 1,Example: Filtering the REF_DATE  Column in CODR Table
# MAGIC %python
# MAGIC df = pd.read_csv('/dbfs/mnt/bdl-lde/bronze/statcan/output/GDP at basic prices, by industry, monthly, industry detail/36100434.csv') 
# MAGIC display(df)
# MAGIC 
# MAGIC #Convert the REF_DATE column to the datetime datatype
# MAGIC df['REF_DATE'] = pd.to_datetime(df['REF_DATE'])
# MAGIC df['REF_DATE'] = df['REF_DATE'].dt.date.apply(lambda x: x.strftime('%Y-%m'))
# MAGIC 
# MAGIC #Print all the unique values within the REF_DATE column
# MAGIC print(df['REF_DATE'].unique())
# MAGIC 
# MAGIC #Filter the dataframe to only have rows where the reference date is 2021-10
# MAGIC df = df[df['REF_DATE'] == '2021-10']
# MAGIC display(df)

# COMMAND ----------

# MAGIC %sh 
# MAGIC #Note: Excel files cannot be loaded into a dataframe from a data lake. An excel file can be loaded from a URL. The openpyxl library must be #installed to do so.
# MAGIC 
# MAGIC pip install openpyxl 

# COMMAND ----------

# DBTITLE 1,Example of Displaying External Data Source 
# MAGIC %python
# MAGIC import pandas as pd
# MAGIC 
# MAGIC #load data from data lake
# MAGIC df1 = pd.read_csv('/dbfs/mnt/bdl-lde/bronze/job_postings_tracker/CA/provincial_postings_ca.csv') 
# MAGIC print(df1)
# MAGIC 
# MAGIC #load file from Github
# MAGIC df2 = pd.read_csv('https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/CA/provincial_postings_ca.csv') 
# MAGIC print(df2)
# MAGIC 
# MAGIC 
# MAGIC df3 = pd.read_excel('https://github.com/NicolasWoloszko/OECD-Weekly-Tracker/raw/main/Data/Weekly_Tracker_Excel.xlsx')
# MAGIC display(df3)

# COMMAND ----------

# DBTITLE 1,Downloading an Excel File to the Data Lake as a CSV File
# MAGIC %python
# MAGIC #Load the excel file from a URL into a Pandas dataframe
# MAGIC df3 = pd.read_excel('https://github.com/NicolasWoloszko/OECD-Weekly-Tracker/raw/main/Data/Weekly_Tracker_Excel.xlsx')
# MAGIC 
# MAGIC #Save the dataframe to the datalake as a CSV file
# MAGIC df3.to_csv('file_name.csv')
# MAGIC 
# MAGIC #Validate that the file was downloaded
# MAGIC dbutils.fs.ls("/mnt/bdl-lde/examples/accessing_datalake/data")
# MAGIC 
# MAGIC #load the csv file from the data lake & display it
# MAGIC df = pd.read_csv("/dbfs/mnt/bdl-lde/examples/accessing_datalake/data/file_name.csv")
# MAGIC display(df)

# COMMAND ----------

# DBTITLE 1,Example: Ingest a CODR Table into the Data Lake
# MAGIC %python
# MAGIC 
# MAGIC #Note: to download multiple CODR tables you may find using the /shared/ingest data/Ingest CODR Data Job notebook more convenient then using the below sample code (downloading a single table at a time).
# MAGIC 
# MAGIC import pandas as pd
# MAGIC import requests
# MAGIC import json
# MAGIC import os
# MAGIC import io
# MAGIC import zipfile
# MAGIC 
# MAGIC #Downloads a CODR table into the current directory
# MAGIC def downloadFullTableCSV2(PID):
# MAGIC     zipFileName = f"{folderName}.zip"
# MAGIC     
# MAGIC     #Fetch the URL to the specified table. Store the URL within the fileURL variable.
# MAGIC     response = requests.get(f"https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{PID}/en")
# MAGIC     fileURL = response.json()['object']
# MAGIC     
# MAGIC     r = requests.get(fileURL)
# MAGIC     z = zipfile.ZipFile(io.BytesIO(r.content))
# MAGIC     z.extractall("./")
# MAGIC     
# MAGIC #Set the working directory. This is the directory where the files will be downloaded to.
# MAGIC workingDirectory = "/dbfs/mnt/bdl-lde/examples/accessing_datalake/data"
# MAGIC os.chdir(workingDirectory)
# MAGIC print(os.getcwd())
# MAGIC 
# MAGIC centralGovermentDebtPID = "10100002"
# MAGIC folderName = "centralGovermentDebt"
# MAGIC downloadFullTableCSV2(centralGovermentDebtPID)
# MAGIC 
# MAGIC #List the files that were downloaded
# MAGIC dbutils.fs.ls("/mnt/bdl-lde/examples/accessing_datalake/data")
# MAGIC 
# MAGIC #Load the data into a dataframe & then display it
# MAGIC df = pd.read_csv('/dbfs/mnt/bdl-lde/examples/accessing_datalake/data/10100002.csv')
# MAGIC display(df)
