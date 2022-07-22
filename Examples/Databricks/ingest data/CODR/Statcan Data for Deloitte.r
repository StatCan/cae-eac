# Databricks notebook source
#install.packages("cansim")
library(cansim)
library(tidyverse)

# COMMAND ----------

Business_snapshot = list("Raw_33100270_en" = cansim::get_cansim("33100270", language = "en"),
                         "Raw_33100270_fr" = cansim::get_cansim("33100270", language = "fr"))

# COMMAND ----------

Business_Activity = list("Raw_33100270_en" = cansim::get_cansim("33100270", language = "en"),
                         "Raw_36100434_en" = cansim::get_cansim("36100434", language = "en"),
                         "Raw_36100402_en" = cansim::get_cansim("36100402", language = "en"),
                         "Raw_36100633_en" = cansim::get_cansim("36100633", language = "en"),
                         "Raw_14100355_en" = cansim::get_cansim("14100355", language = "en"),
                         "Raw_14100379_en" = cansim::get_cansim("14100379", language = "en"),
                         "Raw_14100067_en" = cansim::get_cansim("14100067", language = "en"),
                         "Raw_14100380_en" = cansim::get_cansim("14100380", language = "en"),
                         "Raw_14100292_en" = cansim::get_cansim("14100292", language = "en"),
                         "Raw_14100387_en" = cansim::get_cansim("14100387", language = "en"),
                         "Raw_14100325_en" = cansim::get_cansim("14100325", language = "en"),
                         "Raw_14100326_en" = cansim::get_cansim("14100326", language = "en"),
                         "Raw_14100371_en" = cansim::get_cansim("14100371", language = "en"),
                         "Raw_14100372_en" = cansim::get_cansim("14100372", language = "en"),
                         "Raw_14100223_en" = cansim::get_cansim("14100223", language = "en"),
                         "Raw_14100213_en" = cansim::get_cansim("14100213", language = "en"),
                         "Raw_36100104_en" = cansim::get_cansim("36100104", language = "en"),
                         "Raw_3610010801_en" = cansim::get_cansim("3610010801", language = "en"),
                         "Raw_33100226_en" = cansim::get_cansim("33100226", language = "en"),
                         "Raw_33100398_en" = cansim::get_cansim("33100398", language = "en")
                       )



# COMMAND ----------

Business_Activity_fr = list(  "Raw_33100270_fr" = cansim::get_cansim("33100270", language = "fr"),
                         "Raw_36100434_fr" = cansim::get_cansim("36100434", language = "fr"),
                         "Raw_36100402_fr" = cansim::get_cansim("36100402", language = "fr"),
                         "Raw_36100633_fr" = cansim::get_cansim("36100633", language = "fr"),
                         "Raw_14100355_fr" = cansim::get_cansim("14100355", language = "fr"),
                         "Raw_14100379_fr" = cansim::get_cansim("14100379", language = "fr"),
                         "Raw_14100067_fr" = cansim::get_cansim("14100067", language = "fr"),
                         "Raw_14100380_fr" = cansim::get_cansim("14100380", language = "fr"),
                         "Raw_14100292_fr" = cansim::get_cansim("14100292", language = "fr"),
                         "Raw_14100387_fr" = cansim::get_cansim("14100387", language = "fr"),
                         "Raw_14100325_fr" = cansim::get_cansim("14100325", language = "fr"),
                         "Raw_14100326_fr" = cansim::get_cansim("14100326", language = "fr"),
                         "Raw_14100371_fr" = cansim::get_cansim("14100371", language = "fr"),
                         "Raw_14100372_fr" = cansim::get_cansim("14100372", language = "fr"),
                         "Raw_14100223_fr" = cansim::get_cansim("14100223", language = "fr"),
                         "Raw_14100213_fr" = cansim::get_cansim("14100213", language = "fr"),
                         "Raw_36100104_fr" = cansim::get_cansim("36100104", language = "fr"),
                         "Raw_3610010801_fr" = cansim::get_cansim("3610010801", language = "fr"),
                         "Raw_33100226_fr" = cansim::get_cansim("33100226", language = "fr"),
                         "Raw_33100398_fr" = cansim::get_cansim("33100398", language = "fr"))

# COMMAND ----------

Work_force = list("Raw_1410038001_en" = cansim::get_cansim("1410038001",language = "en"),
                  "Raw_1410035501_en" = cansim::get_cansim("1410035501",language = "en"),
                  "Raw_1410034201_en" = cansim::get_cansim("1410034201",language = "en"),
                  "Raw_1410007701_en" = cansim::get_cansim("1410007701",language = "en"))
                  

# COMMAND ----------

Work_force_0=list( "Raw_1410040001_en" = cansim::get_cansim("1410040001",language = "en"),
                  "Raw_1410039901_en" = cansim::get_cansim("1410039901",language = "en"),
                  "Raw_1410039801_en" = cansim::get_cansim("1410039801",language = "en"),
                  "Raw_1410037101_en" = cansim::get_cansim("1410037101",language = "en"),
                  "Raw_1410037201_en" = cansim::get_cansim("1410037201",language = "en"))
                 

# COMMAND ----------

Work_force_1 = list( "Raw_1410030001_en" = cansim::get_cansim("1410030001",language = "en"),
                  "Raw_1410003601_en" = cansim::get_cansim("1410003601",language = "en"),
                  "Raw_1410028902_en" = cansim::get_cansim("1410028902",language = "en"),
                  "Raw_1410038001_en" = cansim::get_cansim("1410038001",language = "en"))

# COMMAND ----------

Work_force_2 = list( "Raw_1410038702_en" = cansim::get_cansim("1410038702",language = "en"),
                  "Raw_1410029601_en" = cansim::get_cansim("1410029601",language = "en"),
                  "Raw_1410029102_en" = cansim::get_cansim("1410029102",language = "en"),
                  "Raw_1410039801_en" = cansim::get_cansim("1410039801",language = "en"),
                  "Raw_1410040001_en" = cansim::get_cansim("1410040001",language = "en"))

# COMMAND ----------

Work_force_3 = list("Raw_1410039901_en" = cansim::get_cansim("1410039901",language = "en"),
                  "Raw_1410021301_en" = cansim::get_cansim("1410021301",language = "en"),
                  "Raw_1410020301_en" = cansim::get_cansim("1410020301",language = "en"),
                  "Raw_1410032201_en" = cansim::get_cansim("1410032201",language = "en"),
                  "Raw_9810005701_en" = cansim::get_cansim("9810005701",language = "en"))

# COMMAND ----------

Work_force_4 = list(  "Raw_9810005801_en" = cansim::get_cansim("9810005801",language = "en"),
                  "Raw_9810009601_en" = cansim::get_cansim("9810009601",language = "en"),
                  "Raw_9810009701_en" = cansim::get_cansim("9810009701",language = "en"),
                  "Raw_9810010601_en" = cansim::get_cansim("9810010601",language = "en"),
                  "Raw_9810010701_en" = cansim::get_cansim("9810010701",language = "en"))

# COMMAND ----------

#Separate list is created due to memory issues

Work_force_fr = list("Raw_1410038001_fr" = cansim::get_cansim("1410038001",language = "fr"),
                     "Raw_1410035501_fr" = cansim::get_cansim("1410035501",language = "fr"),
                     "Raw_1410034201_fr" = cansim::get_cansim("1410034201",language = "fr"),
                     "Raw_1410007701_fr" = cansim::get_cansim("1410007701",language = "fr"),
                     "Raw_1410040001_fr" = cansim::get_cansim("1410040001",language = "fr"))

# COMMAND ----------

#Memory issue fix
Work_force_fr_0 = list("Raw_1410039901_fr" = cansim::get_cansim("1410039901",language = "fr"),
                     "Raw_1410039801_fr" = cansim::get_cansim("1410039801",language = "fr"),
                     "Raw_1410037101_fr" = cansim::get_cansim("1410037101",language = "fr"),
                     "Raw_1410037201_fr" = cansim::get_cansim("1410037201",language = "fr"),
                     "Raw_1410030001_fr" = cansim::get_cansim("1410030001",language = "fr"),
                     "Raw_1410003601_fr" = cansim::get_cansim("1410003601",language = "fr"))


# COMMAND ----------

#Memory issue fix
Work_force_fr_1 = list("Raw_1410028902_fr" = cansim::get_cansim("1410028902",language = "fr"),
                     "Raw_1410038001_fr" = cansim::get_cansim("1410038001",language = "fr"),
                     "Raw_1410038702_fr" = cansim::get_cansim("1410038702",language = "fr"),
                     "Raw_1410029601_fr" = cansim::get_cansim("1410029601",language = "fr"),
                     "Raw_1410029102_fr" = cansim::get_cansim("1410029102",language = "fr"),
                     "Raw_1410039801_fr" = cansim::get_cansim("1410039801",language = "fr"))

# COMMAND ----------

#Memory issue fix
Work_force_fr_2 = list( "Raw_1410040001_fr" = cansim::get_cansim("1410040001",language = "fr"),
                     "Raw_1410039901_fr" = cansim::get_cansim("1410039901",language = "fr"),
                     "Raw_1410021301_fr" = cansim::get_cansim("1410021301",language = "fr"),
                     "Raw_1410020301_fr" = cansim::get_cansim("1410020301",language = "fr"),
                     "Raw_1410032201_fr" = cansim::get_cansim("1410032201",language = "fr"),
                     "Raw_9810005701_fr" = cansim::get_cansim("9810005701",language = "fr"))

# COMMAND ----------

#Memory issue fix
Work_force_fr_3 = list( "Raw_9810005801_fr" = cansim::get_cansim("9810005801",language = "fr"),
                     "Raw_9810009601_fr" = cansim::get_cansim("9810009601",language = "fr"),
                     "Raw_9810009701_fr" = cansim::get_cansim("9810009701",language = "fr"),
                     "Raw_9810010601_fr" = cansim::get_cansim("9810010601",language = "fr"),
                     "Raw_9810010701_fr" = cansim::get_cansim("9810010701",language = "fr"))

# COMMAND ----------


Mobility = list(Raw_2410004901_en = cansim::get_cansim("2410004901", language = "en"),
                Raw_2410004901_fr = cansim::get_cansim("2410004901", language = "fr"))




# COMMAND ----------

Combined_list = c(Business_snapshot,Business_Activity,Work_force,Work_force_0,Work_force_1,Work_force_2,Work_force_3,Work_force_4,Work_force_fr,Work_force_fr_0,Work_force_fr_1,Work_force_fr_2,Work_force_fr_3,Mobility)

# COMMAND ----------

Combined_list %>%
  names(.) %>%
  purrr::walk(~ write_csv(Combined_list[[.]], paste0("/dbfs/mnt/bdl-lde/Datasets from all sources/Statcan/", ., ".csv")))

