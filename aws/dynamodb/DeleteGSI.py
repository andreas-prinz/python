from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr
import argparse
import time
from decimal import *

def RemoveGSI(attributename):
    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) #low-level Client
    table = dynamodb.Table('movies') #define which dynamodb table to access
    oldindexname = attributename + "-globo-index"

    response = table.update(
        GlobalSecondaryIndexUpdates=[
            {
                'Delete': {
                    'IndexName': oldindexname
                }
            }
        ],
    )
    return response

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("indexattribute", help="Delete GSI based on attribute entered here")
    args = parser.parse_args()
    oldGSIkey = (args.indexattribute) #section to collect argument from command line

    result = RemoveGSI(oldGSIkey)
