import json

def lambda_handler(event, context):
    print("In lambda handler")

    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Serverless Web Application: AWS Lambda handles backend execution, API Gateway manages HTTP requests, and Amazon S3 provides static website hosting."
    }

    return resp
