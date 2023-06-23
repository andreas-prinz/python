from decimal import Decimal
import json
import argparse
import boto3
from pprint import pprint, pformat
import time
import random
import threading


def load_movies(movies, startnum, endnum):

    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client
    table = dynamodb.Table('movies')

    countx = startnum
    while (countx <= endnum):

        response = table.put_item(Item=movies[countx])
        countx += 1

def gen_movies(startnum, endnum):

    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client
    table = dynamodb.Table('movies')

    for x in range(startnum,endnum):
        newmyear = random.randint(1920,2017)
        xstrin = str(x)
        yearstr = str(newmyear)
        newmtitle="Junkerdata" + yearstr + xstrin +" -- junk even harder"
        newmdirector = ["Horst Bleve" + xstrin]
        newmreleased = str(newmyear) + "-06-03T00:00:00Z"
        newmrating = 1
        newmgenrelist = ["FakeActionData", "FakeDramaData", "FakeHorrorData", "FakeFamilyData", "FakeSci-FiData", "FakeCrimeData", "FakeComedyData", "FakeFakeData", "FakeGenreData", "FakeMoreData"]
        newmgenre = newmgenrelist[random.randint(0,9)]
        newmimage = "http://ia.media-imdb.com/images/M/MV5BMTQxODE3NjM1Ml5BMl5BanBnXkFtZTcwMzkzNjc4OA@@._V1_SX400_" + xstrin + ".jpg"
        newmplot = "In the year " + yearstr + ", only more junk can save the database"
        newmrank = 4700 + x
        newmrtime = 50
        newmactors = ["FakeLead", "FakeSidekick", "FakeAntagonist"]
        movie = {
            "year": newmyear,
            "title": newmtitle,
            "directors": newmdirector,
            "release_date": newmreleased,
            "rating": newmrating,
            "genre": newmgenre,
            "image_url": newmimage,
            "plot": newmplot,
            "rank": newmrank,
            "running_time_secs": newmrtime,
            "actors": newmactors
        }

        response = table.put_item(Item=movie)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("datafile", help="location of text data file, ex: movies.json")
    args = parser.parse_args()

    start = time.time()

    with open(args.datafile,"r") as json_file:
            movie_list = json.load(json_file, parse_float=Decimal)

    t1 = threading.Thread(target=load_movies, args=(movie_list, 0, 1100,))
    t2 = threading.Thread(target=load_movies, args=(movie_list, 1101, 2200,))
    t3 = threading.Thread(target=load_movies, args=(movie_list, 2201, 3300,))
    t4 = threading.Thread(target=load_movies, args=(movie_list, 3301, 4608,))

    t1.start()
    time.sleep(2)
    t2.start()
    time.sleep(2)
    t3.start()
    time.sleep(2)
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    json_file.close()

    t1 = threading.Thread(target=gen_movies, args=(1,4000,))
    t2 = threading.Thread(target=gen_movies, args=(4001,8000,))
    t3 = threading.Thread(target=gen_movies, args=(8001,12000,))
    t4 = threading.Thread(target=gen_movies, args=(12001,16000,))
    t5 = threading.Thread(target=gen_movies, args=(16001,20000,))
    t6 = threading.Thread(target=gen_movies, args=(20001,24000,))
    t7 = threading.Thread(target=gen_movies, args=(24001,28000,))
    t8 = threading.Thread(target=gen_movies, args=(28001,32000,))
    t9 = threading.Thread(target=gen_movies, args=(32001,36000,))
    t10 = threading.Thread(target=gen_movies, args=(36001,40000,))

    t1.start()
    time.sleep(2)
    t2.start()
    time.sleep(2)
    t3.start()
    time.sleep(2)
    t4.start()
    time.sleep(2)
    t5.start()
    time.sleep(2)
    t6.start()
    time.sleep(2)
    t7.start()
    time.sleep(2)
    t8.start()
    time.sleep(2)
    t9.start()
    time.sleep(2)
    t10.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()

    end = time.time()
    print('Total time: {} sec'.format(end - start))
