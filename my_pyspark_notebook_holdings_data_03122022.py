# Databricks notebook source
# MAGIC %md
# MAGIC HOLDINGS DATA

# COMMAND ----------

from pyspark.sql.functions import desc

# COMMAND ----------


holdings = spark.read.csv("/FileStore/tables/my_holdings_031222.csv",header='true')
display(holdings)


# COMMAND ----------

# DBTITLE 1,Collect method
holdings.collect()


# COMMAND ----------

# DBTITLE 1,EDA
holdings.describe().show()

# COMMAND ----------

holdings.show()

# COMMAND ----------

# DBTITLE 1,Rename
holdings = holdings.withColumnRenamed('Qty.', 'Quantity').withColumnRenamed('Avg. cost', 'Average').withColumnRenamed('Cur. val','Current').withColumnRenamed('P&L','Profit_Loss').withColumnRenamed('Net chg.','Net_change').withColumnRenamed('Day chg.','Day_change')

# COMMAND ----------

# DBTITLE 1,Filter
holdings.filter(holdings['Profit_Loss']<0).show()

# COMMAND ----------

# DBTITLE 1,Sorting
holdings.sort(desc(holdings.LTP)).show()
