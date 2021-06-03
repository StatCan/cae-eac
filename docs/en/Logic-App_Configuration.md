# How to Configure a Logic App to Auto-Terminate a Cluster on Databricks-XYZ

1. Select a cluster and on the configuration page uncheck the box for "terminate after X minutes of inactivity".

<img src="images\logic_autoterminate.png" alt="Auto Terminate" width="75%"/>

2. Clone the "**recurrence-trigger-to-deallocate-VRF-cluster**" logic app on Azure portal and name the new logic app "**recurrence-trigger-to-deallocate-XYZ-cluster**".
   
3. In the logic app designer of the new logic app, update the **databricksInstance** and **workspaceName** (located in the HTTP step) with the Databricks-XYZ properties. Also check to ensure the **resourceGroup** is correct as well.

<img src="images\logic_designer.png" alt="Logc App Designer" width="75%"/>

4. Enable system assigned identity.

<img src="images\logic_identity.png" alt="Logic App Identity Assignment" width="75%"/>

5. Add a new access policy for the newly created logic app to **CAE-Admin-Secrets**. You only need to grant **GET** Secrets Permission on the keyvault.

<img src="images\logic_keyvaultpermissions.png" alt="Keyvault Permissions" width="75%"/>

6. Create a CLOUD jira ticket to grant permission to "**databricks-api-client-sp**" as a contributor to your Databricks-XYZ (See CLOUD-7451 for reference).

---
**NOTE**: "recurrence-trigger-to-deallocate-*XYZ*-cluster" logic apps call a primary logic app "**create-list-and-deallocate-clusters**" to perform the actual deallocation. This app fetches the entire list of clusters on the databrick and stops all of them. Because of this, it is possible that your newly created app may be running succesfully but the called app is failing. Therefore, always check both apps' run history to confirm they are both succeeding.

Also note, if the databrick to run the logic app on contains no clusters, running or otherwise, "**create-list-and-deallocate-clusters**" will fail when called. 

---