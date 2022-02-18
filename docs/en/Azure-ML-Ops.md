_[Français](../../fr/AML-MLOps)_

# Azure Machine Learning 
# Develop Machine Learning Models in Azure Machine Learning
[Access Your CAE Azure ML Workspace](AzureML.md)
## No Code Azure ML Tools ad Interfaces

### Azure ML Studio

### Azure Auto ML
### Azure ML Designer

## Python ML Model development 
### Create/Request a Compute Instance/Compute Cluster

### Create and Run Notebooks
While you can use the Notebooks page in Azure Machine Learning studio to run notebooks, it’s often more productive to use a more fully-featured notebook development environment like Jupyter. Azure Machine Learning compute instance includes an installation of Jupyter.

1. In Azure Machine Learning studio, view the Compute page for your workspace; and on the Compute Instances tab, start your compute instance if it is not already running.
2. When the compute instance is running, click the Jupyter link to open the Jupyter home page in a new browser tab. Be sure to open Jupyter and not JupyterLab.

Verify that that azureml-sdk and azureml-widgets are installed. Lunch a new Terminal and run
    - pip show azureml-sdk
    - pip show azureml-widgets
### Azure Machine Learning SDK

### Git and Github Integration 
Use Git and github to track, share and collaborate on ML model development code and GitHub Actions support to implement ML workflows.
# ML models Deployment Options In CAE

# Azure ML Learning Resources
1. Build and operate machine learning solutions with Azure Machine Learning (accessible from the DSVM) (https://docs.microsoft.com/en-ca/learn/paths/build-ai-solutions-with-azure-ml-service/)

2. Build and Operate Machine Learning Solutions with Azure
(https://www.coursera.org/learn/build-and-operate-machine-learning-solutions-with-azure)

# Practice Azure ML
1. Azure Machine Learning Exercises (Not accessible from the DSVM)
(https://microsoftlearning.github.io/mslearn-dp100/)