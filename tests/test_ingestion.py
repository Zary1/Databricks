def test_table_exists(spark,table_name):
    # verify table exists
  if spark.catalog.tableExists(table_name):
    # verify if table has a row
    count = spark.table(table_name).count()
    if count > 0:
      print(f"Test OK: table {table_name} exists and has {count} rows")
      return True
    else:
      print(f"Test FAILED: table {table_name} exists but is empty")
      return False
  

 