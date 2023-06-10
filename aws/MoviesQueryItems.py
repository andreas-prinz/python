from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key
import argparse


def query_movies(year):

    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client

    table = dynamodb.Table('movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    return response['Items']


if __name__ == '__main__':


    parser = argparse.ArgumentParser()
    parser.add_argument("Year", help="Search year, ex: 1950")
    args = parser.parse_args()

    query_year = int(args.Year)

    print(f"Movies released in {query_year}")

    movies = query_movies(query_year)
    for movie in movies:
        print(movie['year'], ":", movie['title'])
