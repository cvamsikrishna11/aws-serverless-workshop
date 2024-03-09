import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    print("Event:", event)

    table_name = 'FoodItems'
    
    print("Using table:", table_name)

    table = dynamodb.Table(table_name)

    food_id = event['queryStringParameters']['id']

    print("Fetching item with ID:", food_id)

    response = table.get_item(
        Key={
            'FoodItemId': food_id
        }
    )

    print ("DynamoDB Response:", response)

    if 'Item' in response:
        print("Item found:", response['Item'])
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    else:
        print("Item not found")
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Item not found'})
        }