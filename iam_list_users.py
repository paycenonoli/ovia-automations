# Import all the modules and libraries
import boto3
from pprint import pprint
# Open the Management Console
aws_management_console = boto3.session.Session(profile_name="default")
# Open the iAM Console
iam_console = aws_management_console.client(service_name="iam")
# Use Boto3 Documentation to get more information
iam_client = boto3.client("iam")
response = iam_client.list_users()
for each_user in response['Users']:
    print(each_user['UserName'])