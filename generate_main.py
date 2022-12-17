from Tests.test_functions_client import run_all_tests_client, input_for_test_clients
from Tests.test_functions_movie import run_all_tests_movie, input_for_test_movies
from Tests.test_functions_link import run_all_tests_link, input_for_test_links
from Utils.rent_movies import *
from UI.print_functions import print_menu
from main_with_generate import *
from Services.ServiceC import service_clients
from Services.ServiceM import service_movies

s_cls = service_clients()
s_mvs = service_movies()
mvs = Movies()
cls = Clients()
while True:
    command = input("Introduceti comanda ")
    if(command == "generare"):
        num_clienti = int(input("Introdu nr: "))
        num_filme = int(input("introdu nr: "))
        cls = s_cls.generate_clients(num_clienti)
        mvs = s_mvs.generate_movies(num_filme)
    elif(command == "afisare filme"):
        movies = mvs.get_movie_list()
        print_movie_list(movies)
    elif(command == "afisare clienti"):
        clients = cls.get_clients_list()
        print_client_list(clients)
    elif(command == "exit"):
        break

