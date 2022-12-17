from Repository.Links import Links
from Utils.validation_functions import *
from Repository.LinksFIle import LinksFile


class service_links_file:
    def __init__(self, mode):
        if(mode == "file"):
            self.__links = LinksFile('Data/links.txt')
        else:
            self.__links = Links()

    def add_link(self, id_c, id_m, clients_list, movies_list):
        """
        Adauga o inchiriere
        :param id_c:
        :param id_m:
        :return:
        """
        val_id_c = validate_id_year(id_c)
        val_id_m = validate_id_year(id_m)
        if (val_id_c == False or val_id_m == False):
            return

        id_c = int(id_c)
        id_m = int(id_m)

        if (not clients_list.check_if_id_exists(id_c) or not movies_list.check_if_id_exists(id_m)):
            print("ID inexistent!")
            return

        self.__links.add_link(id_c, id_m)

    def get_link_by_id(self, id):
        """
        Returneaza un link dupa id
        :param id:
        :return:
        """
        val_id = validate_id_year(id)
        if (val_id == False):
            return

        id = int(id)

        return self.__links.get_link_by_id(id)

    def del_link(self, id):
        """
        Sterge o inchirirere
        :param id:
        :return:
        """
        self.__links.del_link(id)

    def most_rented_movies(self):
        """
        Returneaza cele mai inchiriate filme
        :return:
        """
        dict_movies = self.__links.dict_for_most_rented_movies()
        max_cnt = 0
        id_list_movies = list()
        for id, cnt in dict_movies.items():
            if (cnt > max_cnt):
                id_list_movies.clear()
                max_cnt = cnt
                id_list_movies.append(id)
            elif (cnt == max_cnt):
                id_list_movies.append(id)

        return id_list_movies

    def get_link_pos(self, i):
        """
        Returneaza pozitia unei inchirieri in lista
        :param i:
        :return:
        """
        return self.__links.get_link_pos(i)

    def del_link_client(self, client_id):
        """
        Sterge inchirierea unui client
        :param client_id:
        :return:
        """
        self.__links.del_link_client(client_id)

    def del_link_movie(self, movie_id):
        """
        Sterge inchirierea dupa id-ul filmului
        :param movie_id:
        :return:
        """
        self.__links.del_link_movie(movie_id)

    def del_link_clients(self, clients_id):
        """
        Sterge inchirierile a mai multor clienti
        :param clients_id:
        :return:
        """
        self.__links.del_link_clients(clients_id)

    def del_link_movies(self, movies_id):
        """
        Sterge inchirierile a mai multor filme
        :param movies_id:
        :return:
        """
        self.__links.del_link_movies(movies_id)

    def get_num_links(self):
        """
        Returneaza lungimea listei de inchirieri
        :return:
        """
        return self.__links.get_num_links()

    def get_link_list(self):
        """
        Returneaza lista de inchirieri
        :return:
        """
        return self.__links.get_link_list()

    def get_id_clients(self):
        """
        Returneaza id-ul clientilor
        :return:
        """
        return self.__links.get_id_clients()
