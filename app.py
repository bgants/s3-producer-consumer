#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3_producer_consumer.s3_producer_consumer_stack import S3ProducerConsumerStack

# Set up environment variables
account = os.getenv("AWS_ACCOUNT_ID")
primary_region = os.getenv("AWS_PRIMARY_REGION")
domain_name = os.getenv("AWS_DOMAIN_NAME", "default-domain-name")

primary_environment = cdk.Environment(account=account, region=primary_region)

app = cdk.App()
S3ProducerConsumerStack(app, "S3ProducerConsumerStack", env=primary_environment)

app.synth()
