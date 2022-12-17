from Repository.Movies import Movies
from main_with_generate import *
from Utils.validation_functions import *


class service_movies:
    def __init__(self):
        self.__movies = Movies()

    def generate_movies(self, num_movies):
        mvs = generate_multiple_movies(num_movies)

        return mvs

    def verify_id(self, new_id):
        """
        Verifica id-ul filmului
        :param new_id:
        :return:
        """
        return self.__movies.verify_id(new_id)

    def check_if_id_exists(self, new_id):

        return self.__movies.check_if_id_exists(new_id)

    def add_movie(self, id, title, description, type, year):
        """
        Adauga film
        :param id:
        :param title:
        :param description:
        :param type:
        :param year:
        :return:
        """
        val_id = validate_id_year(id)
        val_year = validate_id_year(year)
        if (val_id == False or val_year == False):
            return

        id = int(id)
        year = int(year)

        if (self.verify_id(id) == False):
            return

        self.__movies.add_movie(id, title, description, type, year)

    def del_movie_by_id(self, movie_id):
        """
        Sterge un film dupa id
        :param movie_id:
        :return:
        """
        val_id = validate_id_year(movie_id)
        if (val_id == False):
            return

        movie_id = int(movie_id)

        movie_id = self.__movies.del_movie_by_id(movie_id)

        return movie_id

    def del_movie_by_title(self, title):
        """
        Sterge un film dupa titlu
        :param title:
        :return:
        """
        id_del = self.__movies.del_movie_by_title(title)

        return id_del

    def del_movie_by_description(self, word):
        """
        Sterge un film dupa descriere
        :param word:
        :return:
        """
        id_del = self.__movies.del_movie_by_description(word)

        return id_del

    def del_movie_by_type(self, type):
        """
        Sterge un film dupa gen
        :param type:
        :return:
        """
        id_del = self.__movies.del_movie_by_type(type)

        return id_del

    def del_movie_by_year(self, year):
        """
        Sterge un film dupa an
        :param year:
        :return:
        """
        val_year = validate_id_year(year)
        if (val_year == False):
            return

        year = int(year)

        id_del = self.__movies.del_movie_by_year(year)

        return id_del

    def get_num_movies(self):
        """
        Returneaza numarul de filme
        :return:
        """
        return self.__movies.get_num_movies()

    def get_movie_by_id(self, searched_id):
        """
        Returneaza un film dupa id
        :param searched_id:
        :return:
        """
        return self.__movies.get_movie_by_id(searched_id)

    def mod_movie_title(self, id, new_title):
        """
        Modifica titlul unui film
        :param id:
        :param new_title:
        :return:
        """
        val_id = validate_id_year(id)
        if (val_id == False):
            return

        id = int(id)

        self.__movies.mod_movie_title(id, new_title)

    def mod_movie_description(self, id, new_description):
        """
        Modifica descrierea unui film
        :param id:
        :param new_description:
        :return:
        """
        val_id = validate_id_year(id)
        if (val_id == False):
            return

        id = int(id)

        self.__movies.mod_movie_description(id, new_description)

    def mod_movie_type(self, id, new_type):
        """
        Modifica genul unui film
        :param id:
        :param new_type:
        :return:
        """
        val_id = validate_id_year(id)
        if (val_id == False):
            return

        id = int(id)

        self.__movies.mod_movie_type(id, new_type)

    def mod_movie_year(self, id, new_year):
        """
        Modifica anul unui film
        :param id:
        :param new_year:
        :return:
        """
        val_id = validate_id_year(id)
        if (val_id == False):
            return

        id = int(id)

        self.__movies.mod_movie_year(id, new_year)

    def search_movie_by_id(self, id):
        """
        Cauta film dupa id
        :param id:
        :return:
        """
        val_id = validate_id_year(id)
        if (val_id == False):
            return

        id = int(id)

        return [self.get_movie_by_id(id)]

    def search_movie_by_title(self, title):
        """
        Cauta film dupa titlu
        :param title:
        :return:
        """
        return self.__movies.search_movie_by_title(title)

    def search_movie_by_description(self, description):
        """
        Cauta film dupa descriere
        :param description:
        :return:
        """
        return self.__movies.search_movie_by_description(description)

    def search_movie_by_type(self, type):
        """
        Cauta film dupa gen
        :param type:
        :return:
        """
        return self.__movies.search_movie_by_type(type)

    def search_movie_by_year(self, year):
        """
        Cauta film dupa an
        :param year:
        :return:
        """
        val_year = validate_id_year(year)
        if (val_year == False):
            return

        year = int(year)

        return self.__movies.search_movie_by_year(year)

    def movies_by_id(self, id_list):
        """
        Returneaza lista de filme dupa id
        :param id_list:
        :return:
        """
        movie_list = list()
        for id in id_list:
            movie = self.get_movie_by_id(id)
            movie_list.append(movie)

        return movie_list

    def get_movie_list(self):
        """
        Returneaza lista de filme
        :return:
        """
        return self.__movies.get_movie_list()

