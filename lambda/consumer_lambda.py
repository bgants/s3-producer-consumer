import json
import os
from aws_lambda_powertools import Logger

logger = Logger()


@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    # Log the event
    logger.info(f"Received event from S3 bucket: {json.dumps(event)}")

    # get s3 bucket name from environment variable    
    bucket_name = os.environ["BUCKET_NAME"]
    
    
    # use the bucket name to perform some action
    # For example, you can log the bucket name
    logger.info(f"Bucket name: {bucket_name}")