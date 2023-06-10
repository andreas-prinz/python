import boto3

def delete_movie_table():
    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client

    table = dynamodb.Table('movies')
    table.delete()


if __name__ == '__main__':
    delete_movie_table()
    print("movies table deleted.")
