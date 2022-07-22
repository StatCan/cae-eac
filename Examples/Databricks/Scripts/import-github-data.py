# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest External File
# MAGIC 
# MAGIC This notebook can be used to download an external file. When running the notebook as a databricks job, the notebook requires the following parameters:
# MAGIC - **url**: defines the endpoint used to fetch the data.
# MAGIC - **working_directory**: defines where the file will be downloaded to. 

# COMMAND ----------

import pandas as pd
import requests
import urllib.request 
import json
import os
import zipfile
import io
import urllib

# COMMAND ----------

def downloadZipFile(url):
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("./")

def downloadFile(url,file_name=None):
    if file_name == None:
        indexOfLastSlash = url.rfind("/")
        file_name = url[indexOfLastSlash + 1:]
        
    # open in binary mode
    with open(file_name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
    
def isGithubLink(source):
    if "https://github.com" in source:
        return True
    return False

def isGithubRepo(url):
    return isGithubLink(url) and ("/tree/" in url or url.count('/') == 2)

def downloadGithubRepo(s1): 
    if not isGithubLink(s1):
        print(f"URL {s1} is not a github link. Exiting")
        return 

    afterDomain = s1.replace("https://github.com/","")
    if "/tree/" in s1:
        indexOfNextSlash = afterDomain.find("/")
        owner = afterDomain[0:indexOfNextSlash]
        print(f"Owner: {owner}")

        afterOwner = afterDomain[indexOfNextSlash + 1:]
        indexOfNextSlash = afterOwner.find("/")
        repo = afterOwner[0:indexOfNextSlash]
        print(f"Repo: {repo}")

        indexOfNextSlash = afterOwner.find("tree/")
        afterRepo = afterOwner[indexOfNextSlash + len("tree/"):]
        indexOfNextSlash = afterRepo.find("/")
        branch = afterRepo[0:indexOfNextSlash]
        print(f"Branch: {branch}")

        url = f"https://github.com/{owner}/{repo}/archive/{branch}.zip"
        downloadZipFile(url)
    elif s1.count('/') == 2:
        indexOfNextSlash = afterDomain.find("/")
        owner = afterDomain[0:indexOfNextSlash]
        print(owner)

        afterOwner = afterDomain[indexOfNextSlash + 1:]
        indexOfNextSlash = afterOwner.find("/")
        repo = afterOwner[0:indexOfNextSlash]
        print(repo)
        
        url = f"https://github.com/{owner}/{repo}/archive/master.zip"
        downloadGithubRepoIntoFolder(s1)
    else:
        print("URL type is not recogonized")

# COMMAND ----------

workingDirectory = "/dbfs/mnt/bdl-lde/examples"
os.chdir(dbutils.widgets.get("working_directory"))
print("The current working directory: {0}".format(os.getcwd()))

url = dbutils.widgets.get("url")
if isGithubRepo(url):
    downloadGithubRepo(url)
else:
    downloadFile(url)

# COMMAND ----------

import pandas as pd

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
url2 = "https://github.com/cs109/2014_data/raw/master/countries.csv"
c = pd.read_csv(url)
c
