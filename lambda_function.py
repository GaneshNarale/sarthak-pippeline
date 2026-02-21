import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LambdaLogs')

def lambda_handler(event, context):
    
    message = "Hello from DevOps to devops engineerrrr "
    
    # Store in DynamoDB
    table.put_item(
        Item={
            'id': str(datetime.datetime.now().timestamp()),
            'message': message
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

