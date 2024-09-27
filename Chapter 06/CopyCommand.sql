--Copy command example to load data into Redshift

COPY schema_name.table_name
FROM 's3://bucket_name/object_key'
IAM_ROLE 'arn:aws:iam::1234567890:role/RedshiftRole'
FORMAT CSV
IGNOREHEADER 1;
