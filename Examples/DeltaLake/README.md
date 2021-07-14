# Delta Lake Examples

## Example Code Text Files

These files contain sample code showing how to create and use delta tables in both Databricks and Azure Synapse notebooks, using PySpark (Python), Scala, and/or SQL.

All of the sample code provided here is compatible with both Databricks and Synapse, **except for SQL, which is only supported in Databricks.**

## Sample Notebooks

This folder contains example notebook files that can be imported into either Databricks or Azure Synapse, as well as the sample data files that were used in each notebook.

**covid_tracking_sample_data_1.json** is used in the Databricks notebook.

**data_duplicate_sample_data_2.csv** is used in the Synapse notebook.

**If the sample notebook does not run**, you may need to upload the respective data file to your data lake and change the path to the file within the notebook accordingly.

### How to Import Notebooks into Databricks

1. Open the sample notebook file (**.dbc**) on Github. Copy the URL in your browser.
2. Within Databricks, open the **Workspace** menu.
3. Find the folder where you want to import the sample notebook and click the down arrow. Then click **Import**.
4. Next to **Import from**, click on **URL**, and paste in the URL copied from GitHub. Click **Import**. The sample notebook will now be in that folder.

### How to Import Notebooks into Synapse

1. Open the sample notebook file (**.ipynb**) on GitHub. Click on **Raw** to show the source code, then right click anywhere and **Save Page As...** to download the file to your computer.
2. Within Synapse, navigate to the **Develop** tab.
3. Click the plus button to add a new resource, then click **Import**.
4. Find the sample notebook file and upload it.