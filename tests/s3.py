import boto3

SOURCE_BUCKET = "dev-miaradia-s3-bucket"
DESTINATION_BUCKET = "frils-aws-bucket"
OBJECT_KEY = "test_airflow.zip"
s3 = boto3.resource('s3')
copy_source = {
    'Bucket': SOURCE_BUCKET,
    'Key': OBJECT_KEY
}
# s3.meta.client.copy(copy_source, DESTINATION_BUCKET, OBJECT_KEY)


s3 = boto3.client('s3')
response = s3.head_object(Bucket=SOURCE_BUCKET, Key=OBJECT_KEY)
size = response['ContentLength']
print(size)
