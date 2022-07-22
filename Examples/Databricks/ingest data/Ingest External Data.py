# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest External Data
# MAGIC 
# MAGIC This notebook can be used to download an external file. When running the notebook as a databricks job, the notebook requires the following parameters:
# MAGIC - **url**: defines the endpoint used to fetch the data.
# MAGIC - **working_directory**: defines where the file will be downloaded to. 
# MAGIC 
# MAGIC The notebook can also be used to download a Github repo using the following urls:
# MAGIC - https://github.com/&lt;owner>/&lt;repo>
# MAGIC - https://github.com/&lt;owner>/&lt;repo&gt;/tree/&lt;branch&gt;/&lt;folder>
# MAGIC - https://github.com/&lt;owner&gt;/&lt;repo&gt;/archive/&lt;branch&gt;.zip"

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
    """
    Retrieves the content of a zip file from the passed URL and 
    extracts the content of the zip file into the current directory.
    """
    
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("./")

def downloadFile(url,file_name=None):
    """
    Downloads a file given a URL to the current directory.
    """
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
    """
    Returns true if the URL follows one of the following URL structures:
    - https://github.com/<owner>/<repo>
    - https://github.com/<owner>/<repo>/tree/<branch>/<folder>
    """
    return isGithubLink(url) and ("/tree/" in url or url.count('/') == 2)

def downloadGithubRepo(url): 
    """
    Downloads a Github repo if the URL follows one of the following URL structures:
    - https://github.com/<owner>/<repo>
    - https://github.com/<owner>/<repo>/tree/<branch>/<folder>
    """
    
    if not isGithubRepo(url):
        print(f"URL {url} is not a github link. Exiting")
        return 

    afterDomain = url.replace("https://github.com/","")
    if "/tree/" in url:
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
    elif url.count('/') == 2:
        indexOfNextSlash = afterDomain.find("/")
        owner = afterDomain[0:indexOfNextSlash]
        print(owner)

        afterOwner = afterDomain[indexOfNextSlash + 1:]
        indexOfNextSlash = afterOwner.find("/")
        repo = afterOwner[0:indexOfNextSlash]
        print(repo)
        
        url = f"https://github.com/{owner}/{repo}/archive/master.zip"
        downloadZipFile(url)
    else:
        print("URL type is not recogonized")

# COMMAND ----------

os.chdir(dbutils.widgets.get("working_directory"))
print("The current working directory: {0}".format(os.getcwd()))

url = dbutils.widgets.get("url")
if isGithubRepo(url):
    downloadGithubRepo(url)
else:
    downloadFile(url)

# COMMAND ----------


