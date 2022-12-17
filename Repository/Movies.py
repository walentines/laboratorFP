from Domain.Movie import Movie
from Utils.validation_functions import *


class Movies:
    def __init__(self):
        self.__movies_list = list()

    def check_if_id_exists(self, new_id):
        for movie in self.__movies_list:
            if (movie.get_id() == new_id):
                return True

        return False

    def verify_id(self, new_id):
        """
        Verifica id-ul filmului
        :param new_id:
        :return:
        """
        for movie in self.__movies_list:
            if (movie.get_id() == new_id):
                print("ID-ul exista deja in lista!")
                return False

        return True

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
        new_movie = Movie()
        new_movie.set_id(id)
        new_movie.set_title(title)
        new_movie.set_description(description)
        new_movie.set_type(type)
        new_movie.set_year(year)
        self.__movies_list.append(new_movie)

    def get_movie_pos(self, i):
        """
        Returneaza pozitia unui film in lista de filme
        :param i:
        :return:
        """
        return self.__movies_list[i]

    def del_movie_by_id(self, movie_id):
        """
        Sterge un film dupa id
        :param movie_id:
        :return:
        """
        for movie in self.__movies_list:
            if (movie.get_id() == movie_id):
                self.__movies_list.remove(movie)

        return movie_id

    def del_movie_by_title(self, title):
        """
        Sterge un film dupa titlu
        :param title:
        :return:
        """
        id_del = list()
        i = 0
        while (i < len(self.__movies_list)):
            movie = self.get_movie_pos(i)
            if (title.lower() in movie.get_title().lower()):
                id_del.append(movie.get_id())
                self.__movies_list.remove(movie)
            else:
                i += 1

        return id_del

    def del_movie_by_description(self, word):
        """
        Sterge un film dupa descriere
        :param word:
        :return:
        """
        id_del = list()
        i = 0
        while (i < len(self.__movies_list)):
            movie = self.get_movie_pos(i)
            if (word.lower() in movie.get_description().lower()):
                id_del.append(movie.get_id())
                self.__movies_list.remove(movie)
            else:
                i += 1

        return id_del

    def del_movie_by_type(self, type):
        """
        Sterge un film dupa gen
        :param type:
        :return:
        """
        id_del = list()
        i = 0
        while (i < len(self.__movies_list)):
            movie = self.get_movie_pos(i)
            if (type == movie.get_type()):
                id_del.append(movie.get_id())
                self.__movies_list.remove(movie)
            else:
                i += 1

        return id_del

    def del_movie_by_year(self, year):
        """
        Sterge un film dupa an
        :param year:
        :return:
        """
        id_del = list()

        i = 0
        while (i < len(self.__movies_list)):
            movie = self.get_movie_pos(i)
            if (year == movie.get_year()):
                id_del.append(movie.get_id())
                self.__movies_list.remove(movie)
            else:
                i += 1

        return id_del

    def get_num_movies(self):
        """
        Returneaza numarul de filme
        :return:
        """
        return len(self.__movies_list)

    def get_movie_by_id(self, searched_id):
        """
        Returneaza un film dupa id
        :param searched_id:
        :return:
        """
        for movie in self.__movies_list:
            if (movie.get_id() == searched_id):
                return movie

    def mod_movie_title(self, id, new_title):
        """
        Modifica titlul unui film
        :param id:
        :param new_title:
        :return:
        """

        for movie in self.__movies_list:
            if (movie.get_id() == id):
                movie.set_title(new_title)

    def mod_movie_description(self, id, new_description):
        """
        Modifica descrierea unui film
        :param id:
        :param new_description:
        :return:
        """
        for movie in self.__movies_list:
            if (movie.get_id() == id):
                movie.set_description(new_description)

    def mod_movie_type(self, id, new_type):
        """
        Modifica genul unui film
        :param id:
        :param new_type:
        :return:
        """
        for movie in self.__movies_list:
            if (movie.get_id() == id):
                movie.set_type(new_type)

    def mod_movie_year(self, id, new_year):
        """
        Modifica anul unui film
        :param id:
        :param new_year:
        :return:
        """
        for movie in self.__movies_list:
            if (movie.get_id() == id):
                movie.set_year(new_year)

    def search_movie_by_title(self, title):
        """
        Cauta film dupa titlu
        :param title:
        :return:
        """
        movie_list = list()
        for movie in self.__movies_list:
            if (title.lower() in movie.get_title().lower()):
                movie_list.append(movie)

        return movie_list

    def search_movie_by_description(self, description):
        """
        Cauta film dupa descriere
        :param description:
        :return:
        """
        movie_list = list()
        for movie in self.__movies_list:
            if (description.lower() in movie.get_description().lower()):
                movie_list.append(movie)

        return movie_list

    def search_movie_by_type(self, type):
        """
        Cauta film dupa gen
        :param type:
        :return:
        """
        movie_list = list()
        for movie in self.__movies_list:
            if (type == movie.get_type()):
                movie_list.append(movie)

        return movie_list

    def search_movie_by_year(self, year):
        """
        Cauta film dupa an
        :param year:
        :return:
        """
        movie_list = list()
        for movie in self.__movies_list:
            if (year == movie.get_year()):
                movie_list.append(movie)

        return movie_list

    def get_movie_list(self):
        """
        Returneaza lista de filme
        :return:
        """
        return self.__movies_list
