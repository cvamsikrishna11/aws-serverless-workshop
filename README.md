# AWS Serverless Workshop
This repository serves as a guide and toolkit for building a serverless application on AWS, focusing on utilizing AWS Lambda and DynamoDB to create a simple food ordering application scenario!

### Prerequisites
Before you begin, ensure you have the following prerequisites met:

1. An active AWS account.
2. AWS CLI installed and configured with appropriate credentials. See AWS CLI setup instructions. (https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
3. Basic familiarity with AWS services, especially AWS Lambda and DynamoDB.

### Setup Instructions

1. Clone the repo

```
git clone https://github.com/cvamsikrishna11/aws-serverless-workshop.git

cd aws-serverless-workshop (or open the folder on VS code)
```

2. Deploy AWS Databases and Roles
```
aws cloudformation create-stack --stack-name FoodApp --template-body file://dynamodb-iam.yml --capabilities CAPABILITY_IAM --capabilities CAPABILITY_NAMED_IAM --region us-east-1
```

3. Insert items in the DynamoDB table
```
aws dynamodb batch-write-item --request-items file://food-items.json --region us-east-1
```

4. Create lambda functions

5. Integrate with API Gateway

6. Test with Postman

7. For the scheduler create a Rule under EventBridge