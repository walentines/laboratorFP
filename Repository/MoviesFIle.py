from Domain.Movie import Movie

class MoviesFile:
    def __init__(self, file):
        self.__filename = file

    def build_movie(self, id, title, description, type, year):
        id = int(id)
        year = int(year)
        mv = Movie()
        mv.set_id(id)
        mv.set_title(title)
        mv.set_year(year)
        mv.set_description(description)
        mv.set_type(type)

        return mv

    def load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except:
            print("Maybe this file is corrupted!")
            return

        movies = []
        lines = f.readlines()
        for line in lines:
            id, title, description, type, year, _ = line.split(';')
            mv = self.build_movie(id, title, description, type, year)
            movies.append(mv)
        f.close()

        return movies

    def get_movie_list(self):

        return self.load_from_file()

    def get_movie_pos(self, all_movies, i):
        """
        Returneaza pozitia unui film in lista de filme
        :param i:
        :return:
        """
        return all_movies[i]

    def save_to_file(self, movie_list):
        with open(self.__filename, 'w') as f:
            for movie in movie_list:
                movie_string = str(movie.get_id()) + ';' + str(movie.get_title()) + ';' + str(
                    movie.get_description()) + ';' + str(movie.get_type()) + ';' + str(movie.get_year()) + ';' + '\n'
                f.write(movie_string)

    def add_movie(self, id, title, description, type, year):
        movie = self.build_movie(id, title, description, type, year)
        all_movies = self.get_movie_list()
        if(movie in all_movies):
            print("Movie is duplicated")
            return
        all_movies.append(movie)
        self.save_to_file(all_movies)

    def check_if_id_exists(self, new_id):
        all_movies = self.get_movie_list()
        for movie in all_movies:
            if (movie.get_id() == new_id):
                return True

        return False

    def verify_id(self, new_id):
        """
        Verifica id-ul filmului
        :param new_id:
        :return:
        """
        all_movies = self.get_movie_list()
        for movie in all_movies:
            if (movie.get_id() == new_id):
                print("ID-ul exista deja in lista!")
                return False

        return True

    def del_movie_by_id(self, id):
        all_movies = self.get_movie_list()
        for movie in all_movies:
            if (movie.get_id() == id):
                all_movies.remove(movie)

        self.save_to_file(all_movies)

        return id

    def del_movie_by_title(self, title):
        """
        Sterge un film dupa titlu
        :param title:
        :return:
        """
        all_movies = self.get_movie_list()
        id_del = list()
        i = 0
        while (i < len(all_movies)):
            movie = self.get_movie_pos(all_movies, i)
            if (title.lower() in movie.get_title().lower()):
                id_del.append(movie.get_id())
                all_movies.remove(movie)
            else:
                i += 1

        self.save_to_file(all_movies)

        return id_del

    def del_movie_by_description(self, word):
        """
        Sterge un film dupa descriere
        :param word:
        :return:
        """
        all_movies = self.get_movie_list()
        id_del = list()
        i = 0
        while (i < len(all_movies)):
            movie = self.get_movie_pos(all_movies, i)
            if (word.lower() in movie.get_description().lower()):
                id_del.append(movie.get_id())
                all_movies.remove(movie)
            else:
                i += 1

        self.save_to_file(all_movies)

        return id_del

    def del_movie_by_type(self, type):
        """
        Sterge un film dupa gen
        :param type:
        :return:
        """
        all_movies = self.get_movie_list()
        id_del = list()
        i = 0
        while (i < len(all_movies)):
            movie = self.get_movie_pos(all_movies, i)
            if (type == movie.get_type()):
                id_del.append(movie.get_id())
                all_movies.remove(movie)
            else:
                i += 1

        self.save_to_file(all_movies)

        return id_del

    def del_movie_by_year(self, year):
        """
        Sterge un film dupa an
        :param year:
        :return:
        """
        all_movies = self.get_movie_list()
        id_del = list()

        i = 0
        while (i < len(all_movies)):
            movie = self.get_movie_pos(all_movies, i)
            if (year == movie.get_year()):
                id_del.append(movie.get_id())
                all_movies.remove(movie)
            else:
                i += 1

        self.save_to_file(all_movies)

        return id_del

    def get_num_movies(self):
        """
        Returneaza numarul de filme
        :return:
        """
        return len(self.load_from_file())

    def get_movie_by_id(self, searched_id):
        """
        Returneaza un film dupa id
        :param searched_id:
        :return:
        """
        all_movies = self.get_movie_list()
        for movie in all_movies:
            if (movie.get_id() == searched_id):
                return movie

    def mod_movie_title(self, id, new_title):
        """
        Modifica titlul unui film
        :param id:
        :param new_title:
        :return:
        """
        all_movies = self.get_movie_list()
        for movie in all_movies:
            if (movie.get_id() == id):
                movie.set_title(new_title)

        self.save_to_file(all_movies)

    def mod_movie_description(self, id, new_description):
        """
        Modifica descrierea unui film
        :param id:
        :param new_description:
        :return:
        """
        all_movies = self.get_movie_list()
        for movie in all_movies:
            if (movie.get_id() == id):
                movie.set_description(new_description)

        self.save_to_file(all_movies)

    def mod_movie_type(self, id, new_type):
        """
        Modifica genul unui film
        :param id:
        :param new_type:
        :return:
        """
        all_movies = self.get_movie_list()
        for movie in all_movies:
            if (movie.get_id() == id):
                movie.set_type(new_type)

        self.save_to_file(all_movies)

    def mod_movie_year(self, id, new_year):
        """
        Modifica anul unui film
        :param id:
        :param new_year:
        :return:
        """
        all_movies = self.get_movie_list()
        for movie in all_movies:
            if (movie.get_id() == id):
                movie.set_year(new_year)

        self.save_to_file(all_movies)

    def search_movie_by_title(self, title):
        """
        Cauta film dupa titlu
        :param title:
        :return:
        """
        all_movies = self.get_movie_list()
        movie_list = list()
        for movie in all_movies:
            if (title.lower() in movie.get_title().lower()):
                movie_list.append(movie)

        return movie_list

    def search_movie_by_description(self, description):
        """
        Cauta film dupa descriere
        :param description:
        :return:
        """
        all_movies = self.get_movie_list()
        movie_list = list()
        for movie in all_movies:
            if (description.lower() in movie.get_description().lower()):
                movie_list.append(movie)

        return movie_list

    def search_movie_by_type(self, type):
        """
        Cauta film dupa gen
        :param type:
        :return:
        """
        all_movies = self.get_movie_list()
        movie_list = list()
        for movie in all_movies:
            if (type == movie.get_type()):
                movie_list.append(movie)

        return movie_list

    def search_movie_by_year(self, year):
        """
        Cauta film dupa an
        :param year:
        :return:
        """
        all_movies = self.get_movie_list()
        movie_list = list()
        for movie in all_movies:
            if (year == movie.get_year()):
                movie_list.append(movie)

        return movie_list