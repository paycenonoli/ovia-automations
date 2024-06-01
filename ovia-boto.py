import boto3

instance = boto3.client('ec2', region_name='us-east-2')

instance_ids = ["i-075ccfcc1b269235f", "i-04f6cd0661f6a2d96"]

instance.start_instances(InstanceIds=instance_ids)