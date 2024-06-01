import boto3
client = boto3.client('ec2')

response = client.terminate_instances(
    InstanceIds=[
        'i-0a6a8214a16e728ed',
    ]
)