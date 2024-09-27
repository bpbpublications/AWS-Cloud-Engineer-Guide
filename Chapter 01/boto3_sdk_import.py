#Import Boto3 SDK Module example to create S3 bucket

import boto3
s3=boto3.client('s3')
s3.create_bucket(Bucket='my-bucket')









