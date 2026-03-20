# utils/functions.py
def ingest_to_bronze(spark,file_path, table_name):
    try:
       print(f"--- in process: {table_name} ---")
       df = spark.read.format("csv") \
          .option("header", "false") \
          .option("inferSchema", "true") \
          .load(file_path)
    
       df.write.format("delta") \
        .mode("overwrite") \
        .saveAsTable(f"db_project_divvy_bronze.{table_name}")
    
       print(f"---completed: {table_name} ---")


    except Exception as e:

        print(f"Error: {e}")