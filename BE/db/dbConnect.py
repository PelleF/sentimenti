import boto3
import uuid


class DynamoDbClass:
    """A class to connect to DynamoDB and retrieve and save entries"""

    def __init__(self, table_name):
        # Initialize all configs so we can use the database
        self.table_name = table_name
        self.dynamo_client = boto3.client('dynamodb', region_name="eu-west-1", endpoint_url='http://localhost:8000')
        self.dynamo_resource = boto3.resource('dynamodb', region_name="eu-west-1", endpoint_url='http://localhost:8000')
        try:
            self.table = self.dynamo_resource.Table(table_name)
            # TODO FIX THIS THING THAT IT ALWAYUS WORKS, EXISITNG OR NOT
        except self.dynamo_client.exceptions.ResourceNotFoundException as _:
            print(f"Table with the name {table_name} is created")
            self.table = self.dynamo_client.create_table(TableName=table_name, KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}], AttributeDefinitions=[ {"AttributeName": "id", "AttributeType": "S"}], ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10})
            pass

    def insert_database(self, score, title, url):
        entry = {"id": str(uuid.uuid4()), "score": score, "title": title, "url": url}
        self.table.put_item(Item=entry)


if __name__ == "__main__":
    # Use this if you want to test shit
    dyno = DynamoDbClass("another_test_why_not_agai9n_2")
    dyno.insert_database("0.5", "A brave new world Pelle is exploring", "www.trucs.com")
    print(dyno.table.scan())
