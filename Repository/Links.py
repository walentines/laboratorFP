from Domain.Link import Link
from Utils.validation_functions import *

class Links:
    def __init__(self):
        self.__links = list()

    def add_link(self, id_c, id_m):
        """
        Adauga o inchiriere
        :param id_c:
        :param id_m:
        :return:
        """
        link = Link()
        link.set_id_client(id_c)
        link.set_id_movie(id_m)
        link.set_id_link(self.get_num_links() + 1)

        self.__links.append(link)

    def get_link_by_id(self, id):
        """
        Returneaza un link dupa id
        :param id:
        :return:
        """
        for link in self.__links:
            if (link.get_id() == id):
                return link

    def del_link(self, id):
        """
        Sterge o inchirirere
        :param id:
        :return:
        """
        link = self.get_link_by_id(id)
        self.__links.remove(link)

    def dict_for_most_rented_movies(self):
        dict_movies = dict()
        for link in self.__links:
            movie_id = link.get_id_movie()
            if (movie_id in dict_movies):
                dict_movies[movie_id] += 1
            else:
                dict_movies[movie_id] = 1

        return dict_movies

    def get_link_pos(self, i):
        """
        Returneaza pozitia unei inchirieri in lista
        :param i:
        :return:
        """
        return self.__links[i]

    def del_link_client(self, client_id):
        """
        Sterge inchirierea unui client
        :param client_id:
        :return:
        """
        i = 0
        while (i < self.get_num_links()):
            link = self.get_link_pos(i)
            if (link.get_id_client() == client_id):
                self.__links.remove(link)
            else:
                i += 1

    def del_link_movie(self, movie_id):
        """
        Sterge inchirierea dupa id-ul filmului
        :param movie_id:
        :return:
        """
        i = 0
        while (i < self.get_num_links()):
            link = self.get_link_pos(i)
            if (link.get_id_movie() == movie_id):
                self.__links.remove(link)
            else:
                i += 1

    def del_link_clients(self, clients_id):
        """
        Sterge inchirierile a mai multor clienti
        :param clients_id:
        :return:
        """
        for id in clients_id:
            self.del_link_client(id)

    def del_link_movies(self, movies_id):
        """
        Sterge inchirierile a mai multor filme
        :param movies_id:
        :return:
        """
        for id in movies_id:
            self.del_link_movie(id)

    def get_num_links(self):
        """
        Returneaza lungimea listei de inchirieri
        :return:
        """
        return len(self.__links)

    def get_link_list(self):
        """
        Returneaza lista de inchirieri
        :return:
        """
        return self.__links

    def get_id_clients(self):
        """
        Returneaza id-ul clientilor
        :return:
        """
        clients_id = set()
        for link in self.__links:
            clients_id.add(link.get_id_client())

        return clients_id
