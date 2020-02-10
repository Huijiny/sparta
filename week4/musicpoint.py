from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

all_movies = list(db.movies.find());
print(all_movies)

target_movie = db.movies.find_one({'title' : '월-E'});
target_movie_star = target_movie['star']
print(target_movie_star)
for movie in all_movies :
    if float(movie['star']) > float(target_movie_star) :
        print(movie['title'])

