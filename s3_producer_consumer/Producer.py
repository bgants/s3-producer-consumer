from aws_cdk import (
    aws_s3 as s3,
)
from constructs import Construct
import aws_cdk as cdk


class Producer(Construct):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        account_id = cdk.Stack.of(self).account

        bucket = s3.Bucket(
            self,
            "ProducerBucket",  # Provide a unique id for the bucket
            bucket_name="producer-bucket-" + account_id,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        self.producer_bucket = bucket
