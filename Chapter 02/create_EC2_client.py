#Create an EC2 client using the AWS SDK for Python - Boto3
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html

import boto3
# Specify your AWS credentials or use an IAM role with  appropriate permissions
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
region_name = 'your_region_name'  # e.g., 'us-east-1'

# Create an EC2 client
ec2_client = boto3.client(
    'ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)


 # Specify instance configuration
 
	instance_config = {
	'ImageId': 'ami-0c55b159cbfafe1f0',                   
	'InstanceType': 't2.micro',
	'KeyName': 'my-key-pair',            
	'SecurityGroupIds': ['sg-1234567890'] 
}


#Launch the instance
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html#run-instances
	# Create an EC2 instance with the specified configuration
	response = ec2_client.run_instances(**instance_config)

#Check the instance status
	# Describe the status of the instance
	response =ec2_client.describe_instances(InstanceIds=[instance_id])
	# Extract the instance state from the response 
	instance_state=response['Reservations'][0]['Instances'][0] ['State']['Name']
	# Print the instance state 
	print(f"The instance with ID {instance_ id} is currently in the state: {instance_state}") 

