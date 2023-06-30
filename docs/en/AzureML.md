## Getting Started

1.	On the machine learning **Overview** page, click **Launch studio**.

    ![Launch Studio button](images/AzureML_03.png)  

2.	Use the drop-down to select **vdl** subscription and the **Machine Learning workspace** you want to access, then click **Get started**.

    ![Select subscription and workspace](images/AzureML_04.png)

3. Once inside your Machine Learning workspace, you can train, deploy and manage machine learning models, use AutoML, and run pipelines. See [Getting started quickly]( https://docs.microsoft.com/en-us/azure/machine-learning/) for more information.

    ![Azure Machine Learning Studio](images/AzureML_05.png)  

## Using Azure ML Notebook standalone
### Requirements

A compute instance in Azure ML. You should see it under **Compute --> Compute instances**.

**Note**: If a compute instance has not been created for you, please contact the support team via [Slack](https://cae-eac.slack.com).

### Steps

1.	Under **Notebooks**, create a new notebook in your user directory. You can then enter the code to execute.

    ![Create new file](images/CreateFile.png)  

2.	Select the **Compute instance** assigned to you.

    ![Select compute instance](images/SelectInstanceCompute.png)

3.	Click the **run all cells button** to execute your code.

    ![Run all cells button](images/RunCells.png)


## Using Databricks Connect as Remote Compute

**Disclaimer:** Please note that the Databricks connect configuration shown below is under revision and will likely change in the near future.

### Requirements

A compute instance in Azure ML. You should see it under **Compute --> Compute instances**.

**Note**: If a compute instance has not been created for you, please contact the support team via [Slack](https://cae-eac.slack.com).

### Steps

1.	Under **Notebooks**, open **Terminal**.

    ![Open terminal](images/AzureML_11.png)  

2. Select your **Compute instance** from the drop-down next to **Compute**.

3.  Execute the code from [Databricks Connect Setup](https://github.com/StatCan/cae-eac/blob/master/Examples/AzureML/Databricks-Connect-Setup.txt) in the terminal, while following the prompts to continue as needed. This code installs Python 3.7 and sets up a new kernel for Azure ML notebooks.

    When prompted, enter the following values to configure Databricks connect:

    **Host:** the **URL** from the **Overview** page for your Databricks workspace.

    ![Databrick Connect URL](images/DatabrickConnectURL.PNG)

    **Token:** the [personal access token](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/authentication#--generate-a-personal-access-token) generated in your Databricks Workspace User Settings.

    **Cluster ID:** the value found under **Cluster --> Advanced Options --> Tags** in your Databricks workspace.
    
    ![Databrick Connect Cluster ID](images/DatabrickConnectClusterID.PNG)

    **Org ID:** the part of the Databricks URL found after **.net/?o=**
    
    ![Databrick Connect Org ID](images/DatabrickConnectOrgID.PNG)

    **Port:** keep the existing value

4.	Execute the following code in terminal to test the connectivity to Azure Databricks.
    ```
    databricks-connect test
    ```

5.	Create a new notebook with Azure ML and select the **Python 3 kernel**. It should now display Python 3.7.9

    ![Select Python 3](images/AzureML_13.png)  

6.	Databricks connect should be setup now! Try the [Databricks connect example code](https://github.com/StatCan/cae-eac/blob/master/Examples/AzureML/Databricks-Connect-Example.txt) in a notebook, replacing **public-data/incoming/1test.txt** with the path to a file in your data lake container.

## Request compute
Please contact the support team through the [slack](https://cae-eac.slack.com) channel to request Azure ML compute. You will receive the following error when creating it yourself:

![Create Compute Error](images/AzureMLCreateComputeError.png)
