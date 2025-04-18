from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as _lambda,
)
from cdk_aws_lambda_powertools_layer import LambdaPowertoolsLayer
from constructs import Construct
import aws_cdk.aws_iam as iam
import aws_cdk as cdk


class Consumer(Construct):
    def __init__(
        self, scope: Construct, construct_id: str, producer_bucket: s3.Bucket, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_role = iam.Role(
            self,
            "ConsumerLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        producer_bucket.grant_read_write(self.lambda_role)
        
        power_tools_layer = LambdaPowertoolsLayer(self, "PowerToolsLayer")
        
        consumer_lambda = _lambda.Function(
            self,
            "ConsumerLambda",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="consumer_lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
            layers=[power_tools_layer],  # Add the Lambda Powertools layer
            environment={
                "BUCKET_NAME": producer_bucket.bucket_name,
                "LAMBDA_ROLE": self.lambda_role.role_arn,
            },
        )
        
        cdk.CfnOutput(
            self,
            "ConsumerLambdaFunctionName",
            value=consumer_lambda.function_name,
            description="The name of the consumer lambda function",
        )


        
        
