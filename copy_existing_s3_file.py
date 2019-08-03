import boto3
s3 = boto3.resource('s3')
bucket_name = 'test-encryption-bucket-source'
region = 'us-east-1'
bucket = s3.Bucket(bucket_name)
kms_key = 'Source_Region_ARN_VALE'
client = boto3.client('s3', region)
for file in bucket.objects.all():
    print(file.key)
    client.copy_object(
    Bucket=bucket_name,
    CopySource=bucket_name+'/'+file.key,
    Key=file.key,
    ServerSideEncryption='aws:kms',
    StorageClass='STANDARD',
    SSEKMSKeyId=kms_key
    )
