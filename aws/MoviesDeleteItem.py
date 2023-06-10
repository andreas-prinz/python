from decimal import Decimal
from pprint import pprint
from botocore.exceptions import ClientError

import boto3


def update_movie(title, year):

    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client

    table = dynamodb.Table('movies')

    try:
        response = table.delete_item(
            Key={
                'year': year,
                'title': title
            },
            ConditionExpression = "attribute_exists(info.actors)",
            ReturnValues="ALL_OLD"
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print("Delete movie failed:",e.response['Error']['Message'])
        else:
            raise e
    else:
        if 'Attributes' in response:
            print("Delete movie succeeded:","\n")
            pprint(response['Attributes'])
        else:
            print("Movie not found")


if __name__ == '__main__':

    movie_title = "The Godfather"
    movie_year =  1972

    print("\n","Deleting...","\n")

    update_movie(movie_title, movie_year)
