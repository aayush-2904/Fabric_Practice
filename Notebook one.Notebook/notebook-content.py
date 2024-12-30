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

from pyspark.sql import SparkSession
from pyspark.sql.functions import when

# Create Spark session
spark = SparkSession.builder \
    .appName("Customer Categorization") \
    .getOrCreate()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

customer_df = spark.read.format("delta").load("abfss://6d2b74ce-60f3-410a-842c-2414e6b8405f@onelake.dfs.fabric.microsoft.com/46959508-6c0c-4deb-a899-634684e7a191/Tables/Customer")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

customer_df = customer_df.withColumn(
    "Category6",
    when(customer_df.Age < 28, "Young").otherwise("Old")
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

customer_df.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Write updated DataFrame back to the Customer table
customer_df.write.format("delta").mode("append").option("mergeSchema", "true").save("abfss://6d2b74ce-60f3-410a-842c-2414e6b8405f@onelake.dfs.fabric.microsoft.com/46959508-6c0c-4deb-a899-634684e7a191/Tables/Customer")


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
