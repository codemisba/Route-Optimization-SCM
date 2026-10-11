from pyspark.sql import SparkSession

# Postgres driver JAR file
# https://jdbc.postgresql.org/download/postgresql-42.7.1.jar

# Initialize Spark session
spark = SparkSession.builder \
    .appName("RouteOptimizationDataIngestion") \
    .master("local[*]") \
    .config("spark.driver.extraClassPath", "postgresql-42.7.1.jar") \
    .config("spark.executor.extraClassPath", "postgresql-42.7.1.jar") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.1") \
    .config("spark.jars.repositories", "https://repo1.maven.org/maven2/") \
    .config("spark.jars", "postgresql-42.7.1.jar") \
    .getOrCreate()

# PostgreSQL connection properties
url = "jdbc:postgresql://ep-broad-breeze-a1czee36-pooler.ap-southeast-1.aws.neon.tech/DRODB?sslmode=require"
properties = {
    "user": "neondb_owner",
    "password": "npg_6OQxq1nkRlwi",
    "driver": "org.postgresql.Driver"
}

# CSV paths and table names
csv_table_map = {
    "../Datasets/Raw/customer_data.csv": "customer_data",
    "../Datasets/Raw/delivery_driver_data.csv": "delivery_driver_data",
    "../Datasets/Raw/route_data.csv": "route_data",
    "../Datasets/Raw/vehicle_data.csv": "vehicle_data",
    "../Datasets/Raw/warehouse_data.csv": "warehouse_data"
}

# Read and write each file to Postgres
for file_path, table_name in csv_table_map.items():
    print(f"Reading: {file_path}")
    df = spark.read.option("header", True).csv(file_path)
    print(f"Writing to table: {table_name}")
    df.write.jdbc(url=url, table=table_name, mode="overwrite", properties=properties)

spark.stop()

print("Data ingestion completed.")