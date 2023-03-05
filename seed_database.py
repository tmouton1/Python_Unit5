"""Script to seed database."""
import os
import json
from random import choice, randint
from datetime import datetime
from server import app


import crud
import model
import server

os.system("dropdb ratings")
os.system('createdb ratings')

model.connect_to_db(server.app)

with app.app_context():

    model.db.create_all()

# Load movie data from JSON file
    with open('data/movies.json') as f:
        movie_data = json.loads(f.read())

    # Create movies, store them in list so we can use them
    # to create fake ratings later
    movies_in_db = []
    for movie in movie_data:
        title, overview, poster_path = (
            movie["title"],
            movie["overview"],
            movie["poster_path"],
        )

    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

with app.app_context():   
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

    with app.app_context():
        model.db.session.add_all(movies_in_db)
        model.db.session.commit()


for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)

    with app.app_context():
        model.db.session.add(user)

for _ in range(10):
    random_movie = choice(movies_in_db)
    score = randint(1, 5)

    rating = crud.create_rating(user, random_movie, score)

    with app.app_context():
        model.db.session.add(rating)

with app.app_context():        

    model.db.session.commit()




