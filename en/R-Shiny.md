# R-Shiny from RStudio
The document describes how to access to R-Shiny package from RStudio.

## Getting Starting

Please send a [slack](https://cae-eac.slack.com) message to the CEA team to enable RStudio on your databricks cluster to be able to use R-Shiny.

**Warning**: 
R-Shiny clusters are shut down everyday at 7pm. To save cost, please stop your R-Shiny clusters when you are not using them.

## Accessing R-Shiny

1.	From the Azure portal, Launch the Databricks workspace that was created for you.
2.	Click on **Clusters**.
 

3. From the available list of clusters, select the cluster with RStudio installed.

 

    **Note:** You must have the cluster running before you can access to RStudio. See the [Databricks section](../DataBricks/DataBricks.md) for information on how to start a cluster.


4.	Select the **Apps** tab.



5.	Click on **Set up RStudio**.
 

    **Note**: A **one-time password** is generated for you, click on the **show** to display and copy it. You must log in using the Username and Password provided.
 
6.	Click on **Open RStudio**.

 
7.	A new tab opens, enter the username and password provided in the login form and sign in to RStudio.
 

 
8.	From the RStudio UI, enter the **library(shiny)** command in the console to import the Shiny package.


## R-Shiny app example 

We will use the **Hello Shiny** example to explore the structure of a Shiny app.

1. Launch the app from your RStudio session by running :

    library(shiny)

    runExample("01_hello")

2.	Your app should match the image below. 


