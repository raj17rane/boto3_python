import boto3
import logging


client = boto3.client('s3')


response = client.list_buckets()

try:
    if response:
        assert isinstance(response, object)
        print(response)
except Exception as e:
    logging.error(e)
    print("No no bucket list")

