# Databricks notebook source
# MAGIC %md
# MAGIC #Statistics Canada Web Service
# MAGIC This notebook showcases python code that uses the Statistics Canada web service to import data into a datalake and then access the data to perform some analysis using Python. The web service documentation can be found in the following link https://www.statcan.gc.ca/en/developers/wds.
# MAGIC 
# MAGIC To import data from Statistics Canada using their web service, one can use the getFullTableDownloadCSV endpoint. To call this endpoint, a product identification number is required. Product Identification number (PID) is a unique product identifier for all Statistics Canada products, including large multidimensional tables. The first two digits refer to a subject, the next two digits refer to product type, the last four digits refer to the product itself.
# MAGIC 
# MAGIC **GET URL**: https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/< PID >/en
# MAGIC 
# MAGIC In this example, data will be imported from table 10-10-0002-01 (formerly CANSIM 191-0002). The table contains central goverment debt data (refer to https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010000201 for more information).

# COMMAND ----------

# MAGIC %python
# MAGIC import pandas as pd
# MAGIC import requests
# MAGIC import urllib.request 
# MAGIC import json
# MAGIC import os
# MAGIC import zipfile
# MAGIC 
# MAGIC workingDirectory = "/dbfs/mnt/bdl-lde/examples/statistics_canada_web_service"
# MAGIC os.chdir(workingDirectory)
# MAGIC print(os.getcwd())

# COMMAND ----------

# MAGIC %python
# MAGIC #Extracts contents of .zip file (named fileName) into a folder (specified by the folderName parameter).
# MAGIC def unzip_file_current_directory(fileName,folderName):
# MAGIC     print("The current working directory: {0}".format(os.getcwd()))
# MAGIC     with zipfile.ZipFile(fileName, 'r') as my_zip:
# MAGIC         my_zip.extractall(folderName)
# MAGIC     print(f"The .zip file {fileName} has been extracted into a folder named {folderName}.")

# COMMAND ----------

# MAGIC %python
# MAGIC os.chdir(workingDirectory)
# MAGIC 
# MAGIC def downloadFullTableCSV(PID, folderName):
# MAGIC     zipFileName = f"{folderName}.zip"
# MAGIC     
# MAGIC     #Fetch the URL to the specified table. Store the URL within the fileURL variable.
# MAGIC     response = requests.get(f"https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{centralGovermentDebtPID}/en")
# MAGIC     fileURL = response.json()['object']
# MAGIC 
# MAGIC     #Download the specified table (.zip file). 
# MAGIC     urllib.request.urlretrieve(fileURL, zipFileName) 
# MAGIC     unzip_file_current_directory(zipFileName, f"bronze/{folderName}")
# MAGIC 
# MAGIC     #Delete the .zip file. Keep the extracted contents of the zip file.
# MAGIC     if os.path.exists(zipFileName):
# MAGIC       os.remove(zipFileName)
# MAGIC       print(f"The file {zipFileName} has been deleted")
# MAGIC     else:
# MAGIC       print(f"The file {zipFileName} does not exist")
# MAGIC     
# MAGIC centralGovermentDebtPID = "10100002"
# MAGIC folderName = "centralGovermentDebt"
# MAGIC downloadFullTableCSV(centralGovermentDebtPID,folderName)

# COMMAND ----------

# MAGIC %python
# MAGIC df = pd.read_csv(f"./bronze/{folderName}/{centralGovermentDebtPID}.csv")
# MAGIC display(df)

# COMMAND ----------

# MAGIC %python
# MAGIC print(df.columns)
# MAGIC print(df.shape)
# MAGIC print(df.dtypes)

# COMMAND ----------

# MAGIC %python
# MAGIC df['REF_DATE'] = pd.to_datetime(df['REF_DATE'])
# MAGIC df['REF_DATE'] = df['REF_DATE'].dt.date.apply(lambda x: x.strftime('%Y-%m'))

# COMMAND ----------

# MAGIC %python
# MAGIC df = df[df['REF_DATE'] == '2021-10']

# COMMAND ----------

# MAGIC %python
# MAGIC #Write adjusted table to the datalake
# MAGIC print(os.getcwd())
# MAGIC if(not(os.path.exists(f"./silver/{folderName}"))):
# MAGIC     os.mkdir(f"./silver/{folderName}")
# MAGIC     
# MAGIC df.to_csv(f"./silver/{folderName}/{centralGovermentDebtPID}.csv")

# COMMAND ----------

git clone 
