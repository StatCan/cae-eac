_[Français](../../fr/AzureSynapse)_

# Azure Synapse

## Access Azure Synapse

1. Make sure you are in your cloud VM in order to access Azure Synapse. See [Virtual Machines](VirtualMachines.md) for information on how to create one if needed.

2. Inside your virtual machine, open a web browser and navigate to the Azure Portal (https://portal.azure.com). Sign in with your cloud account credentials.

3. Start typing "synapse" into the search bar to find **Azure Synapse Analytics**.
![Access Synapse](images/AzureSynapseAccess.png) 

4. Find your Synapse Workspace in the list and click on it. Then click **Open Synapse Studio**.
![Open Synapse Studio](images/AzureSynapseOpenStudio.png)


## Start and Stop SQL Pool

1. Click on the **Manage** tab.
![Manage tab](images/AzureSynapseStartStopPool_1.png)

2. Find your dedicated SQL pool in the list and hover over it. You should see a pause button if the pool is currently running, or a start button if it is not. Click the button to start or stop your SQL pool.
![Start or Stop SQL Pools](images/AzureSynapseStartStopPool_2.png)

Note: SQL pools automatically stop running after one hour of inactivity.

## Home

The **Home** tab is where you start when you first open Azure Synapse Studio. 

From here, you can access shortcuts for common tasks such as creating SQL scripts or notebooks by clicking the **New** dropdown menu button. Recently opened resources are also displayed.

## Data

(rough notes)

This is where you can:
- explore everything in your database
- explore linked datasets
- read data from CSV files
- bring data in from linked services

## Develop

(rough notes)

- create SQL scripts, notebooks, Power BI reports

## Integrate

(rough notes)

This is where you create pipelines, much like Data Factory. Show how to do a copy data.

Also transformations on data.

## Monitor

(rough notes)

Can see things like pipeline runs, trigger runs, and SQL requests.

## Manage

(rough notes)

- start and stop SQL and Apache Spark pools
- access control to grant access to different groups of users
- set up git integration

# Change Display Language
See [Language](Language.md) page to find out how to change the display language.


---
### Rough Notes (to be deleted later)
How to access the data lake from azure synapse

How to  create power bi reports?
Please contact the CEA support team to validate that a linked service is setup

Link to Microsoft documentation if available.
