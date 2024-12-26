# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "46959508-6c0c-4deb-a899-634684e7a191",
# META       "default_lakehouse_name": "LakehouseDemo1",
# META       "default_lakehouse_workspace_id": "6d2b74ce-60f3-410a-842c-2414e6b8405f"
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
import sempy.fabric as fabric 
dataset = "test_06"
workspace = "01-Fabric"

# Objects to refresh, define using a dictionary
objects_to_refresh = [
    {
        "table": "Customer"
  }
    
]

# Refresh the dataset
fabric.refresh_dataset(
    workspace=workspace,
    dataset=dataset, 
    objects=objects_to_refresh,
)

# List the refresh requests
fabric.list_refresh_requests(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
