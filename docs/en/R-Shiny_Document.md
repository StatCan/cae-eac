# How To Use RStudio-Server On the Cluster

1. Open your databrick workspace and select the cluster on which rstudio-server and rshiny have been installed. Then select the **Apps** tab.

<img src="images\databricks_clustertab.jpg" alt="Databricks Workspace" width="75%"/>
<img src="images\clusters_select.png" alt="Clusters" width="75%"/>
<img src="images\cluster_apptab.png" alt="App Tab" width="75%"/>
<img src="images\rstudio-server_apptab.png" alt="Login Info" width="75%"/>

2. Note your username and unique password for accessing rstudio-server. Ensure you keep your password safe and secure.
   
3. Click "Open RStudio". You will be prompted for the login information you just got. After sign in you should see rstudio open up.

<img src="images\rstudio_signin.png" alt="RStudio Server Sign in" width="20%"/>
<img src="images\rstudio_open.png" alt="RStudio Window" width="75%"/>

***
## RShiny example

After logging in to RStudio, you can import the Shiny package and run the example '01_hello':

```
> library(shiny)
> runExample("01_hello")
```

You should see output:

Listening on http://127.0.0.1:7726

<img src="images\rstudio_exampleoutput.png" alt="Example Output" width="75%"/>

***
## Use Apache Spark inside Shiny apps

The following example uses SparkR to launch Spark jobs. The example uses the [ggplot2 diamonds dataset](https://ggplot2.tidyverse.org/reference/diamonds.html) to plot the price of diamonds by carat. The carat range can be changed using the slider at the top of the application, and the range of the plot's x-axis would change accordingly.

```
library(SparkR)
library(sparklyr)
library(dplyr)
library(ggplot2)
sparkR.session()

sc <- spark_connect(method = "databricks")
diamonds_tbl <- spark_read_csv(sc, path = "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")

# Define the UI
ui <- fluidPage(
  sliderInput("carat", "Select Carat Range:", min = 0, max = 5, value = c(0, 5), step = 0.01),
  plotOutput('plot')
)

# Define the server code
server <- function(input, output) {
  output$plot <- renderPlot({
    # Select diamonds in carat range
    df <- diamonds_tbl %>%
      dplyr::select("carat", "price") %>%
      dplyr::filter(carat >= !!input$carat[[1]], carat <= !!input$carat[[2]])

    # Scatter plot with smoothed means
    ggplot(df, aes(carat, price)) +
      geom_point(alpha = 1/2) +
      geom_smooth() +
      scale_size_area(max_size = 2) +
      ggtitle("Price vs. Carat")
  })
}
# Return a Shiny app object
shinyApp(ui = ui, server = server)

```

Output:

Listening on http://127.0.0.1:7726

<img src="images\rstudio_ggplot_example.png" alt="Rstudio Job Succeeded" width="75%"/>
<img src="images\rstudio_ggplot_output.png" alt="GGPlot Example Output" width="75%"/>