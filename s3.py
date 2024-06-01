s3_client = boto3.client('s3')

bucket_name = 'ovia-aos-lambda'

# Retrieve a list of contents
response = s3_client.list_objects_v2(
    Bucket=bucket_name
)

# Extract objects
key = []

for content in response['Contents']:
    key.append(content['Key'])
    
print(key)