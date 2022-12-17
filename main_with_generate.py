import random
import string
from Repository.Clients import Clients
from Repository.Movies import Movies


def generate_random_person():
    id = random.randint(1, 1000000)
    name = ''.join(random.choices(string.ascii_letters, k=8))
    cnp = random.randint(1000000000000, 9999999999999)
    age = random.randint(10, 99)

    return id, age, cnp, name


def generate_random_movie():
    types = ["action", "superhero", "adventure", "thriller", "drama"]

    id = random.randint(1, 1000000)
    title = ''.join(random.choices(string.ascii_letters, k=10))
    description = ''.join(random.choices(string.ascii_letters, k=20))
    type = random.choice(types)
    year = random.randint(1900, 2022)

    return id, type, year, title, description


def generate_multiple_clients(x):
    cls = Clients()
    for i in range(x):
        id, age, cnp, name = generate_random_person()
        cls.add_client(id, name, cnp, age)

    return cls


def generate_multiple_movies(x):
    mvs = Movies()
    for i in range(x):
        id, type, year, title, description = generate_random_movie()
        mvs.add_movie(id, title, description, type, year)

    return mvs
