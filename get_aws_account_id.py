import boto3
'''
aws_mgmt_console = boto3.session.Session(profile_name='default')

sts_mgmt_console = aws_mgmt_console.client(service_name='sts')

response = sts_mgmt_console.get_caller_identity()

print(response['Account'])

'''
aws_mgt_console = boto3.session.Session(profile_name='raj')
sts_mgt_console = aws_mgt_console.client(service_name='sts')
response = sts_mgt_console.get_caller_identity()
print(response['Account'])



