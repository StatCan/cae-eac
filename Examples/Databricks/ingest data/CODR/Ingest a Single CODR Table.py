# Databricks notebook source
import pandas as pd
import requests
import urllib.request 
import json
import os
import zipfile
from datetime import date
from datetime import datetime


# COMMAND ----------

# DBTITLE 1,Functions
#Extracts contents of .zip file (named fileName) into a folder (specified by the folderName parameter).
def unzip_file_current_directory(fileName,folderName):
    print("The current working directory: {0}".format(os.getcwd()))
    with zipfile.ZipFile(fileName, 'r') as my_zip:
        my_zip.extractall(folderName)
    print(f"The .zip file {fileName} has been extracted into a folder named {folderName}.")
    
def downloadFullTableCSV(PID, folderName):
    zipFileName = f"{folderName}.zip"
    
    #Fetch the URL to the specified table. Store the URL within the fileURL variable.
    response = requests.get(f"https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{PID}/en")
    fileURL = response.json()['object']

    #Download the specified table (.zip file). 
    urllib.request.urlretrieve(fileURL, zipFileName) 
    unzip_file_current_directory(zipFileName, f"bronze/{folderName}")

    #Delete the .zip file. Keep the extracted contents of the zip file.
    if os.path.exists(zipFileName):
      os.remove(zipFileName)
      print(f"The file {zipFileName} has been deleted")
    else:
      print(f"The file {zipFileName} does not exist")

# COMMAND ----------

# DBTITLE 1,Directory to Download File to 
workingDirectory = "/dbfs/mnt/bdl-lde/examples/statistics_canada_web_service"
os.chdir(workingDirectory)
print(os.getcwd())

# COMMAND ----------

# DBTITLE 1,Download Action
table_name_to_download = "Private sector business counts by majority ownership"
table_PID = "33100492"

downloadFullTableCSV(table_PID,table_name_to_download)
