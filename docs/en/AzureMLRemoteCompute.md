<!--## Using Attach Databricks as Remote Compute

<!--### Requirements

<!--•	An attached compute in Azure ML. You should see it under **Compute > Attached compute**.

<!--•	A compute instance in Azure ML. You should see it under **Compute > Compute instances**. 

<!--**Note**: If a compute instance or/and attached compute have not been created for you, please contact the support team via [Slack](https://cae-eac.slack.com).

<!--### Steps

<!--1.	Under **Notebooks**, create a new folder in your user directory.

<!--![AzureML_06](images/AzureML_06.png)  
 
<!--2.	Create a sample **.py** file in the newly created folder, and select **Text** as the **File type**. 

<!--![AzureML_07](images/AzureML_07.png)  
 
<!--This file should contain your Python code to execute with Databricks. 
<!--![AzureML_08](images/AzureML_08.png)  

<!--3.	In your user root directory, create a new **notebook**.

<!--![AzureML_09](images/AzureML_09.png)  
 
<!--4.	Copy and paste the [Attach-Databricks-Notebook](https://github.com/StatCan/cae-eac/blob/master/Examples/AzureML/Attach-Databricks-Notebook.txt) code in the new notebook. Update the code with the missing values. It should run as validated with Azure ML SDK version 1.18.0.

<!--![AttachNotebook](images/AttachNotebook.png)  

<!--5.	You can see the results with the following steps:

    <!--a.  Click on the **PipelineRun link**.

    ![PipelinRun Link](images/AttachDatabricks.png) 

    b.  Click on the **Databricks run page link** under **Outputs + logs**.

    ![AttachDatabricks Result](images/AttachDatabricksResult0.PNG)  

    c.  You should be redirected to the Databricks run page.

    ![AttachDatabricksResult](images/AttachDatabricksResult.PNG)
      
    d. Under **Driver Logs**, see the result in the **Standart output** tab.

    ![AttachDatabricksResult2](images/AttachDatabricksResult2.PNG)    
 

<!--**References**: 

<!--•	[Using Databricks Connect](https://github.com/hudua/azureml-databricks/blob/main/guides/azure-ml-databricks-connect.md)

<!--•	[Using attach Databricks as remote compute](https://github.com/hudua/azureml-databricks/blob/main/guides/azure-ml-attach-databricks.md)



