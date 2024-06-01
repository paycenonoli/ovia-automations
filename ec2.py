import boto3

# Initialize a session using Amazon EC2
client = boto3.client('ec2')

# Retrieve  a list of ec2 instances
response = client.describe_instances()

# Extract instance IDs
instance_ids = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance["InstanceId"])

    
print(instance_ids)
