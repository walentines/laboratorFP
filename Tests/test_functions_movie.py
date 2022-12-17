from Repository.MoviesFIle import MoviesFile
from Domain.Movie import Movie
from Services.ServiceMFile import service_movies_file
import unittest

class TestMovieDomain(unittest.TestCase):
    def test_get_id(self):
        mv = Movie()
        new_id = 1
        mv.set_id(new_id)
        self.assertEqual(mv.get_id(), new_id)

    def test_get_title(self):
        mv = Movie()
        new_title = "The Nun"
        mv.set_title(new_title)
        self.assertEqual(mv.get_title(), new_title)

    def test_get_description(self):
        mv = Movie()
        new_description = "hello world"
        mv.set_description(new_description)
        self.assertEqual(mv.get_description(), new_description)

    def test_get_type(self):
        mv = Movie()
        new_type = "horror"
        mv.set_type(new_type)
        self.assertEqual(mv.get_type(), new_type)

    def test_get_year(self):
        mv = Movie()
        new_year = 2000
        mv.set_year(new_year)
        self.assertEqual(mv.get_year(), new_year)

    def test_set_id(self):
        mv = Movie()
        new_id = 1
        mv.set_id(new_id)
        self.assertEqual(mv.get_id(), new_id)

    def test_set_title(self):
        mv = Movie()
        new_title = "The Nun"
        mv.set_title(new_title)
        self.assertEqual(mv.get_title(), new_title)

    def test_set_description(self):
        mv = Movie()
        new_description = "hello world"
        mv.set_description(new_description)
        self.assertEqual(mv.get_description(), new_description)

    def test_set_type(self):
        mv = Movie()
        new_type = "horror"
        mv.set_type(new_type)
        self.assertEqual(mv.get_type(), new_type)

    def test_set_year(self):
        mv = Movie()
        new_year = 2000
        mv.set_year(new_year)
        self.assertEqual(mv.get_year(), new_year)



class TestMovieFileRepo(unittest.TestCase):

    def test_load_from_file(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        movies = file.load_from_file()
        num_movies = 8
        self.assertEqual(len(movies), num_movies)

    def test_get_movie_list(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        movies = file.get_movie_list()
        num_movies = 8
        self.assertEqual(len(movies), num_movies)

    def test_get_movie_pos(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        movies = file.get_movie_list()
        movie_pos = 0
        correct_id = 1
        movie = file.get_movie_pos(movies, movie_pos)
        movie_id = movie.get_id()
        self.assertEqual(movie_id, correct_id)

    def test_add_movie(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        prev_movies = file.get_movie_list()
        file.add_movie(256, "The", "iaenge", "hi", 2006)
        movies = file.get_movie_list()
        num_movies = 9
        self.assertEqual(len(movies), num_movies)
        file.save_to_file(prev_movies)

    def test_del_movie_by_id(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        prev_movies = file.get_movie_list()
        id = file.del_movie_by_id(1)
        movies = file.get_movie_list()
        correct_len = 7
        self.assertEqual(len(movies), correct_len)
        file.save_to_file(prev_movies)

    def test_del_movie_by_title(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        prev_movies = file.get_movie_list()
        id = file.del_movie_by_title("Spiderman")
        movies = file.get_movie_list()
        correct_len = 6
        self.assertEqual(len(movies), correct_len)
        file.save_to_file(prev_movies)

    def test_del_movie_by_description(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        prev_movies = file.get_movie_list()
        id = file.del_movie_by_description("Interesting")
        movies = file.get_movie_list()
        correct_len = 7
        self.assertEqual(len(movies), correct_len)
        file.save_to_file(prev_movies)

    def test_del_movie_by_year(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        prev_movies = file.get_movie_list()
        id = file.del_movie_by_year(2018)
        movies = file.get_movie_list()
        correct_len = 7
        self.assertEqual(len(movies), correct_len)
        file.save_to_file(prev_movies)

    def test_mod_movie_title(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        file.mod_movie_title(8, "Salut")
        self.assertEqual(file.get_movie_by_id(8).get_title(), "Salut")

    def test_mod_movie_description(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        file.mod_movie_description(8, "Salut")
        self.assertEqual(file.get_movie_by_id(8).get_description(), "Salut")

    def test_mod_movie_type(self):
        file = MoviesFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/movies_test.txt')
        file.mod_movie_type(8, "Salut")
        self.assertEqual(file.get_movie_by_id(8).get_type(), "Salut")

class TestMovieService(unittest.TestCase):
    def setUp(self) -> None:
        self.__serviceM = service_movies_file(" ")

    def test_add_movie(self):
        id = 1
        title = "The Nun"
        description = "This is a description"
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)
        self.assertEqual(self.__serviceM.get_num_movies(), 1)

    def test_del_movie_by_id(self):
        id = 1
        self.__serviceM.del_movie_by_id(id)
        self.assertEqual(self.__serviceM.get_num_movies(), 0)

    def test_del_movie_by_title(self):
        id = 1
        title = "The Nun"
        description = "This is a description"
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)
        self.__serviceM.del_movie_by_title("The Nun")
        self.assertEqual(self.__serviceM.get_num_movies(), 0)

    def test_del_movie_by_description(self):
        id = 1
        title = "The Nun"
        description = "This is a description"
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)
        self.__serviceM.del_movie_by_description("This is a description")
        self.assertEqual(self.__serviceM.get_num_movies(), 0)

    def test_del_movie_by_type(self):
        id = 1
        title = "The Nun"
        description = "This is a description"
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)
        self.__serviceM.del_movie_by_type("horror")
        self.assertEqual(self.__serviceM.get_num_movies(), 0)

    def test_del_movie_by_year(self):
        id = 1
        title = "The Nun"
        description = "This is a description"
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)
        self.__serviceM.del_movie_by_year(2020)
        self.assertEqual(self.__serviceM.get_num_movies(), 0)

    def test_mod_movie_title(self):
        id = 1
        title = "The Nun"
        description = "This is a description"
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)
        self.__serviceM.mod_movie_title(id, "The Nun 2")
        self.assertEqual(self.__serviceM.get_movie_by_id(id).get_title(), "The Nun 2")

    def test_mod_movie_description(self):
        id = 1
        title = "The Nun"
        description = "This is a description"
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)
        self.__serviceM.mod_movie_description(id, "The Nun 2")
        self.assertEqual(self.__serviceM.get_movie_by_id(id).get_description(), "The Nun 2")

    def test_mod_movie_type(self):
        id = 1
        title = "The Nun"
        description = "This is a description"
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)
        self.__serviceM.mod_movie_type(id, "The Nun 2")
        self.assertEqual(self.__serviceM.get_movie_by_id(id).get_type(), "The Nun 2")

    def test_mod_movie_year(self):
        id = 1
        title = "The Nun"
        description = "This is a description"
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)
        self.__serviceM.mod_movie_year(id, 1999)
        self.assertEqual(self.__serviceM.get_movie_by_id(id).get_year(), 1999)
