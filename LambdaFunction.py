import json
import random

def lambda_handler(event, context):
    responses = ["yes", "no", "maybe"]
    answer = random.choice(responses)
    return {
        'statusCode': 200,
        'body': answer
    }
