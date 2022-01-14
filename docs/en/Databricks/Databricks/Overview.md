# Azure Databricks

Databricks is a collaborative data analytics platform that provides a unified experience for "developing data intensive applications: Databricks SQL, Databricks Data Science & Engineering, and Databricks Machine Learning".

![Start a notebook](images/DataBrickCreateNotebook.png)

## Azure Databricks vs Azure Data Factory
In comparison to Azure Data Factory for ETL, ELT processess, Azure Databricks ETL processes are created using code instead of a drag and drop, no code solution. Moreover, with databricks you are able to fine-tune how the back-end works to maximimze performance. This fine-tuning generally isn't available with Data Factory. 

## Azure Databricks vs Azure Synapse
Azure Databricks and Azure Synapse Analytics try to achieve the same thing. The goal of both resources is to have a unified workspace for data science, data engineering and machine learning (with integration to AML). The following are some differences between the two resources:
- Both workspaces use Apache Spark, however the version running on Databricks is about 50 times more performant than the one used by Synapse. 
- Databricks supports real-time co-authoring of notebooks while Synapse doesn't. In Synapse, to see the changes made to a notebook by another user, that user needs to save the notebook first. 
- Azure Synapse has the capability to build a data warehouse with a dedicated SQL pool. Databricks doesn't have the ability to create a Data Warehouse but it can create Delta Lakes which has the main benifits of a data warehouse and a data lake. 

## Azure Databricks vs Azure Machine Learning
`Coming soon`