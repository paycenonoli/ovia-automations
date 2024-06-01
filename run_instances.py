import boto3
client = boto3.client('ec2')

response = client.run_instances(
    ImageId='ami-09040d770ffe2224f',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,  
)
