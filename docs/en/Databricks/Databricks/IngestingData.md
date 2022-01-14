# Ingesting Data into Databricks

Data can be downloaded or uploaded to the Databricks File System (DBFS), which is storage specific to the Databricks workspace. You can read data from a data source and  upload a data file (e.g. CSV) directly to the DBFS.

**Note:** The internal data lake container for your environment has already been mounted onto the DBFS for you so you can work with the container directly. Please send a [Slack](https://cae-eac.slack.com) message if you don't know the name of your mounted data lake container.

There are many ways to download data so that it can be used by a Databricks cluster for analysis, transformation, etc. The followings are methods are common ways to do it.
- [Manually upload data to the DBFS mount point](#manually-upload-data-to-the-dbfs-mount-point)
- [Download data from a endpoint using a HTTP request](#download-data-from-an-endpoint-using-a-http-request)
- [Fetch data from a URL and store it in a dataframe](#fetch-data-from-a-url-and-store-it-in-a-dataframe)
- [Use Azure Data Factory to ingest the data into the DBFS mount point](#use-azure-data-factory-to-ingest-the-data-into-the-dbfs-mount-point)

## Manually Upload Data to the DBFS Mount Point

Prequisites: The databricks environment must have a storage account container mounted onto the databricks cluster you are using. 

In this method, the data (files) will be downloaded manually to a CAE VM and then uploaded to a data lake container. While using a Databricks cluster, one can then access the data stored in the container through the mount point. 

In the majority of cases, your project will have a dedicated container within the Azure data lake named **statsconviddsinternal**. Assuming this is the case for your project, after downloading the files to your local filesystem on your CAE VM, you can upload the data to the data lake through either the Azure Storage Explorer application or through the Azure portal. 

After uploading the data to your container within the data lake, you can access the data within your mount point path /dbfs/<mount point name> in your databricks workspace.

**Note:** One of the main benifits of using the Azure Storage Explorer application over the Azure portal is that with the application, one can upload folders and their contents to a data lake. Using the Azure portal, one cannot upload folders.  

## Download Data from an Endpoint using a HTTP Request
Perhaps the data you wish to ingest is provided by a website through a HTTP URL. If this is the case, you can create a Databricks notebook that downloads the file to the file system using a HTTP GET request. Python has many librarys which can be used to execute HTTP requests. One of the popular libraries to use is the requests library (https://docs.python-requests.org/en/latest/). 

After creating a notebook dedicated to ingesting data, you can optionally configure a execution schedule for the notebook. For instance, you can setup a schedule such that the notebook is executed every week at 10:00 AM on Mondays. This is useful if you know the data will be updated on a defined schedule and you always want the latest data. Refer to [this section](#databricks-jobs) for more information on Databricks jobs.

An example of some data sources which can accessed through a HTTP request, Github and the Statistics Canada website with CODR data. A brief overview of how one might download data from these data sources is what follows.
<br/>
<br/>

### Upload Data from Github

 There are multiple of ways to download Github data. For instance, the following are a couple examples of some URLs that can be used to download data:
- Individual files on a specific branch. 
    - ht<span>tps://github.com</span>/&lt;owner&gt;/&lt;repo&gt;/raw/main/&lt;branch&gt;/&lt;path to file&gt;.
- The entire repository based on a tag or branch name respectively. 
    - ht<span>tps://github.com</span>/&lt;owner name&gt;/&lt;repository name&gt;/archive/refs/tags/&lt;tag name&gt;.zip
    - ht<span>tps://github.com</span>/&lt;owner name&gt;/&lt;repository name&gt;/archive/refs/heads/&lt;branch name&gt;.zip
- Release assets based on the tag name and the name of the file.
    - ht<span>tps://github.com</span>/&lt;owner name&gt;/&lt;repository name&gt;/releases/download/&lt;tag name&gt;/&lt;file name&gt;

An example of Python code that uses the requests library to download a repository is displayed in the code block below. 

```python
    import requests
    
    #Open in binary mode and download file to current directory
    with open(file_name,"wb") as file:
        response = requests.get("https://github.com/StatCan/cae-eac/archive/refs/heads/master.zip")
        file.write(response.content)
```
<br/>

### Download CODR Data using the Statcan Web Service

Another example of a website you might download data from using HTTP requests is the Statcan website. One can download CODR data from the website using the web service they provide. As mentioned on the Statcan website, "Statistics Canada has developed a Web Data Service that provides access to data and metadata that we release each business day. This is a good option for users who want to consume a discrete amount of data points updates to Statistics Canada data". Refer to https://www.statcan.gc.ca/en/developers/wds/user-guide for more information. 

To download an entire table in the form of a .csv file, one can call the **ht<span>tps://www150.statcan.gc.ca</span>/t1/wds/rest/getFullTableDownloadCSV/&lt;PID>** endpoint. 

```python
    import requests
    import io
    import zipfile

    response = requests.get(f"https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{PID}/en")
    fileURL = response.json()['object']

    #download zip file to current directory
    response = requests.get(fileURL)
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall("./")
```

## Fetch Data from a URL and Store it in a Dataframe
As an alternative to downloading files to the file system before cleaning and transforming the data, one can also directly fetch the data from an URL and store it within a dataframe. By doing this, one can trasform the data before it is saved to the file system. This is also a good method if it not nessessary to save the data to the file system, even after transforming the data. 

```python
    import pandas as pd 

    #Ingest data into a Python dataframe
    pd.read_csv("https://github.com/2014_data/raw/master/countries.csv")

    #Ingest data into a Spark dataframe
    spark.read.csv("https://github.com/2014_data/raw/master/countries.csv")

```

## Use Azure Data Factory to Ingest Data into the DBFS Mount Point 
If you want to create a data ingestion pipeline that has minimal or no code, then using Azure Data Factory (ADF) may be the best option. Using ADF, pipelines are created using drag and drop boxes. One can create a pipeline that fetches data from a URL on the internet and transfers it into a data lake container that can be accessed by a Databricks cluster. This can be done by just using the copy activity as displayed below. 

One can also create a pipeline where the data undergoes a seiries of transformations before it is copied into the data lake. This can be done using the Data Flow activity (refer to the following documentation for more information https://docs.microsoft.com/en-us/azure/data-factory/concepts-data-flow-overview). 

<br/>

# Databricks Jobs
Databricks jobs are used to run code on a schedule. There are five types of jobs, Notebook, JAR, Spark Submit, Python and Pipeline. Each job has a task which essentially represents a step in a job. A job can have one or many tasks. Each notebook task, requires the creator to input the task name, the location of the notebook to run, and the parameters of the task. Whereas for each job, one has the option to configure the execution schedule, alerts, the permission structure, the maximum number of concurrent runs and the databricks cluster to run the code on.

The value of parameters on a notebook task can be read from the notebook using the `dbutils.widgets.get("<parameter name")` command (Databricks widgets). Refer to [Databricks Widgets](https://docs.databricks.com/notebooks/widgets.html) for more information on widgets. 

## All-Purpose Clusters vs Job Clusters
As per the Databricks [documentation](https://docs.microsoft.com/en-us/azure/databricks/clusters/cluster-config-best-practices), "all-purpose clusters can be shared by multiple users and are best for performing ad-hoc analysis, data exploration or development". Once a all-purpose cluster has been started, it will run until it has been manually terminated or it has been idle for the amount of time configured for auto-shutdown.

Job clusters on the other hand are not shared by other workloads and are only started when a job is executed and gets terminated immediately after the job completes. Therefore, using job clusters for Databricks jobs can benificial since each task runs in a fully isolated environment and it can save on costs because the cluster is only running for the duration of the job.