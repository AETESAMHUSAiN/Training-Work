from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class CustResourceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(
            self, 
            id="bucket1234", 
            bucket_name="ak-bucket123"
        )