from pprint import pprint
import boto3


def put_movie(title, year, actors):

    region=boto3.session.Session().region_name

    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client

    table = dynamodb.Table('movies')
    response = table.put_item(
       Item={
            'year': year,
            'title': title,
            'info': {
                'actors': actors
            }
        }
    )
    return response


if __name__ == '__main__':

    movie_title = "The Godfather"
    movie_year =  1972
    movie_actors = {"Marlon Brando", "Al Pacino", "James Caan"}

    movie_resp = put_movie(movie_title, movie_year, movie_actors)
    print("Put movie succeeded:")
    pprint(movie_resp)

        movie_title = "Deliverance"
    movie_year =  1972
    movie_actors = {"Jon Voight", "Burt Reynolds", "Ned Beatty"}

    movie_resp = put_movie(movie_title, movie_year, movie_actors)
    print("Put movie succeeded:")
    pprint(movie_resp)

    movie_title = "The Shawshank Redemption"
    movie_year =  1994
    movie_actors = {"Tim Robbins", "Morgan Freeman", "Bob Gunton"}

    movie_resp = put_movie(movie_title, movie_year, movie_actors)
    print("Put movie succeeded:")
    pprint(movie_resp)
