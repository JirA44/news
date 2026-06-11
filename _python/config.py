import boto3

s3 = boto3.client('s3', region_name='us-east-1')
bucket_name = 'example-bucket'
file_path = 'data.txt'

s3.upload_file(file_path, bucket_name, file_path)