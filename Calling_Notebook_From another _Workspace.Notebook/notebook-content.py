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
# META       "default_lakehouse_workspace_id": "6d2b74ce-60f3-410a-842c-2414e6b8405f",
# META       "known_lakehouses": [
# META         {
# META           "id": "46959508-6c0c-4deb-a899-634684e7a191"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
from notebookutils import mssparkutils

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print(mssparkutils.notebook.run("02Fabric-Pyspark_Practice/Function_Practice_1"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

mssparkutils.notebook.run("Function_Practice_1", 900, {"guid": "8081e6fc-6cfb-4bf0-bebe-9cf613ce71f4"})

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

mssparkutils.notebook.run("Function_Practice_1", 90,"8081e6fc-6cfb-4bf0-bebe-9cf613ce71f4")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************



# Define the path to the notebook in the other workspace
notebook_path ="/synfs/nb_resource"  # Update this to the correct path

# Optionally, define parameters to pass to the target notebook
parameters = {
    file_path : "abfss://6d2b74ce-60f3-410a-842c-2414e6b8405f@onelake.dfs.fabric.microsoft.com/46959508-6c0c-4deb-a899-634684e7a191/Files/dimension_customer.csv",  # Replace with the actual path
filter_column : "Customer",  # Replace with the actual column to filter on
filter_value : "Unknown"  
}

# Run the notebook and capture the result
try:
    result = mssparkutils.notebook.run(notebook_path, 60, parameters)
    print("Notebook executed successfully!")
    print("Result:", result)
except Exception as e:
    print("An error occurred while running the notebook:", e)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************



# Define the path to the notebook in the other workspace
notebook_path ="/synfs/nb_resource"  # Update this to the correct path


# Run the notebook and capture the result
try:
    result = mssparkutils.notebook.run(notebook_path, 120)
    print("Notebook executed successfully!")
    print("Result:", result)
except Exception as e:
    print("An error occurred while running the notebook:", e)

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
