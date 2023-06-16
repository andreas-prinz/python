from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr
import argparse
import time
from decimal import *

def scan_movies(GenreToFind):
    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) #low-level Client
    table = dynamodb.Table('movies') #define which dynamodb table to access

    scanreturn = table.query(                    # perform first scan
        IndexName="genre-globo-index",            # assume the global index name was created using our CreateGSI script that named it genre-globo-index
        KeyConditionExpression=Key("genre").eq(GenreToFind)
    )
    return scanreturn


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("Genre", help="Search by genre, ex: Action... argument is case sensitive")
    args = parser.parse_args()
    query_direct = (args.Genre) #section to collect argument from command line

    start = time.time()
    movies = scan_movies(query_direct) #scan_movies returns dict, which is dict of each individual database item returned by scan
    end = time.time()
    print("Count is ", movies['Count'])  # print the count of items returned by the query
    print("ScannedCount is ", movies['ScannedCount'])  # print the count of items that had to be scanned to process the query
    print('Total time: {} sec'.format(end - start))
