# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest CODR Data Job
# MAGIC 
# MAGIC This notebook ingests CODR data into the statsconviddsinternal datalake. The data is stored within the bdl-lde/bronze/statcan/ directory inside the data lake. To ingest the CODR data, the Statistics Canada web service is used (refer to https://www.statcan.gc.ca/en/developers/wds/user-guide for more info).

# COMMAND ----------

import pandas as pd
import requests
import urllib.request 
import json
import os
import platform
import zipfile
import time
import datetime

# COMMAND ----------

# DBTITLE 1,Define the Data to Ingest
# MAGIC %run "./CODR Data to Ingest"

# COMMAND ----------

#Extracts contents of .zip file (named fileName) into a folder (specified by the folderName parameter).
def unzip_file_current_directory(fileName,folderName):
    with zipfile.ZipFile(fileName, 'r') as my_zip:
        my_zip.extractall(folderName)
    print(f"The .zip file {fileName} has been extracted into a folder named {folderName}.")

def wasFileModifiedToday(file_path):
    if os.path.exists(file_path):
        modifiedDate = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if modifiedDate.strftime("%m/%d/%y") == datetime.date.today().strftime("%m/%d/%y"):
            return True
        return False
        
# Downloads CODR data to current directory
def downloadFullTableCSV(PID, folderName):
    if wasFileModifiedToday(f"./{folderName}"):
        print(f"The file {folderName} was modified today. Skipping download.")
        return
    
    zipFileName = f"{folderName}.zip"
    
    #Fetch the URL to the specified table. Store the URL within the fileURL variable.
    response = requests.get(f"https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{PID}/en")
    fileURL = response.json()['object']

    #Download the specified table (.zip file). 
    urllib.request.urlretrieve(fileURL, zipFileName) 
    unzip_file_current_directory(zipFileName, f"{folderName}")

    #Delete the .zip file. Keep the extracted contents of the zip file.
    if os.path.exists(zipFileName):
      os.remove(zipFileName)
    else:
      print(f"Tryed to delete a file named {zipFileName} but it does not exist")


# COMMAND ----------

os.chdir("/dbfs/mnt/bdl-lde/bronze/statcan/")
print(os.listdir("./"))


# COMMAND ----------

# DBTITLE 1,Ingest Data into Data Lake
for theme in codr_tables:
    print(f"\n\nParsing tables from the {theme} theme.")
    
    os.chdir(codr_tables[theme].storage_path)
    print("The current working directory: {0}".format(os.getcwd()))
    for table in codr_tables[theme].tables:
        downloadFullTableCSV(table.PID,(table.indicator).replace("/", ""))
