import unittest
from Repository.LinksFIle import LinksFile
from Repository.ClientsFIle import ClientsFile
from Repository.MoviesFIle import MoviesFile
from Services.ServiceLFile import service_links_file
from Services.ServiceMFile import service_movies_file
from Services.ServiceCFile import service_clients_file
from Domain.Link import Link

class TestLinkDomain(unittest.TestCase):
    def test_get_id(self):
        lk = Link()
        new_id = 1
        lk.set_id_link(new_id)
        self.assertEqual(lk.get_id(), new_id)

    def test_get_id_client(self):
        lk = Link()
        new_id_client = 1
        lk.set_id_client(new_id_client)
        self.assertEqual(lk.get_id_client(), new_id_client)

    def test_get_id_movie(self):
        lk = Link()
        new_id_movie = 1
        lk.set_id_movie(new_id_movie)
        self.assertEqual(lk.get_id_movie(), new_id_movie)

    def test_set_id(self):
        lk = Link()
        new_id = 1
        lk.set_id_link(new_id)
        self.assertEqual(lk.get_id(), new_id)

    def test_set_id_client(self):
        lk = Link()
        new_id_client = 1
        lk.set_id_client(new_id_client)
        self.assertEqual(lk.get_id_client(), new_id_client)

    def test_set_id_movie(self):
        lk = Link()
        new_id_movie = 1
        lk.set_id_movie(new_id_movie)
        self.assertEqual(lk.get_id_movie(), new_id_movie)

class TestLinkRepoFile(unittest.TestCase):
    def test_load_from_file(self):
        file = LinksFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/links_test.txt')
        links = file.load_from_file()
        num_links = 5
        self.assertEqual(len(links), num_links)
        file = LinksFile("gnaeiognea")
        self.assertEqual(file.load_from_file(), None)

    def test_get_link_list(self):
        file = LinksFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/links_test.txt')
        links = file.get_link_list()
        num_links = 5
        self.assertEqual(len(links), num_links)

    def test_add_link(self):
        file = LinksFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/links_test.txt')
        prev_links = file.get_link_list()
        file.add_link(1, 2)
        links = file.get_link_list()
        num_links = 6
        self.assertEqual(len(links), num_links)
        file.save_to_file(prev_links)

    def test_del_link(self):
        file = LinksFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/links_test.txt')
        prev_links = file.get_link_list()
        file.del_link(1)
        links = file.get_link_list()
        num_links = 4
        self.assertEqual(len(links), num_links)
        file.save_to_file(prev_links)

    def test_get_link_pos(self):
        file = LinksFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/links_test.txt')
        links = file.get_link_list()
        links_pos = 0
        correct_link_id = 1
        link = file.get_link_pos(links, links_pos)
        link_id = link.get_id()
        self.assertEqual(link_id, correct_link_id)

    def test_del_link_client(self):
        file = LinksFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/links_test.txt')
        prev_links = file.get_link_list()
        file.del_link_client(3)
        links = file.get_link_list()
        num_links = 4
        self.assertEqual(len(links), num_links)
        file.save_to_file(prev_links)

    def test_del_link_movie(self):
        file = LinksFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/links_test.txt')
        prev_links = file.get_link_list()
        file.del_link_movie(7)
        links = file.get_link_list()
        num_links = 3
        self.assertEqual(len(links), num_links)
        file.save_to_file(prev_links)

class TestLinkService(unittest.TestCase):
    def setUp(self) -> None:
        self.__serviceL = service_links_file(" ")
        self.__serviceM = service_movies_file(" ")
        self.__serviceC = service_clients_file(" ")

    def test_add_link(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)

        id = 1
        title = "The Nun"
        description = "This is a horror movie."
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)

        id_c = 1
        id_m = 1

        self.__serviceL.add_link(id_c, id_m, self.__serviceC, self.__serviceM)
        self.assertEqual(self.__serviceL.get_num_links(), 1)

        id_c = 2
        id_m = 1
        self.assertEqual(self.__serviceL.add_link(id_c, id_m, self.__serviceC, self.__serviceM), None)


    def test_del_link(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)

        id = 1
        title = "The Nun"
        description = "This is a horror movie."
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)

        id_c = 1
        id_m = 1

        self.__serviceL.add_link(id_c, id_m, self.__serviceC, self.__serviceM)
        self.__serviceL.del_link(1)
        self.assertEqual(self.__serviceL.get_num_links(), 0)

    def test_del_link_client(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)

        id = 1
        title = "The Nun"
        description = "This is a horror movie."
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)

        id_c = 1
        id_m = 1

        self.__serviceL.add_link(id_c, id_m, self.__serviceC, self.__serviceM)
        self.__serviceL.del_link_client(1)
        self.assertEqual(self.__serviceL.get_num_links(), 0)

    def test_del_link_movie(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)

        id = 1
        title = "The Nun"
        description = "This is a horror movie."
        type = "horror"
        year = 2020
        self.__serviceM.add_movie(id, title, description, type, year)

        id_c = 1
        id_m = 1

        self.__serviceL.add_link(id_c, id_m, self.__serviceC, self.__serviceM)
        self.__serviceL.del_link_movie(1)
        self.assertEqual(self.__serviceL.get_num_links(), 0)
