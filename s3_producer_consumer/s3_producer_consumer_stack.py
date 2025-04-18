from aws_cdk import (
    Stack,
)
from constructs import Construct
import aws_cdk as cdk

from s3_producer_consumer.Consumer import Consumer
from s3_producer_consumer.Producer import Producer


class S3ProducerConsumerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_producer = Producer(self, "Producer")
        
        Consumer(
            self, "Consumer", producer_bucket=bucket_producer.producer_bucket
        )

        cdk.CfnOutput(
            self,
            "ProducerBucketName",
            value=bucket_producer.producer_bucket.bucket_name,
            description="The name of the producer bucket",
        )
