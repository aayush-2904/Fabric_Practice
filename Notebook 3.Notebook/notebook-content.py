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
import sempy_labs as labs
dataset = 'test_06' # Enter your dataset name
workspace = '01-Fabric' # Enter your workspace name (if set to None it will use the workspace in which the notebook is running)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************



fabric.refresh_dataset(
    workspace = workspace,
    dataset = dataset,
    refresh_type = 'full',
    apply_refresh_policy = 'false'
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

labs.refresh_semantic_model(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = labs.refresh_semantic_model(dataset=dataset, workspace=workspace, visualize=True)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

labs.refresh_semantic_model(dataset=dataset, workspace=workspace, tables=['Customer'])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


fabric.list_refresh_requests(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

labs.get_semantic_model_refresh_history(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

labs.get_semantic_model_refresh_history(dataset=dataset, workspace=workspace)

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
