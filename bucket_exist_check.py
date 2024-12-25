import boto3
from botocore.exceptions import ClientError
#import pprint


def check_bucket_exists(bucket_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        error_code = e.response['Error']['code']
        if error_code == '404':  # Not Found
            return False
        elif error_code == '403':  # Forbidden
            return False  # Bucket exists but you don't have access
        raise  # Re-raise other errors


def list_bucket_objects(bucket_name):
    """
    List objects in a bucket, optionally filtering by prefix
    """
    s3_client = boto3.client('s3')
    try:
        response = s3_client.list_objects_v2(
            Bucket=bucket_name,

        )
        if 'Contents' in response:
            return response['Contents']
        return []
    except ClientError as e:
        print(f"Error: {e}")
        return []


my_bucket = 'co.in.itreach-raj2'
exists = check_bucket_exists(my_bucket)
if exists:
    print(f"Bucket {my_bucket} exist")
else:
    print(f"Bucket {my_bucket} does not exist")

for oj in list_bucket_objects(my_bucket):
    file_name = oj['Key']
    file_size = oj['Size']
    print(f"File: {file_name}, Size: {file_size} bytes")


















