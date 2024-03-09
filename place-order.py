import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    print("Starting order placement lambda function withe event: ", event)
    
    table_name = 'FoodOrders'

    print("Using table: ", table_name)

    table = dynamodb.Table(table_name)

    payload = json.loads(event['body'])

    print("Payload received: ",payload)

    order_id = str(uuid.uuid4())
 
    print("Generated OrderId: ", order_id)

    item = {
        'OrderId': order_id,
        'FoodItemId': payload['FoodItemId'],
        'Price': payload['Price'],
        'Address': payload['Address'],
        'Phone': payload['Phone'],
        'Email': payload['Email']
    }
    print("Item to insert: ",item)

    response = table.put_item(Item=item)
    
    print("Order placed successfully:", response)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Order placed successfully', 'OrderId': order_id})
    }