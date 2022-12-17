from Services.ServiceL import service_links
from Services.ServiceC import service_clients
from Services.ServiceM import service_movies

def input_for_test_movies():
    mvs = service_movies()

    id = 1
    title = "Spiderman 1"
    description = "After being bitten by a genetically-modified spider, a shy teenager gains spider-like abilities that he uses to fight injustice as a masked superhero and face a vengeful enemy."
    type = "superhero"
    year = 2002

    mvs.add_movie(id, title, description, type, year)

    id = 2
    title = "Avengers"
    description = "Earth's Mightiest Heroes stand as the planet's first line of defense against the most powerful threats in the universe."
    type = "action"
    year = 2005

    mvs.add_movie(id, title, description, type, year)

    id = 3
    title = "Matrix"
    description = "Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government."
    type = "adventure"
    year = 1999

    mvs.add_movie(id, title, description, type, year)

    id = 4
    title = "Batman"
    description = "On Halloween, Gotham City mayor Don Mitchell Jr. is murdered by the Riddler, a masked killer."
    type = "thriller"
    year = 2022

    mvs.add_movie(id, title, description, type, year)

    id = 5
    title = "The Nun"
    description = "ngaeuighaeiuhuaeihgiuaehg"
    type = "horror"
    year = 2020

    mvs.add_movie(id, title, description, type, year)

    id = 6
    title = "Mario"
    description = "mario and luigi"
    type = "horror"
    year = 2023

    mvs.add_movie(id, title, description, type, year)

    id = 7
    title = "Ora de logica!"
    description = "Ora de logica este horror"
    type = "horror"
    year = 2022

    mvs.add_movie(id, title, description, type, year)

    return mvs


def get_movies_with_type(movies, type):
    movie_list = list()
    for movie in movies:
        if (movie.get_type() == type):
            movie_list.append(movie)

    return movie_list

def sort_clients_age(list_of_clients):
    return sorted(list_of_clients, key=lambda x: x.get_age())


def id_to_clients(cls, clients_id):
    clients_list = list()
    for id in clients_id:
        clients_list.append(cls.get_client_by_id(id))

    return clients_list


def id_to_movies(mvs, movies_id):
    movies_list = list()
    for id in movies_id:
        movies_list.append(mvs.get_movie_by_id(id))

    return movies_list

def input_for_test_clients():
    cls = service_clients()

    id = 1
    name = "Serban Valentin"
    cnp = 5030917297316
    age = 19

    cls.add_client(id, name, cnp, age)

    id = 2
    name = "Domnica Teodor"
    cnp = 5030917567316
    age = 20

    cls.add_client(id, name, cnp, age)

    id = 3
    name = "Tacore Clara"
    cnp = 4560403990495
    age = 19

    cls.add_client(id, name, cnp, age)

    id = 4
    name = "Modoian Vlad"
    cnp = 8594857494596
    age = 18

    cls.add_client(id, name, cnp, age)

    id = 5
    name = "Vlad Tepes"
    cnp = 1000000000001
    age = 40

    cls.add_client(id, name, cnp, age)

    id = 6
    name = "Nichita Stanescu"
    cnp = 1000000000002
    age = 35

    cls.add_client(id, name, cnp, age)

    id = 7
    name = "Mihai Eminovici"
    cnp = 1000000000003
    age = 39

    cls.add_client(id, name, cnp, age)

    id = 8
    name = "Ratonul Neinfricat"
    cnp = 1000000000004
    age = 1

    cls.add_client(id, name, cnp, age)

    return cls


def add_links(links, cls, mvs):
    id_client = 6
    id_movie = 5
    links.add_link(id_client, id_movie, cls, mvs)
    cls.add_movie_client(id_client, id_movie)

    id_client = 4
    id_movie = 5
    links.add_link(id_client, id_movie, cls, mvs)
    cls.add_movie_client(id_client, id_movie)

    id_client = 3
    id_movie = 5
    links.add_link(id_client, id_movie, cls, mvs)
    cls.add_movie_client(id_client, id_movie)

    id_client = 2
    id_movie = 6
    links.add_link(id_client, id_movie, cls, mvs)
    cls.add_movie_client(id_client, id_movie)

    id_client = 2
    id_movie = 7
    links.add_link(id_client, id_movie, cls, mvs)
    cls.add_movie_client(id_client, id_movie)

def input_for_test_links(cls, mvs):
    links = service_links()
    id_client = 1
    id_movie = 1
    links.add_link(id_client, id_movie, cls, mvs)
    cls.add_movie_client(id_client, id_movie)

    id_client = 2
    id_movie = 2
    links.add_link(id_client, id_movie, cls, mvs)
    cls.add_movie_client(id_client, id_movie)

    id_client = 3
    id_movie = 3
    links.add_link(id_client, id_movie, cls, mvs)
    cls.add_movie_client(id_client, id_movie)

    id_client = 4
    id_movie = 4
    links.add_link(id_client, id_movie, cls, mvs)
    cls.add_movie_client(id_client, id_movie)

    return links

def sort_list_clients_name(clients_list):
    return sorted(clients_list, key=lambda x: x.get_name())


def sort_list_clients_movies(clients_list):
    return sorted(clients_list, key=lambda x: x.get_movies_len(), reverse=True)


def get_30_percent_clients(clients_list):
    return clients_list[:int(0.3 * len(clients_list))]


def print_30_percent(clients_list):
    for client in clients_list:
        print("Nume: " + str(client.get_name()) + "\n" + "Numar filme inchiriate: " + str(client.get_movies_len()) + "\n")


def eq_list_client(cl_list1, cl_list2):
    if (len(cl_list1) != len(cl_list2)):
        return False
    for i in range(len(cl_list1)):
        if (cl_list1[i] != cl_list2[i]):
            return False

    return True


def eq_list_movie(mv_list1, mv_list2):
    if (len(mv_list1) != len(mv_list2)):
        return False
    for i in range(len(mv_list1)):
        if (mv_list1[i] != mv_list2[i]):
            return False

    return True
