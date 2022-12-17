from Utils.rent_movies import *
from UI.print_functions import print_menu
from Services.ServiceCFile import service_clients_file
from Services.ServiceMFile import service_movies_file
from Services.ServiceLFile import service_links_file
mode = ""


class UI:
    def __init__(self):
        global mode
        self.__cls = service_clients_file(mode)
        self.__mvs = service_movies_file(mode)
        self.__lks = service_links_file(mode)

    def add_movie(self):
        id = input("Introdu ID: ")
        title = input("Introdu Titlu: ")
        description = input("Introdu Descriere: ")
        type = input("Introdu gen: ")
        year = input("Introdu an: ")
        self.__mvs.add_movie(id, title, description, type, year)

    def del_movie_by_id(self):
        id = input("Introdu ID: ")
        id = self.__mvs.del_movie_by_id(id)
        self.__lks.del_link_movie(id)

    def del_movie_by_title(self):
        title = input("Introdu Titlu: ")
        id_del = self.__mvs.del_movie_by_title(title)
        self.__lks.del_link_movies(id_del)

    def del_movie_by_description(self):
        description = input("Introdu Descriere: ")
        id_del = self.__mvs.del_movie_by_description(description)
        self.__lks.del_link_movies(id_del)

    def del_movie_by_type(self):
        type = input("Introdu gen: ")
        id_del = self.__mvs.del_movie_by_type(type)
        self.__lks.del_link_movies(id_del)

    def del_movie_by_year(self):
        year = input("Introdu an: ")
        id_del = self.__mvs.del_movie_by_year(year)
        self.__lks.del_link_movies(id_del)

    def search_movie_by_id(self):
        id = input("Introdu ID: ")
        movies = self.__mvs.search_movie_by_id(id)

        return movies

    def print_movie_list(self, mv_list):
        for mv in mv_list:
            print(mv)
            print()
    def search_movie_by_title(self):
        title = input("Introdu Titlu: ")
        movies = self.__mvs.search_movie_by_title(title)

        return movies

    def search_movie_by_description(self):
        description = input("Introdu Descriere: ")
        movies = self.__mvs.search_movie_by_description(description)

        return movies

    def search_movie_by_type(self):
        type = input("Introdu gen: ")
        movies = self.__mvs.search_movie_by_type(type)

        return movies

    def search_movies_by_year(self):
        year = input("Introdu an: ")
        movies = self.__mvs.search_movie_by_year(year)

        return movies

    def mod_movie_title(self):
        id = input("Introdu ID: ")
        title = input("Introdu Titlu: ")
        self.__mvs.mod_movie_title(id, title)

    def mod_movie_description(self):
        id = input("Introdu ID: ")
        description = input("Introdu Descriere: ")
        self.__mvs.mod_movie_description(id, description)

    def mod_movie_type(self):
        id = input("Introdu ID: ")
        type = input("Introdu gen: ")
        self.__mvs.mod_movie_type(id, type)

    def mod_movie_year(self):
        id = input("Introdu ID: ")
        year = input("Introdu an: ")
        self.__mvs.mod_movie_year(id, year)

    def add_client(self):
        id = input("Introdu ID: ")
        name = input("Introdu nume: ")
        cnp = input("Introdu CNP: ")
        age = input("Introdu varsta: ")
        self.__cls.add_client(id, name, cnp, age)

    def del_client_by_id(self):
        id = input("Introdu ID: ")
        id = self.__cls.del_client_by_id(id)
        self.__lks.del_link_client(id)

    def del_client_by_name(self):
        name = input("Introdu nume: ")
        id_del = self.__cls.del_client_by_name(name)
        print(id_del)
        self.__lks.del_link_clients(id_del)

    def del_client_by_cnp(self):
        cnp = input("Introdu CNP: ")
        id_del = self.__cls.del_client_by_cnp(cnp)
        self.__lks.del_link_clients(id_del)

    def del_client_by_age(self):
        age = input("Introdu varsta: ")
        id_del = self.__cls.del_client_by_age(age)
        self.__lks.del_link_clients(id_del)

    def mod_client_name(self):
        id = input("Introdu ID: ")
        name = input("Introdu nume: ")
        self.__cls.mod_client_name(id, name)

    def mod_client_cnp(self):
        id = input("Introdu ID: ")
        cnp = input("Introdu CNP: ")
        self.__cls.mod_client_cnp(id, cnp)

    def mod_client_age(self):
        id = input("Introdu ID: ")
        age = input("Introdu varsta: ")
        self.__cls.mod_client_age(id, age)

    def search_client_by_id(self):
        id = input("Introdu ID: ")
        clients = self.__cls.search_client_by_id(id)

        return clients

    def print_client_list(self, cl_list):
        for cl in cl_list:
            print(cl)
            print()

    def search_client_by_name(self):
        name = input("Introdu nume: ")
        clients = self.__cls.search_client_by_name(name)

        return clients

    def search_clients_by_cnp(self):
        cnp = input("Introdu CNP: ")
        clients = self.__cls.search_client_by_cnp(cnp)

        return clients

    def search_clients_by_age(self):
        age = input("Introdu varsta: ")
        clients = self.__cls.search_client_by_age(age)

        return clients

    def get_client_list(self):
        return self.__cls.get_clients_list()

    def get_movie_list(self):
        return self.__mvs.get_movie_list()

    def get_link_list(self):
        return self.__lks.get_link_list()

    def print_link_list(self, lk_list):
        for lk in lk_list:
            print(lk)
            print()

    def add_link(self):
        id_c = input("Introdu ID-ul clientului: ")
        id_m = input("Introdu ID-ul filmului: ")
        self.__lks.add_link(id_c, id_m, self.__cls, self.__mvs)
        self.__cls.add_movie_client(id_c, id_m)

    def del_link(self):
        id = int(input("Introdu ID-ul inchirierii: "))
        link = self.__lks.get_link_by_id(id)
        id_c = link.get_id_client()
        id_m = link.get_id_movie()
        self.__cls.del_movie_client(id_c, id_m)
        self.__lks.del_link(id)

    def most_rented_movies(self):
        id_movies = self.__lks.most_rented_movies()
        movies = self.__mvs.movies_by_id(id_movies)

        return movies

    def sort_list_clients_name(self):
        id_clients = self.__lks.get_id_clients()
        list_of_clients = id_to_clients(self.__cls, id_clients)
        sorted_list = sort_list_clients_name(list_of_clients)

        return sorted_list

    def sort_list_clients_movies(self):
        id_clients = self.__lks.get_id_clients()
        list_of_clients = id_to_clients(self.__cls, id_clients)
        sorted_list = sort_list_clients_movies(list_of_clients)

        return sorted_list

    def get_30_percent_clients(self):
        id_clients = self.__lks.get_id_clients()
        list_of_clients = id_to_clients(self.__cls, id_clients)
        sorted_list = sort_list_clients_movies(list_of_clients)
        thirty_percent = get_30_percent_clients(sorted_list)

        return thirty_percent

    def print_30_percent(self, clients_list):
        for client in clients_list:
            print("Nume: " + str(client.get_name()) + "\n" + "Numar filme inchiriate: " + str(
                client.get_movies_len()) + "\n")

    def show_movie_client(self):
        id_c = input("Introdu ID-ul clientului: ")
        client = self.__cls.get_client_by_id(id_c)
        movies_id = client.get_movie_id_list()
        movies_list = id_to_movies(self.__mvs, movies_id)

        return movies_list

    def print_clients_in_file(self, name_of_the_file, client_list):
        with open(name_of_the_file, 'w') as f:
            for client in client_list:
                client_string = str(client.get_id()) + ';' + str(client.get_name()) + ';' + str(
                    client.get_cnp()) + ';' + str(client.get_age()) + ';' + '\n'
                f.write(client_string)

    def sort_clients_age(self):
        id_clients = self.__lks.get_id_clients()
        list_of_clients = id_to_clients(self.__cls, id_clients)
        clients = sort_clients_age(list_of_clients)

        return clients

    def main_function(self):
        print_menu()
        global mode
        if(mode == "file"):
            add_links(self.__lks, self.__cls, self.__mvs)
        while True:
            command = input("Introduceti comanda pe care doriti sa o efectuati! ")
            if (command == "af"):
                self.add_movie()
            elif (command == "sfi"):
                self.del_movie_by_id()
            elif (command == "sft"):
                self.del_movie_by_title()
            elif (command == "sfd"):
                self.del_movie_by_description()
            elif (command == "sfg"):
                self.del_movie_by_type()
            elif (command == "sfa"):
                self.del_movie_by_year()
            elif (command == "cfi"):
                movies = self.search_movie_by_id()
                self.print_movie_list(movies)
            elif (command == "cft"):
                movies = self.search_movie_by_title()
                self.print_movie_list(movies)
            elif (command == "cfd"):
                movies = self.search_movie_by_description()
                self.print_movie_list(movies)
            elif (command == "cfg"):
                movies = self.search_movie_by_type()
                self.print_movie_list(movies)
            elif (command == "cfa"):
                movies = self.search_movies_by_year()
                self.print_movie_list(movies)
            elif (command == "mft"):
                self.mod_movie_title()
            elif (command == "mfd"):
                self.mod_movie_description()
            elif (command == "mfg"):
                self.mod_movie_type()
            elif (command == "mfa"):
                self.mod_movie_year()
            elif (command == "ac"):
                self.add_client()
            elif (command == "sci"):
                self.del_client_by_id()
            elif (command == "scn"):
                self.del_client_by_name()
            elif (command == "scc"):
                self.del_client_by_cnp()
            elif (command == "scv"):
                self.del_client_by_age()
            elif (command == "mcn"):
                self.mod_client_name()
            elif (command == "mcc"):
                self.mod_client_cnp()
            elif (command == "mcv"):
                self.mod_client_age()
            elif (command == "cci"):
                clients = self.search_client_by_id()
                self.print_client_list(clients)
            elif (command == "ccn"):
                clients = self.search_client_by_name()
                self.print_client_list(clients)
            elif (command == "ccc"):
                clients = self.search_clients_by_cnp()
                self.print_client_list(clients)
            elif (command == "ccv"):
                clients = self.search_clients_by_age()
                self.print_client_list(clients)
            elif (command == "showc"):
                clients = self.get_client_list()
                self.print_client_list(clients)
            elif (command == "showf"):
                movies = self.get_movie_list()
                self.print_movie_list(movies)
            elif (command == "showl"):
                links = self.get_link_list()
                self.print_link_list(links)
            elif (command == "ifc"):
                self.add_link()
            elif (command == "sl"):
                self.del_link()
            elif (command == "cmif"):
                movies = self.most_rented_movies()
                self.print_movie_list(movies)
            elif (command == "acon"):
                sorted_list = self.sort_list_clients_name()
                self.print_client_list(sorted_list)
            elif (command == "acof"):
                sorted_list = self.sort_list_clients_movies()
                self.print_client_list(sorted_list)
            elif (command == "ac3of"):
                thirty_percent = self.get_30_percent_clients()
                self.print_30_percent(thirty_percent)
            elif (command == "showmvc"):
                movies_list = self.show_movie_client()
                self.print_movie_list(movies_list)
            elif (command == "cmifgs"):
                clients = self.sort_clients_age()
                self.print_clients_in_file('show.txt', clients)
            elif (command == "exit"):
                break

    def run(self):
        self.main_function()
