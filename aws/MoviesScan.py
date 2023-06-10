from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key
import argparse


def scan_movies(year_range, display_movies):

    region=boto3.session.Session().region_name

    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client

    table = dynamodb.Table('movies')
    scan_kwargs = {
        'FilterExpression': Key('year').between(*year_range),
        'ProjectionExpression': "#yr, title, info.actors",
        'ExpressionAttributeNames': {"#yr": "year"}
    }

    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        display_movies(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("start_year", help="Starting year, ex: 1950")
    parser.add_argument("end_year", help="Ending year. ex: 1959")

    args = parser.parse_args()

    year1 = int(args.start_year)
    year2 = int(args.end_year)
    query_range = (year1, year2)

    def print_movies(movies):
        for movie in movies:
            print(f"\n{movie['year']} : {movie['title']}")
            if 'info' in movie:
                pprint(movie['info'])
            else:
                print("{'rating': NA}")

    print(f"Scanning for movies released from {query_range[0]} to {query_range[1]}...")
    scan_movies(query_range, print_movies)
