_[Français](../../fr/DataBricks)_

# Accessing Databricks
There are three ways ways one can access a Databricks workspace. A databricks workspace is accessed by navigating to its URL which can be found within the resource's overview page within the Azure portal. You can find your Databricks resource through the Azure Portal by seaching for the reasource using the search box or by navigiating to the CAE dashboard and finding your resource there. 

### Accessing Databricks through the Dashboard

See the [Dashboard section](Dashboards.md) of this documentation from more information.  
1. Click on the Dashboard menu from the Azure Portal.  
![Dashboard](images/DataFactoryDashboard.png)  
2. Under the Azure Databricks section, find the databricks workspace you want to access and click the link.

### Accessing Databricks through the Azure Portal

1. In the Azure Portal Search box, search for **Databricks**.  
![Azure Portal Search](images/DatabricksPortalSearch.png)  

2. You should then see a list of the Databricks workspaces you were given permission to access. Click one of them to open the resource's page.
![DataFactory List](images/DatabricksPortalList.png)

Once the resource page is open, by default you will land on the overview view. Within the view, there is a button to lauch the workspace and there is a attribute that provides the URL to your workspace. By clicking the "Launch Button" or by clicking the URL link you will be redirected your Databricks workspace as displayed in the following image.

![Launch Workspace](images/Databricks/LaunchDatabricksWorkspace.png)

Optionally one also has the option to access their Databricks workspace  without going through the Azure Portal by navigating to https://canadacentral.azuredatabricks.net/, authenticating with your cloud account credentials, and selecting the Databricks workspace that was created for you.  
![Databricks URL](images/DatabricksSelect.png)

## Databricks Connect VM Setup
Databricks connect is a method for accessing a Databricks environment without having to connect through the Azure Portal or the Databricks UI. It allows you to use other IDEs to work on Databricks code.

The following are the steps for installing and testing Databricks Connect on your virtual machine (VM):

1. Databricks Connect conflicts with the Pyspark installation found on the Data Science Virtual Machine images. The default path for this Pyspark installation is `C:\dsvm\tools\spark-2.4.4-bin-hadoop2.7`. Either delete or move this folder in order to install Databricks Connect.

2. Before installing Databricks Connect, create a conda environment. To do this, open a command prompt and run the following commands:
```
    conda create --name dbconnect python=3.7
    conda activate dbconnect
    type pip install -U databricks-connect==X.Y.*
```
**NOTE:** Replace **X** and **Y** with the version number of the Databricks cluster. To find this value, open the Databricks workspace from the Azure portal, click on **Clusters** on the left of the page, and note the **Runtime** version for your cluster.

3. In a command prompt, type **databricks-connect configure**, then enter the following values when prompted:

* **Databricks Host:** `https://canadacentral.azuredatabricks.net`

* **Databricks Token:** a [personal access token](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/authentication#--generate-a-personal-access-token) generated in your Databricks Workspace User Settings

* **Cluster ID:** the value found under **Cluster --> Advanced Options --> Tags** in your Databricks workspace.
![DatabrickConnectClusterID](images/DatabrickConnectClusterID.PNG)

* **Org ID:** the part of the Databricks URL found after **.net/?o=**
![DatabrickConnectOrgID](images/DatabrickConnectOrgID.PNG)

* **Port:** keep the existing value

4. Change the `SPARK_HOME` enviroment variable to `c:\miniconda\envs\(conda env name))\lib\site-packages\pyspark`, and restart your VM. (Please ask for help via a [Slack](https://cae-eac.slack.com) message if you do not know how to change environment variables.)
5. Test the connectivity to Azure Databricks by running **databricks-connect test** in a command prompt. If your Databricks cluster is not running when you start this test you will receive warning messages until it has started, which can take some time.
### Troubleshooting :
1-If you are using databricks connect on windows and you get an error saying: *Cannot find winutils.exe* please refers to https://docs.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect#cannot-find-winutilsexe-on-windows.

## Getting Started

Once inside Databricks you can create a new notebook or open an existing notebook. See [First Access to Databricks](https://docs.microsoft.com/en-us/azure/azure-databricks/quickstart-create-databricks-workspace-portal#run-a-spark-sql-job ) for more information.


# Change Display Language

See [Language](Language.md) page to find out how to change the display language.
