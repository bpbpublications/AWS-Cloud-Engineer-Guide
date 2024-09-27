--Create External Schema

CREATE EXTERNAL SCHEMA <schema_name>
FROM DATA CATALOG DATABASE '<database_name>'
IAM_ROLE '<IAM_role_ARN>'
CREATE EXTERNAL DATABASE IF NOT EXISTS;


--Create External Table

CREATE EXTERNAL TABLE <table_name>
(
column1 data_type,
column2 data_type,
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://<bucket_name>/<path_to_data_files>/'
;


--Query External Spectrum Table

SELECT column1, column2
FROM <schema_name>.<table_name>
WHERE condition;
