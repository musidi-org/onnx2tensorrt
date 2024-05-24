import boto3
import os
from dotenv import load_dotenv
load_dotenv()

bucketClient = boto3.client('s3',
  endpoint_url=os.environ["S3_ENDPOINT"],
  aws_access_key_id=os.environ["S3_KEY_ID"],
  aws_secret_access_key=os.environ["S3_KEY"],
  region_name=os.environ["REGION_NAME"]
)

def downloadBucketFile(filePath, bucketName, bucketKey):
  try:
    bucketClient.download_file(bucketName, bucketKey, filePath)
    return True
  except Exception as error:
    print(error)
    return False

def uploadBucketFile(filePath, bucketName, bucketKey):
  try:
    bucketClient.upload_file(filePath, bucketName, bucketKey)
    return True
  except Exception as error:
    print(error)
    return False
