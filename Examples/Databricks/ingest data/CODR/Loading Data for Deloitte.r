# Databricks notebook source
library(cansim)
library(tidyverse)

# COMMAND ----------


Business_activity = list("Gross domestic product (GDP) at basic prices, by industry, monthly" = cansim::get_cansim("36100434"),
                         "Gross domestic product (GDP) at basic prices, by industry, provinces and territories" = cansim::get_cansim("36100402"),
                         "Experimental indexes of economic activity in the provinces and territories" = cansim::get_cansim("36100633"),
                         "Employment by industry, monthly, seasonally adjusted and unadjusted, and trend-cycle, last 5 months" = cansim::get_cansim("14100355"),
                         "Employment by industry, three-month moving average, unadjusted for seasonality" = cansim::get_cansim("14100379"),
                         "Employment by establishment size, monthly, unadjusted for seasonality" = cansim::get_cansim("14100067"),
                         "Labour force characteristics, three-month moving average, seasonally adjusted" = cansim::get_cansim("14100380"),
                         "Labour force characteristics by territory, three-month moving average, seasonally adjusted and unadjusted, last 5 months" = cansim::get_cansim("14100292"),
                         "Labour force characteristics, three-month moving average, unadjusted for seasonality, last 5 months" = cansim::get_cansim("14100387"),
                         "Job vacancies, payroll employees, job vacancy rate, and average offered hourly wage by economic regions, quarterly, unadjusted for seasonality" = cansim::get_cansim("14100325"),
                         "Job vacancies, payroll employees, job vacancy rate, and average offered hourly wage by industry sector, quarterly, unadjusted for seasonality" = cansim::get_cansim("14100326"),
                         "Job vacancies, payroll employees, and job vacancy rate by provinces and territories, monthly, unadjusted for seasonality" = cansim::get_cansim("14100371"),
                         "Job vacancies, payroll employees, and job vacancy rate by industry sector, monthly, unadjusted for seasonality" = cansim::get_cansim("14100372"),
                         "Employment and average weekly earnings (including overtime) for all employees by province and territory, monthly, seasonally adjusted" = cansim::get_cansim("14100223"),
                         "Fixed weighted index of average hourly earnings for all employees, by industry, monthly" = cansim::get_cansim("14100213"),
                         "Gross domestic product, expenditure-based, Canada, quarterly" = cansim::get_cansim("36100104"),
                         "Quarterly balance sheet and income statement, by industry, seasonally adjusted" = cansim::get_cansim("33100226"),
                         "Real-time Local Business Condition Index (RTLBCI)" = cansim::get_cansim("33100398"))

# COMMAND ----------

Business_snapshot = list("Experimental estimates for business openings and closures for Canada, provinces and territories, census metropolitan areas, seasonally adjusted" = cansim::get_cansim("33100270"))


# COMMAND ----------

Work_force = list("Population" = cansim::get_cansim("1410038001"),                  
"Labour force" = cansim::get_cansim("1410038001"),
"Employment" = cansim::get_cansim("1410038001"),
"Unemployment" = cansim::get_cansim("1410038001"),
"Unemployment rate" = cansim::get_cansim("1410038001"),
"Participation rate" = cansim::get_cansim("1410038001"),
"Employment rate" = cansim::get_cansim("1410038001"),
"Employment by industry (NAICS, sa and trend-cycle, Canada, Provs)" = cansim::get_cansim("1410035501"),
"Unemployment duration" = cansim::get_cansim("1410034201"),
"Supplementary unemployment rates" = cansim::get_cansim("1410007701"),
"Wages_Earnings" = cansim::get_cansim("1410021301"),
"Employment Insurance" = cansim::get_cansim("1410032201"),
"Job vacancies, payroll employees, vacancy rate, average offered hourly wage by industry" = cansim::get_cansim("1410040001"),
"Job vacancies, payroll employees, vacancy rate, average offered hourly wage by broad occupational category" = cansim::get_cansim("1410039901"),
"Job vacancies, payroll employees, vacancy rate, average offered hourly wage by economic regions" = cansim::get_cansim("1410039801"),
"Job vacancies, payroll employees, and job vacancy rate by provinces and territories, monthly, unadjusted for seasonality" = cansim::get_cansim("1410037101"),
"Job vacancies, payroll employees, and job vacancy rate by industry sector, monthly, unadjusted for seasonality" = cansim::get_cansim("1410037201"),
"Hours worked (actual in reference week)" = cansim::get_cansim("1410030001"),
"Hours worked (actual in reference week)" = cansim::get_cansim("1410003601"),
"Hours worked (actual, main job in reference week)" = cansim::get_cansim("1410028902"),
"Labour market tightness_Unemployment by CMA" = cansim::get_cansim("1410038001"),
"Labour market tightness_Unemployment by economic region" = cansim::get_cansim("1410038702"),
"Labour market tightness_Unemployment by NOCS" = cansim::get_cansim("1410029601"),
"Labour market tightness_Unemployment RATE by NAICS" = cansim::get_cansim("1410029102"),
"Labour market tightness_Job vacancies by economic region" = cansim::get_cansim("1410039801"),
"Labour market tightness_Job vacancies by NAICS" = cansim::get_cansim("1410040001"),
"Labour market tightness_Job vacancies by NOCS" = cansim::get_cansim("1410039901"),
"Fixed weighted index of average hourly earnings for all employees, by NAICS industry (year-over-year % change)" = cansim::get_cansim("1410021301"),
"Average weekly earnings by industry, monthly, unadjusted for seasonality" = cansim::get_cansim("1410020301")
)

# COMMAND ----------

head(Work_force[[1]],5)

# COMMAND ----------

Business_activity %>%
  names(.) %>%
  purrr::walk(~ write_csv(Business_activity[[.]], paste0("/dbfs/mnt/bdl-lde/Dashboard_Deloitte/Data_for_Deloitte/Business_activity/", ., ".csv")))

# COMMAND ----------

Business_snapshot %>%
  names(.) %>%
  purrr::walk(~ write_csv(Business_snapshot[[.]], paste0("/dbfs/mnt/bdl-lde/Dashboard_Deloitte/Data_for_Deloitte/Business_snapshot/", ., ".csv")))

# COMMAND ----------

Work_force %>%
  names(.) %>%
  purrr::walk(~ write_csv(Work_force[[.]], paste0("/dbfs/mnt/bdl-lde/Dashboard_Deloitte/Data_for_Deloitte/Work_force/", ., ".csv")))

# COMMAND ----------

Temp_data = list("Gross domestic product (GDP) at basic prices, by industry, monthly" = cansim::get_cansim("36100434", language = "french"),
                 "Gross domestic product (GDP) at basic prices, by industry, provinces and territories" = cansim::get_cansim("36100402", language = "french"),
                 "Experimental indexes of economic activity in the provinces and territories" = cansim::get_cansim("36100633", language = "french"),
                 "Experimental estimates for business openings and closures for Canada, provinces and territories, census metropolitan areas, seasonally adjusted" = cansim::get_cansim("33100270", language = "french"))


# COMMAND ----------

Temp_data %>%
  names(.) %>%
  purrr::walk(~ write_csv(Temp_data[[.]], paste0("/dbfs/mnt/bdl-lde/Dashboard_Deloitte/Data_for_Deloitte/Temp_data_french/", ., ".csv")))
