# Databricks notebook source
dbutils.secrets.listScopes() 

# COMMAND ----------

import pandas as pd
import requests
import urllib.request 
import json
import os
import zipfile

# COMMAND ----------

#Extracts contents of .zip file (named fileName) into a folder (specified by the folderName parameter).
def unzip_file_current_directory(fileName,folderName):
    print("The current working directory: {0}".format(os.getcwd()))
    with zipfile.ZipFile(fileName, 'r') as my_zip:
        my_zip.extractall(folderName)
    print(f"The .zip file {fileName} has been extracted into a folder named {folderName}.")

# Downloads CODR data to current directory
def downloadFullTableCSV(PID, folderName):
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
      print(f"The file {zipFileName} has been deleted")
    else:
      print(f"The file {zipFileName} does not exist")
    


# COMMAND ----------

# DBTITLE 1,Labour Market - CODR
workingDirectory = "/dbfs/mnt/bdl-lde/raw-data/statcan/labour-market"
os.chdir(workingDirectory)
print(os.getcwd())

#Employment by class of worker and industry, seasonally adjusted 
PID = "14100288"
folderName = f"Employment by class of worker and industry, seasonally adjusted"
downloadFullTableCSV(PID,folderName)

#Employment by industry, monthly, seasonally adjusted
PID = "14100355"
folderName = f"Employment by industry, monthly, seasonally adjusted"
downloadFullTableCSV(PID,folderName)

# COMMAND ----------

# DBTITLE 1,Canadian Business - CODR
workingDirectory = "/dbfs/mnt/bdl-lde/raw-data/statcan/canadian-business"
os.chdir(workingDirectory)
print(os.getcwd())

#Canadian Business Counts, with employees
PID = "33100395"
folderName = f"Canadian Business Counts, with employees"
downloadFullTableCSV(PID,folderName)

#Canadian Business Counts, without employees
PID = "33100396"
folderName = f"Canadian Business Counts, without employees"
downloadFullTableCSV(PID,folderName)

#Canadian Business Counts, with employees, census metropolitan areas and census subdivisions
PID = "33100397"
folderName = f"Canadian Business Counts, with employees, census metropolitan areas and census subdivisions"
downloadFullTableCSV(PID,folderName)

#Experimental estimates for business openings and closures for Canada, provinces and territories, census metropolitan areas, seasonally adjusted
PID = "33100270"
folderName = f"Experimental estimates for business openings and closures for Canada, provinces and territories, census metropolitan areas, seasonally adjusted"
downloadFullTableCSV(PID,folderName)

#Experimental indexes of economic activity in the provinces and territories
PID = "36100633"
folderName = f"Experimental indexes of economic activity in the provinces and territories"
downloadFullTableCSV(PID,folderName)

#Real-time Local Business Condition Index (RTLBCI)
PID = "33100398"
folderName = f"Real-time Local Business Condition Index (RTLBCI)"
downloadFullTableCSV(PID,folderName)

# COMMAND ----------

#Canadian Survey on Business Conditions (CSBC)

workingDirectory = "/dbfs/mnt/bdl-lde/raw-data/statcan/CSBC"
os.chdir(workingDirectory)
print(os.getcwd())

startPID = 33100363
for counter in range(32):
  PID = str(startPID + counter)
  folderName = f"canadian-business-{PID}"
  downloadFullTableCSV(PID,folderName)

# COMMAND ----------

# MAGIC %md
# MAGIC ## BDL Data Trust Statcan

# COMMAND ----------

# DBTITLE 1,Labour market
#Download Employment by establishment size, monthly, unadjusted for seasonality
PID = "14100067"
folderName = f"Download Employment by establishment size, monthly, unadjusted for seasonality"
downloadFullTableCSV(PID,folderName)

#Employment by industry by CMA, three-month moving average, unadjusted for seasonality 
PID = "14100379"
folderName = f"Employment by industry by CMA, three-month moving average, unadjusted for seasonality"
downloadFullTableCSV(PID,folderName)

#Labour force characteristics by province and CMA, three-month moving average, seasonally adjusted 
PID = "14100380"
folderName = f"Labour force characteristics by province and CMA, three-month moving average, seasonally adjusted"
downloadFullTableCSV(PID,folderName)

#Labour force characteristics by territory, three-month moving average, seasonally adjusted 
PID = "14100292"
folderName = f"Labour force characteristics by territory, three-month moving average, seasonally adjusted"
downloadFullTableCSV(PID,folderName)

#Labour force characteristics by province and economic region, three-month moving average, unadjusted for seasonality 
PID = "14100387"
folderName = f"Labour force characteristics by province and economic region, three-month moving average, unadjusted for seasonality"
downloadFullTableCSV(PID,folderName)



#Job vacancies, payroll employees, job vacancy rate, and average offered hourly wage by provinces/territories and economic regions, quarterly, unadjusted for seasonality
PID = "14100325"
folderName = f"Job vacancies, payroll employees, job vacancy rate, and average offered hourly wage by provinces/territories and economic regions, quarterly, unadjusted for seasonality"
downloadFullTableCSV(PID,folderName)

#Job vacancies, payroll employees, job vacancy rate, and average offered hourly wage by industry sector, quarterly, unadjusted for seasonality
PID = "14100326"
folderName = f"Job vacancies, payroll employees, job vacancy rate, and average offered hourly wage by industry sector, quarterly, unadjusted for seasonality"
downloadFullTableCSV(PID,folderName)

#Job vacancies, proportion of job vacancies and average offered hourly wage by selected characteristics, quarterly, unadjusted for seasonality
PID = "14100328"
folderName = f"Job vacancies, proportion of job vacancies and average offered hourly wage by selected characteristics, quarterly, unadjusted for seasonality"
downloadFullTableCSV(PID,folderName)

# #Job vacancies and average offered hourly wage by occupation (broad occupational category), quarterly, unadjusted for seasonality
# PID = ""
# folderName = f"Job vacancies and average offered hourly wage by occupation (broad occupational category), quarterly, unadjusted for seasonality"
# downloadFullTableCSV(PID,folderName)



#Job vacancies, payroll employees, and job vacancy rate by provinces and territories, monthly, unadjusted for seasonality
PID = "14100371"
folderName = f"Job vacancies, payroll employees, and job vacancy rate by provinces and territories, monthly, unadjusted for seasonality"
downloadFullTableCSV(PID,folderName)

#Job vacancies, payroll employees, and job vacancy rate by industry sector, monthly, unadjusted for seasonality
PID = "14100372"
folderName = f"Job vacancies, payroll employees, and job vacancy rate by industry sector, monthly, unadjusted for seasonality"
downloadFullTableCSV(PID,folderName)

#Employment and average weekly earnings (including overtime) for all employees by province and territory, monthly, seasonally adjusted
PID = "14100223"
folderName = f"Employment and average weekly earnings (including overtime) for all employees by province and territory, monthly, seasonally adjusted"
downloadFullTableCSV(PID,folderName)

#Fixed weighted index of average hourly earnings for all employees, by industry, monthly
PID = "14100213"
folderName = f"Fixed weighted index of average hourly earnings for all employees, by industry, monthly"
downloadFullTableCSV(PID,folderName)

#Employment insurance beneficiaries (regular benefits) by census metropolitan category, monthly, seasonally adjusted
PID = "14100322"
folderName = f"Employment insurance beneficiaries (regular benefits) by census metropolitan category, monthly, seasonally adjusted"
downloadFullTableCSV(PID,folderName)

# COMMAND ----------

# DBTITLE 1,Canadian business
#Trade in goods by exporter characteristics, by enterprise employment size and industry
PID = "33100226"
folderName = f"Quarterly financial statistics for enterprises"
downloadFullTableCSV(PID,folderName)

# COMMAND ----------

# DBTITLE 1,International Trade
#Trade in goods by exporter characteristics, by enterprise employment size and industry
PID = "12100094"
folderName = f"Trade in goods by exporter characteristics, by enterprise employment size and industry"
downloadFullTableCSV(PID,folderName)

#Trade in goods by exporter characteristics, by industry of establishment and province/territory
PID = "12100098"
folderName = f"Trade in goods by exporter characteristics, by industry of establishment and province/territory"
downloadFullTableCSV(PID,folderName)

#Trade in goods by exporter characteristics, by industry of establishment and census metropolitan area
PID = "12100138"
folderName = f"Trade in goods by exporter characteristics, by industry of establishment and census metropolitan area"
downloadFullTableCSV(PID,folderName)

#Trade in goods by exporter characteristics, by country of destination
PID = "12100104"
folderName = f"Trade in goods by exporter characteristics, by country of destination"
downloadFullTableCSV(PID,folderName)

#Trade in goods by exporter characteristics, by enterprise employment size and export size
PID = "12100097"
folderName = f"Trade in goods by exporter characteristics, by enterprise employment size and export size"
downloadFullTableCSV(PID,folderName)

#Trade in goods by exporter characteristics, by industry of enterprise and number of partner countries
PID = "12100092"
folderName = f"Trade in goods by exporter characteristics, by industry of enterprise and number of partner countries"
downloadFullTableCSV(PID,folderName)

#Trade in goods by importer characteristics, by enterprise employment size and industry
PID = "12100106"
folderName = f"Trade in goods by importer characteristics, by enterprise employment size and industry"
downloadFullTableCSV(PID,folderName)

#Trade in goods by importer characteristics, by industry and census metropolitan area
PID = "12100139"
folderName = f"Trade in goods by importer characteristics, by industry and census metropolitan area"
downloadFullTableCSV(PID,folderName)

#Trade in goods by importer characteristics, by country of origin
PID = "12100114"
folderName = f"Trade in goods by importer characteristics, by country of origin"
downloadFullTableCSV(PID,folderName)

#Trade in goods by importer characteristics, by enterprise employment size and import size
PID = "12100111"
folderName = f"Trade in goods by importer characteristics, by enterprise employment size and import size"
downloadFullTableCSV(PID,folderName)

#Trade in goods by importer characteristics, by industry and related parties
PID = "12100112"
folderName = f"Trade in goods by importer characteristics, by industry and related parties"
downloadFullTableCSV(PID,folderName)

#Trade in goods by importer characteristics, by industry and number of partner countries
PID = "12100105"
folderName = f"Trade in goods by importer characteristics, by industry and number of partner countries"
downloadFullTableCSV(PID,folderName)

# COMMAND ----------

# DBTITLE 1,Output
#GDP at basic prices, by industry, monthly, industry detail
PID = "36100434"
folderName = f"GDP at basic prices, by industry, monthly, industry detail"
downloadFullTableCSV(PID,folderName)

#GDP at basic prices, by industry, provinces and territories 
PID = "36100402"
folderName = f"GDP at basic prices, by industry, provinces and territories"
downloadFullTableCSV(PID,folderName)

# COMMAND ----------

# DBTITLE 1,Environmental
#Climate change investments, by business characteristics
PID = "33100328"
folderName = f"Climate change investments, by business characteristics"
downloadFullTableCSV(PID,folderName)
