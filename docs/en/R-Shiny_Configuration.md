# How to Install RStudio Server Open Source and R-Shiny Package on an Azure Databricks cluster

The documentation is available at:

[https://docs.microsoft.com/en-ca/azure/databricks/spark/latest/sparkr/rstudio](https://docs.microsoft.com/en-ca/azure/databricks/spark/latest/sparkr/rstudio)

---
**NOTE**: If cluster is using runtime version 7.0 **ML** or above, rstudio-server is already installed and configured and you can skip these instructions up to 5. If using version 7.0 or above **non-ML**, rstudio-server is also pre-installed however these steps may need to be followed so as to have the program run on cluster start. Check the rstudio tab on the running cluster's screen to confirm if it has been enabled or not.

---
<br/>

1. Ensure that the cluster is not auto-terminating by unselecting the checkbox on the main configuration page of the cluster.

1. Create an init script to install the RStudio Server Open Source binary package. If you are using a runtime version below 7.0, the rstudio-server package needs to be fetched and installed, as shown in the documentation: [Cluster-scoped init scripts](https://docs.microsoft.com/en-ca/azure/databricks/clusters/init-scripts#cluster-scoped-init-script). If not, you should only need to ensure the rstudio-server program exists on the system and is started when the cluster starts. Here is an example notebook cell that installs an init script on a location on DBFS:

```
script = """#!/bin/bash

set -euxo pipefail
RSTUDIO\_BIN="/usr/sbin/rstudio-server"

if [[! -f "$RSTUDIO\_BIN" && $DB\_IS\_DRIVER = "TRUE"]]; then
    apt-get update
    rstudio-server restart || true
fi
"""

dbutils.fs.mkdirs("/databricks/rstudio")
dbutils.fs.put("/databricks/rstudio/rstudio-install.sh", script, True)
```

2. Run the code in a notebook to install the script at dbfs:/databricks/rstudio/rstudio-install.sh

3. Before launching a cluster add dbfs:/databricks/rstudio/rstudio-install.sh as an init script. This can be done from the cluster configuration page under *Advanced Options*, then select *Init Scripts*. See [Diagnostic logs](https://docs.microsoft.com/en-ca/azure/databricks/clusters/init-scripts#cluster-scoped-init-script) for details.

4. Launch the cluster.

5. Go to Libraries tab and select 'Install new library'. Select CRAN as the source and enter the library name "shiny", repo can be left blank.