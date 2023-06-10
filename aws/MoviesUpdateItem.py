from decimal import Decimal
from pprint import pprint
from botocore.exceptions import ClientError
import boto3


def update_movie(title, year, rating, plot, actors):

    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client

    table = dynamodb.Table('movies')

    try:
        response = table.update_item(
            Key={
                'year': year,
                'title': title
            },
            UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a",
            ExpressionAttributeValues={
                ':r': Decimal(rating),
                ':p': plot,
                ':a': actors
            },
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
            print("Update movie failed:",e.response['Error']['Message'])
    else:
        print("Update movie succeeded:","\n")
        pprint(response)
        return response


if __name__ == '__main__':

    movie_title = "The Godfather"
    movie_year =  1972
    movie_rating = Decimal('9.2')
    movie_plot = "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
    movie_actors = ["Marlon Brando", "Al Pacino", "James Caan"]

    print("\n","Updating...","\n")

    update_movie(movie_title, movie_year, movie_rating, movie_plot, movie_actors)
