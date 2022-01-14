
## Creating a Notebook

 - One way to create a notebook is to click on the **New Notebook** link from the main Databricks page. You can then provide a name for your notebook and select the default notebook language.

 - From the available list of clusters, select the cluster to which you wish to attach your notebook.
![Start a notebook](images/DataBrickCreateNotebook.png)

 - To start or change a cluster from within a notebook, open the notebook and click on the cluster drop down found at the top right of the notebook. You can then start the cluster or detach it and attach a different one.  

## Notebook Languages
At the time of writing, Databricks notebooks support Python, R, Scala and SQL. The default language of the notebook can be changed by clicking the current language name on the top left corner of the screen as depicted in the screenshot below.
![Change notebook languange](images/changelanguage.png)
![and then](images/changelanguage2.png)

### Mixing Notebook Languages
You can override the default language by specifying the language magic command % at the beginning of a cell. The supported magic commands are: %python, %r, %scala, and %sql.

_Note:_  
When you invoke a language magic command, the command is dispatched to the REPL in the execution context for the notebook. Variables defined in one language (and hence in the REPL for that language) are not available in the REPL of another language. REPLs can share state only through external resources such as files in DBFS or objects in object storage.    

Notebooks also support a few auxiliary magic commands:  
%sh: Allows you to run shell code in your notebook. To fail the cell if the shell command has a non-zero exit status, add the -e option. This command runs only on the Apache Spark driver, and not the workers. To run a shell command on all nodes, use an init script.  
%fs: Allows you to use dbutils filesystem commands.  
%md: Allows you to include various types of documentation, including text, images, and mathematical formulas and equations.  

## Sharing a Databricks Notebook
To share a notebook or invite other collaborators, right-click on a specific notebook file or folder from the Workspace menu, and select **Permissions**. You can also do this by clicking on the **Permissions** button from within a notebook. Once shared, multiple authors can participate in the same notebook session and co-author at the same time.  

**Note:** To add a user to the Databricks workspace, please send a [Slack](https://cae-eac.slack.com) message.  

![How to share a Databricks notebook](images/DataBricksShareNotebook.png)


## Reading Mounted Files

![Access files in your container as if they were local files](images/Accessmountedfile.png)

Example:
```
%python
testData = spark.read.format('csv').options(header='true', inferSchema='true').load('/mnt/mad-du/incoming/age-single-years-2018-census-csv.csv')

display(testData)
```

## Installing Libraries 
### Databricks Cluster
Please contact the [slack](https://cae-eac.slack.com) channel to have the support team install these libraries for you.
### Notebook
Use the following commands to install a library in a notebook session:

Python: 
```python
dbutils.library.installPyPI("pypipackage", version="version", repo="repo", extras="extras")
dbutils.library.restartPython() # Removes Python state, but some libraries might not work without calling this function
```
R Code:
```R
install.packages("library") 
```

## Microsoft Documentation  
- [First Access to Databricks](https://docs.microsoft.com/en-us/azure/azure-databricks/quickstart-create-databricks-workspace-portal#run-a-spark-sql-job)  
- [For more information on Databricks](https://azure.microsoft.com/en-us/resources/videos/connect-2017-introduction-to-azure-databricks)  
- [Databricks Connect](https://docs.databricks.com/dev-tools/databricks-connect.html)
- [Install Libraries in Current Notebook Session](https://docs.microsoft.com/en-us/azure/databricks/notebooks/notebooks-python-libraries)  
- [Library Management for Admins](https://docs.microsoft.com/en-us/azure/databricks/libraries#:~:text=Azure%20Databricks%20supports%20three%20library,its%20path%20in%20the%20workspace)  
