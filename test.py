from pyspark.sql import SparkSession
import sqlite3
import pandas as pd

# spark = SparkSession.builder \
#     .appName("ReadParquet") \
#     .getOrCreate()

# df = spark.read.parquet("Calendar.parquet")
df = pd.read_parquet("Calendar.parquet")
conn = sqlite3.connect("Calendar.db")

# df.to_sql(
#     name="Calendar",        # Table name
#     con=conn,
#     if_exists="replace", # Options: replace, append, fail
#     index=False
# )
query = "SELECT * FROM Calendar LIMIT 5"
result = pd.read_sql(query, conn)

print(result)

# import pandas as pd
# import sqlite3

# df = pd.read_parquet("Sales.parquet")
# df.head(10485).to_excel("Sales.xlsx", index=False)
# conn = sqlite3.connect("sales.db")
# df.to_sql(
#     name="sales",        # Table name
#     con=conn,
#     if_exists="replace", # Options: replace, append, fail
#     index=False
# )
# print(df.dtypes)
# df["StartDate"] = df["StartDate"].astype("datetime64[us]")
# df["EndDate"] = df["EndDate"].astype("datetime64[us]")
# print(df.dtypes)
# df.to_parquet(
#     "Promotion_fixed.parquet",
#     engine="pyarrow"
# )

# print(df.show())

# df.printSchema()

# import pyarrow as pa
# import pyarrow.parquet as pq

# # Read the original file
# table = pq.read_table("Calendar.parquet")

# # Convert DateKey from nanoseconds to microseconds
# idx = table.schema.get_field_index("DateKey")

# date_col = table.column(idx).cast(pa.timestamp("us"))

# table = table.set_column(
#     idx,
#     "DateKey",
#     date_col
# )

# # Write a new Parquet file
# pq.write_table(table, "Calendar_fixed.parquet")