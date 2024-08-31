import json
import requests

def lambda_handler(event, context):
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    return {
        'statusCode': 200,
        'body': json.dumps(users)
    }