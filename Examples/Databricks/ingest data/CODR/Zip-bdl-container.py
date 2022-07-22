# Databricks notebook source
import os
import zipfile
import shutil
import filecmp


# COMMAND ----------

# DBTITLE 1,Define Functions
# Define paths
os.chdir("/dbfs/mnt/bdl-lde")
cwd = os.getcwd()
bdl_path = cwd
temp_zip_path = "/tmp/bdl-lde-zipped"
# Temporarily store bdl here in order to zip it
temp_path = "/tmp/bdl-temp"
databricks_zipped_path = "/dbfs/mnt/bdl-lde/bdl-lde-zipped"
dirs = os.listdir(cwd)
print(dirs)

# Probably don't need this function
def extract_all(source, dest):
    try:
        for dir in os.listdir(source):
            path = os.path.join(source, dir)
            with zipfile.ZipFile(path) as zip:
                zip.extractall(dest)
                print(f"Extracted everything from {dir} into {dest}")
    except:
        print("An error has occured while zipping")
    else:
        comparison = filecmp.dircmp(databricks_path, dest)
        print(comparison)
        comparison.report_full_closure()
    finally:
        shutil.rmtree(dest)
        
# Zip bdl-lde container in databricks into another folder "bdl-lde-zipped"
# located in the bdl container
def zip_bdl(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
        print(dest)
    for dir in dirs:
        zip_path = os.path.join(dest, dir)
        dir_files = os.listdir(dir)
        if dir_files and not dir == "bdl-lde-zipped":
            shutil.make_archive(base_dir=dir, format='zip', base_name=zip_path)
            print(dir, dir_files)

    blobStoragePath = "dbfs:/mnt/bdl-lde/bdl-lde-zipped"
    dbutils.fs.cp("file:" +dest, blobStoragePath, True)
    


    

# COMMAND ----------

# DBTITLE 1,Zip everything in the BDL container
zip_bdl(dirs, temp_zip_path)
