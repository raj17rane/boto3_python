import boto3
from botocore.exceptions import ClientError

def delete_bucket(bucket_name):
    """
    Delete an empty S3 bucket
    """
    s3_client = boto3.client('s3')
    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Successfully deleted bucket: {bucket_name}")
        return True
    except ClientError as e:
        print(f"Error deleting bucket: {e}")
        return False

# Function to delete bucket and all its contents
def delete_bucket_and_contents(bucket_name):
    """
    Delete a bucket and all its contents
    """
    s3_client = boto3.client('s3')

    try:
        # First delete all objects and versions
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            if 'Contents' in page:
                objects = [{'Key': obj['Key']} for obj in page['Contents']]
                s3_client.delete_objects(
                    Bucket=bucket_name,
                    Delete={'Objects': objects}
                )

        # Delete versioned objects if versioning is enabled
        paginator = s3_client.get_paginator('list_object_versions')
        for page in paginator.paginate(Bucket=bucket_name):
            versions = []
            if 'Versions' in page:
                versions += [{'Key': v['Key'], 'VersionId': v['VersionId']}
                           for v in page['Versions']]
            if 'DeleteMarkers' in page:
                versions += [{'Key': d['Key'], 'VersionId': d['VersionId']}
                           for d in page['DeleteMarkers']]
            if versions:
                s3_client.delete_objects(
                    Bucket=bucket_name,
                    Delete={'Objects': versions}
                )

        # Finally delete the bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Successfully deleted bucket and all contents: {bucket_name}")
        return True

    except ClientError as e:
        print(f"Error deleting bucket: {e}")
        return False

# Example usage
bucket_name = 'co.in.itreach-raj4'
delete_bucket_and_contents(bucket_name)
