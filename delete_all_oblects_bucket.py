import boto3
from botocore.exceptions import ClientError


def delete_all_objects(bucket_name, prefix=''):
    s3_client = boto3.client('s3')
    try:
        # List all objects
        paginator = s3_client.get_paginator('list_objects_v2')

        # Delete objects in batches
        for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
            if 'Contents' not in page:
                continue

            objects_to_delete = [{'Key': obj['Key']} for obj in page['Contents']]

            # Delete the batch of objects
            s3_client.delete_objects(
                Bucket=bucket_name,
                Delete={
                    'Objects': objects_to_delete,
                    'Quiet': True
                }
            )

        print(f"Successfully deleted all objects from {bucket_name} with prefix {prefix}")
        return True
    except ClientError as e:
        print(f"Error: {e}")
        return False


my_bucket = 'co.in.itreach-raj4'

delete_all_objects(my_bucket)
