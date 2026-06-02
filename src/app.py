import json
import os
import uuid

import boto3

dynamodb = boto3.resource("dynamodb")

TABLE_NAME = os.environ["TABLE_NAME"]

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):

    body = json.loads(event["body"])

    message = body["message"]

    item = {
        "message_id": str(uuid.uuid4()),
        "message": message
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "saved",
            "item": item
        })
    }
