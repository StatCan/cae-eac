
# Artifactory

The CAE environment uses the Artifiactory for package & library management.


## Included packages

Below are the URLs that Artifactory pulls from currently. As long as the package is available on these repositories, it can be downloaded. You can get the name of the package by searching through the repositories.

  - [Conda-forge](https://conda.anaconda.org/conda-forge)
  - [CRAN](https://cran.r-project.org) (In the left menu, click **Packages** under **Software**, then click **Table of available packages**)
  - [Python](https://pypi.org/)
  
The respective artifactory URLs to use are:
  - https://jfrog.aaw.cloud.statcan.ca/artifactory/conda-forge-remote/
  - https://jfrog.aaw.cloud.statcan.ca/artifactory/dev-cran-remote/
  - https://jfrog.aaw.cloud.statcan.ca/artifactory/pypi-remote/
  
**Note**: For any other packages, please contact the **Collaborative Analytics Environment** team.


## Azure DataBricks

The packages can be installed from the Databricks workspace, a Databricks cluster or Databricks notebooks.

 **Note**: 
 - The library sources available in Databricks are **PyPI** for Python packages and **CRAN** for CRAN packages.
 - The artifactory URLs to use depending on the selected library source are:
    - https://jfrog.aaw.cloud.statcan.ca/artifactory/pypi-remote/ for **PyPI**
    - https://jfrog.aaw.cloud.statcan.ca/artifactory/dev-cran-remote/  for **CRAN**
    
    

### From Databricks workspace

1.From the main page, click **Import Library**.

![Databricks](images/Artifactory-DBricks01.png)

2. Under **Library Source**, choose either **PyPI** or **CRAN** depending of the package.

3. Paste the name of the library under **Package** and the associated Artifactory URL (See Note above) under **Repository**.

![Databricks](images/Artifactory-DBricks02.PNG)

4. Click **Create**.

**Note**: Select **Install automatically on all cluster** under **Admin settings** if you wish to install the package on all the available clusters of the workspace.

### From a Databricks cluster

1.From the cluster main page, click **Install new** under **Libraries**.

![Cluster](images/Artifactory-Cluster01.png)

2. Under **Library Source**, choose either **PyPI** or **CRAN** depending of the package.

3. Paste the name of the library under **Package** and the associated Artifactory URL (See Note above) under **Repository**.

![Cluster](images/Artifactory-Cluster02.PNG)

4. Click **Install**. You should see the newly installed library under **Libraries**.

![Cluster](images/Artifactory-Cluster03.PNG)

**Note** : If you don't have permission to install libraries from the workspace or cluster, please contact the **Collaborative Analytics Environment** team.

### From Databricks Notebooks
### Python notebook
1. From your Python notebook, run the following code to setup pip to download packages from Artifactory repositories.

```
%sh
pip config --user set global.index-url https://jfrog.aaw.cloud.statcan.ca/artifactory/api/pypi/pypi-remote/simple
```

![Configure VSC](images/Artifactory-PyNNotebooks01.png)

2. You can now use **pip3** or **pip** command to install packages as following:

```
%sh
pip3 install <PackageName>
```
![Install VSCpackage](images/Artifactory-PyNNotebooks02.png)

### R notebook
1. From your R notebook, run the following code to download packages from Artifactory repositories.

```
install.packages('<PackageName>', repos='https://jfrog.aaw.cloud.statcan.ca/artifactory/dev-cran-remote', dependencies=TRUE)
```
![Install VSCpackage](images/Artifactory-RNotebooks01.png)

## Azure Machine Learning

The packages can be installed from the terminal using Python commands.

1. From the main page, click **Notebooks**, then click **Open Terminal** under **Files**.
 ![Open terminal](images/AzureML_11.png)  
 
2. Select the **compute instance** assigned to you from the drop-down next to Compute.

   *If a compute instance has not been created for you, please contact the  **Collaborative Analytics Environment** team.*
 
3. Run the following code to setup pip to download packages from Artifactory repositories.

```
pip config --user set global.index-url https://jfrog.aaw.cloud.statcan.ca/artifactory/api/pypi/pypi-remote/simple
```

![Configure pip.conf](images/Artifactory-AzureML02.png)

4. You can now use **pip3** or **pip** command to install packages as following:

```
pip3 install <PackageName>
```
![install package](images/Artifactory-AzureML03.png)


## Azure Synapse

Please contact the **Collaborative Analytics Environment** team to install custom packages in your Azure Synapse environment.

## Visual Studio Code
1.From the **Extensions** tab, click **Terminal**, then click **New Terminal**.
![Visual Studio Code](images/Artifactory-VS01.png)

2. Run the following code to setup pip to download packages from Artifactory repositories.

```pip config --user set global.index-url https://jfrog.aaw.cloud.statcan.ca/artifactory/api/pypi/pypi-remote/simple```

![Configure VSC](images/Artifactory-VSC01.png)

3. You can now use **pip3* or **pip** command to install packages as following:

```pip3 install <PackageName>```

![Install VSCpackage](images/Artifactory-VSC02.png)


## RStudio
1. From the RStudio console, run the following code to configure the *Rprofile.site* file to use the Artifactory repositories.

``` 
options(repos = c(artifactory = "https://jfrog.aaw.cloud.statcan.ca/artifactory/dev-cran-remote/"))
```

![Configure Rstudio](images/Artifactory-RStudio01.png)

2. Under **Packages**, click "Install". Choose the new repository that you added in step 1 and enter the package name to install.

![Install Rstudio](images/Artifactory-RStudio02.png)

OR

Run the following command to avoid the steps 1 and 2.
```
install.packages('<PackageName>', repos='https://jfrog.aaw.cloud.statcan.ca/artifactory/dev-cran-remote', dependencies=TRUE)
```

3. You should see the installed package in the **System Library list**.

![Rstudio packages](images/Artifactory-RStudio03.png)

### R Console
1. Run the following code to configure the *Rprofile.site* file to use the Artifactory repositories.

```
options(repos = c(artifactory = "https://jfrog.aaw.cloud.statcan.ca/artifactory/dev-cran-remote/"))
```

2. Under **Packages**, click **Install Package**, choose the package you want to install, then click **Install**

![R packages](images/Artifactory-RStudio04.png)

OR
Run the following code command to install packages.
```
install.packages('<PackageName>', repos='https://jfrog.aaw.cloud.statcan.ca/artifactory/dev-cran-remote', dependencies=TRUE)
```
### Warning
The configuration of the *Rprofile.site* file is temporary and only last your session. Once you close RStudio or the R Console, the settings reset to the default ones, so you have to run the code of the step 1 again.



## Azure Cloud Virtual Machine

### Miniforge Prompt
1. Run the following code to setup pip to download packages from Artifactory repositories.

```
pip config --user set global.index-url https://jfrog.aaw.cloud.statcan.ca/artifactory/api/pypi/pypi-remote/simple
```

![Configure VSC](images/Artifactory-Miniforge01.png)

2. You can now use **pip3** or **pip** command to install packages as following:

```
pip3 install <PackageName>
```

![Install VSCpackage](images/Artifactory-Miniforge02.png)

### Command Prompt
1. Run the following code to setup pip to download packages from Artifactory repositories.

```
pip config --user set global.index-url https://jfrog.aaw.cloud.statcan.ca/artifactory/api/pypi/pypi-remote/simple
```

![Configure VSC](images/Artifactory-Terminal01.png)

2. You can now use **pip3** or **pip** command to install packages as following:

```
pip3 install <PackageName>
```

![Install VSCpackage](images/Artifactory-Python02.png)

### Python application
You can use the Command Prompt to install packages, then import them into the Python notebooks as the following scenario:

1. Let's try to access this non-installed module’s contents with the **import** statement.

![Check library](images/Artifactory-Python01.png)

2. Now let's install it from the **Command Prompt**.
 *See Command Prompt section of this document if the pip.ini file hasn't been configured before*
 
![install library](images/Artifactory-Python02.png)

3. The module can now be imported.

![import library](images/Artifactory-Python03.png)

### Warning
The configuration of the *pip.ini* file is temporary. Once you Virtual Machine, the settings reset to the default ones, so you have to run the code of the step 1 again.

## Download Packages locally

To download packages locally, you can use the **Curl** or **pip download** commands as following:

```
curl -O "https://jfrog.aaw.cloud.statcan.ca/artifactory/cae-generic-test/<PackageName>"
```

```
pip download <package_url>
```
