# Import the boto3 library to interact with AWS services
import boto3

# Create an EC2 client for interacting with Amazon EC2
client = boto3.client("ec2", region_name="us-east-1")

# Use the describe_volumes method to list all volumes
# Filters are used to list only volumes that are in the 'available' state
response = client.describe_volumes(
    Filters=[
        {
            'Name': 'status', # The filter name, in this case, filtering by volume status
            'Values': [
                'available', # The filter value, specifying we only want volumes that are 'available'
            ]
        }
    ],
)

print("Available Volumes Response: ", response)

# Iterate through the list of available volumes returned by the describe_volumes call
for i in response["Volumes"]:
    # Print the Volume ID of each available volume
    print("Deleting Volume with ID ::::::::::::::::::::::::::", i["VolumeId"])
    
    # Use the delete_volume method to delete the volume specified by its VolumeId
    # This operation is irreversible and will delete the volume permanently
    response = client.delete_volume(
        VolumeId=i["VolumeId"]
    )
    
    # Print the response from the delete_volume call
    # This usually contains information about the deletion request
    print(response)