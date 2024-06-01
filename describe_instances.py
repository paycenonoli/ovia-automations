import boto3
from pprint import pprint
client = boto3.client('ec2')

response = client.describe_instances()['Reservations']
for each_instance in response:
    for value in each_instance['Instances']:
        print(value['InstanceId'])