import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_producer_consumer.s3_producer_consumer_stack import S3ProducerConsumerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_producer_consumer/s3_producer_consumer_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3ProducerConsumerStack(app, "s3-producer-consumer")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
