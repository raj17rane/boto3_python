import boto3
from botocore.exceptions import ClientError


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


my_bucket = 'co.in.itreach-raj4'
exists = check_bucket_exists(my_bucket)
if exists:
    print(f"Bucket {my_bucket} exist")
else:
    print(f"Bucket {my_bucket} does not exist")
