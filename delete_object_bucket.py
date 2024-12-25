import boto3
from botocore.exceptions import ClientError


def delete_object(bucket_name, object_key):
    s3_client = boto3.client('s3')
    try:
        s3_client.delete_object(
            Bucket=bucket_name,
            Key=object_key
        )
        print(f"Successfully deleted {object_key}")
        return True
    except ClientError as e:
        print(f"Error deleting object: {e}")
        return False


my_bucket = 'co.in.itreach-raj2'

# Delete single object
delete_object(my_bucket, 'error_whizlab.png')
