from decimal import Decimal
import json
import boto3


def load_movies(movies):

    region=boto3.session.Session().region_name

    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client

    table = dynamodb.Table('movies')
    
    for movie in movies:
       year = int(movie['year'])
       title = movie['title']
       print("Adding movie:", year, title)
       table.put_item(Item=movie)

if __name__ == '__main__':

    with open("moviedata-my.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    
    load_movies(movie_list)
