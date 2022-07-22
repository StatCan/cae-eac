# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest CODR Data Daily Job
# MAGIC 
# MAGIC This notebook ingests CODR data into the statsconviddsinternal datalake. The data is stored within the bdl-lde/bronze/statcan/ directory inside the data lake. To ingest the CODR data, the Statistics Canada web service is used (refer to https://www.statcan.gc.ca/en/developers/wds/user-guide for more info).
# MAGIC 
# MAGIC The notebook uses the Statistics Canada web service to ingest CODR data (refer to https://www.statcan.gc.ca/en/developers/wds). The **getChangedSeriesList** method to determine what data is new and the **getFullTableDownloadCSV** method to download data. 

# COMMAND ----------

import pandas as pd
import requests
import urllib.request 
import json
import os
import platform
import zipfile
import time
from datetime import date
from datetime import datetime

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
        modifiedDate = datetime.fromtimestamp(os.path.getmtime(file_path))
        if modifiedDate.strftime("%m/%d/%y") == datetime.today().strftime("%m/%d/%y"):
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
      
def uniqueSortedPIDs(changedTables):
    productIDs = []
    today = datetime.today()
    for record in changedTables:
        tableReleaseDate = datetime.fromisoformat(record['releaseTime'])
        if(tableReleaseDate < today):
            productIDs.append(record['productId'])
    
    return sorted(set(productIDs))

# COMMAND ----------

# DBTITLE 1,Ingest Data into Data Lake

def downloadTableIfInList(updatedPID):
    for theme in codr_tables:
        for table in codr_tables[theme].tables:
            if(updatedPID == table.PID):
                print(f"It has been determined that the PID {updatedPID} is in the list of tables to update.")
                os.chdir(codr_tables[theme].storage_path)
                print(f"The current working directory has been switched to {os.getcwd()} to download {table.indicator}")
                downloadFullTableCSV(table.PID,(table.indicator).replace("/", ""))
                return
    print(f"The table with PID {updatedPID} was not found in the list of tables to update")



#Get changed series list
print("Getting the changed series list")
changedTables = []
retryCounter = 0
today = datetime.today().strftime("%Y-%m-%d")
while retryCounter < 4:
    try:
        response = requests.get(f"https://www150.statcan.gc.ca/t1/wds/rest/getChangedCubeList/{today}")
        changedTables = response.json()['object']
        productIDs = []
        for table in changedTables:
            productIDs.append(table['productId'])
        
        print("Successfully retrieved the CODR changed series list.")
        break;
    except Exception as e:
        print("An exception occurred when trying to get the CODR changed series list.")
        print(e)
        time.sleep(5)
        retryCounter += 1

print(changedTables)
for pid in changedTables:        
    print(f"Checking if PID {pid} is in the list of tables to update.")
    downloadTableIfInList(pid)
