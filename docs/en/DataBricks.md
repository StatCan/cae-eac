# Azure Databricks

## Accessing Databricks
### Dashboard

See the [Dashboard section](Dashboards.md) of this documentation from more information.  
1. Click on the Dashboard menu from the Azure Portal.  
![Dashboard](images/DataFactoryDashboard.png)  

### Databricks URL

1. Navigate to https://canadacentral.azuredatabricks.net/, sign in with your cloud account credentials, and select the Databricks workspace that was created for you.  
![Databricks URL](images/DatabricksSelect.png)

### Azure Portal

1. In the Azure Portal Search box, search for **Databricks**.  
![Azure Portal Search](images/DatabricksPortalSearch.png)  

2. You should then see a list of the Databricks workspaces you were given permission to access.  
![DataFactory List](images/DatabricksPortalList.png)

## Getting Started

Once inside Databricks you can create a new notebook or open an existing notebook. See [First Access to Databricks](https://docs.microsoft.com/en-us/azure/azure-databricks/quickstart-create-databricks-workspace-portal#run-a-spark-sql-job ) for more information.

## Creating a Cluster

Since you do not have permission to create a cluster, please send a [slack](https://cae-eac.slack.com) message if a cluster has not been created for you or if you require changes to your cluster.

**Note:** You must have a cluster running before you can run code inside your notebook. See below or the [FAQ](FAQ.md) for information on how to start a cluster.

## Creating a Notebook

 - One way to create a notebook is to click on the **New Notebook** link from the main Databricks page. You can then provide a name for your notebook and select the default notebook language.

 - From the available list of clusters, select the cluster to which you wish to attach your notebook.
![Start a notebook](images/DataBrickCreateNotebook.png)

 - To start or change a cluster from within a notebook, open the notebook and click on the cluster drop down found at the top right of the notebook. You can then start the cluster or detach it and attach a different one.  

## Sharing a Databricks Notebook

To share a notebook or invite other collaborators, right-click on a specific notebook file or folder from the Workspace menu, and select **Permissions**. You can also do this by clicking on the **Permissions** button from within a notebook. Once shared, multiple authors can participate in the same notebook session and co-author at the same time.  

**Note:** To add a user to the Databricks workspace, please send a [Slack](https://cae-eac.slack.com) message.  

![How to share a Databricks notebook](images/DataBricksShareNotebook.png)

## Ingesting Data into Databricks

Data can be mounted or uploaded to the Databricks File System (DBFS), which is storage specific to the Databricks workspace. You can read data from a data source or even upload a data file (e.g. CSV) directly to the DBFS.

**Note:** The internal data lake container for your environment has already been mounted for you and you can work with the container directly. Please send a [Slack](https://cae-eac.slack.com) message if you don't know the name of your mounted data lake container.

## Adding Data to Databricks

![Where to import data](images/DataBricksImportData.png)

## Reading Mounted Files

![Access files in your container as if they were local files](images/Accessmountedfile.png)

Example:
```
%python
testData = spark.read.format('csv').options(header='true', inferSchema='true').load('/mnt/mad-du/incoming/age-single-years-2018-census-csv.csv')

display(testData)
```

## Changing Notebook Default Language

![Change notebook languange](images/changelanguage.png)
![and then](images/changelanguage2.png)

## Mixing Notebook Languages

You can override the default language by specifying the language magic command % at the beginning of a cell. The supported magic commands are: %python, %r, %scala, and %sql.

_Note:_  
When you invoke a language magic command, the command is dispatched to the REPL in the execution context for the notebook. Variables defined in one language (and hence in the REPL for that language) are not available in the REPL of another language. REPLs can share state only through external resources such as files in DBFS or objects in object storage.    

Notebooks also support a few auxiliary magic commands:  
%sh: Allows you to run shell code in your notebook. To fail the cell if the shell command has a non-zero exit status, add the -e option. This command runs only on the Apache Spark driver, and not the workers. To run a shell command on all nodes, use an init script.  
%fs: Allows you to use dbutils filesystem commands.  
%md: Allows you to include various types of documentation, including text, images, and mathematical formulas and equations.  

## Starting a Databricks Cluster

1. Click on the cluster drop-down list.
2. Select a cluster from the list.
3. Click on the **Start Cluster** link.  
![Where to start a Databricks cluster](images/DataBricksStartCluster.png)  

1. Click on the cluster drop-down list.
2. Select a cluster from the list.
3. Click on the **Start Cluster** link.  
![Where to start a Databricks cluster](images/DataBricksStartCluster.png)  

## Databricks Connect VM Setup
Databricks connect is a method for accessing a databricks environment without having to connect through the Azure Portal. Its main use is to allow you to use other IDEs to work on databricks code.

The following are the steps for installing and testing databricks connect on your VM environment.

1. Databricks Connect has conflictions with the Pyspark instalation that is on our DataScience VMs by default. The default path of this is `C:\dsvm\tools\spark-2.4.4-bin-hadoop2.7`. This folder must be either deleted or moved in order to install Databricks connect.

2. Before installing databricks connect a conda environment should be created. To do this open command prompt and do the following.
```
    conda create --name dbconnect python=3.7
    conda activate dbconnect
    type pip install -U databricks-connect==X.Y.*
```
(X and Y are to be replaced with the version number of the spark cluster. To see this open databricks from the azure portal and click clusters on the left of the page. You are looking for the runtime)
3. Once the installation has finished, you will need to collect 3 peices of information (copy the text somewhere)
* The **databricks Org ID** (check URL from databricks page, look for ?o= the number that follows is the org ID)
* A **personal access token** (Look at the top right of the databricks window for the button "Databricks-XXX", click user settings, then Generate New Token)
* **Cluster ID** (go back to the clusters page, click on the cluster you wish to use, check the URL for `clusters/XXXX-XXXXXX-XXXXXXXXX/configuration` the Xs are the value)
4. In command prompt type databricks-connect configure, then enter these values.

   **Databricks Host:** `https//:canadacentral.azuredatabricks.net`

    **Databricks Token:** `the personal access token from step 3`

    **Cluster ID:** `the cluster ID from step 3`

    **Org ID:** `Once again from part 3`

    **Port:** leave as 15001
5. The last setup step requires changing an enviroment variable `SPARK_HOME` to `c:\miniconda\envs\(conda env name))\lib\site-packages\pyspark` then restart your VM (If you do not know how to change environment variables please ask for help).
6. To test if your configuration setup works enter databricks-connect test in command prompt. If the cluster you are using is not running when you start your test you will receive warning messages until it has started. This can take time.

## Installing Libraries 
### On Databricks Cluster
Please contact the [slack](https://cae-eac.slack.com) channel to have the support team install these libraries for you.
### Notebook
```python
dbutils.library.installPyPI("pypipackage", version="version", repo="repo", extras="extras")
dbutils.library.restartPython() # Removes Python state, but some libraries might not work without calling this function
```

## Microsoft Documentation  
- [Databricks-Connects](https://docs.databricks.com/dev-tools/databricks-connect.html)
- [First Access to Databricks](https://docs.microsoft.com/en-us/azure/azure-databricks/quickstart-create-databricks-workspace-portal#run-a-spark-sql-job)  
- [For more information on Databricks](https://azure.microsoft.com/en-us/resources/videos/connect-2017-introduction-to-azure-databricks)  
- [Install Libraries in Current Notebook Session](https://docs.microsoft.com/en-us/azure/databricks/notebooks/notebooks-python-libraries)  
- [Library Management for Admins](https://docs.microsoft.com/en-us/azure/databricks/libraries#:~:text=Azure%20Databricks%20supports%20three%20library,its%20path%20in%20the%20workspace)  

# Change Display Language

See [Language](Language.md) page to find out how to change the display language.
