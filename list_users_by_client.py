import boto3

client = boto3.client('iam')

response = client.list_users()

for each_item in response['Users']:
    print(each_item['UserName'])