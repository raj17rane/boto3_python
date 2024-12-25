import boto3
import logging

s3_object = boto3.client('s3')
response =  s3_object.create_bucket(
                     CreateBucketConfiguration=dict(LocationConstraint='eu-west-1'),
                     Bucket='co.in.itreach-raj4'
              )


class ResponseMetadata:
    pass


try:
    if response:
        print(ResponseMetadata['location'])

except Exception as e:
    logging.error(e)
