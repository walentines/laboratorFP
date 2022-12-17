from Repository.ClientsFIle import ClientsFile
from Domain.Client import Client
from Services.ServiceCFile import service_clients_file
import unittest


class TestClientDomain(unittest.TestCase):
    def test_get_id(self):
        cl = Client()
        new_id = 1
        cl.set_id(new_id)
        self.assertEqual(cl.get_id(), new_id)

    def test_get_name(self):
        cl = Client()
        new_name = "Vali"
        cl.set_name(new_name)
        self.assertEqual(cl.get_name(), new_name)

    def test_get_cnp(self):
        cl = Client()
        new_cnp = 5030917297316
        cl.set_cnp(new_cnp)
        self.assertEqual(cl.get_cnp(), new_cnp)

    def test_get_age(self):
        cl = Client()
        new_age = 19
        cl.set_age(new_age)
        self.assertEqual(cl.get_age(), new_age)

    def test_set_id(self):
        cl = Client()
        new_id = 1
        cl.set_id(new_id)
        self.assertEqual(cl.get_id(), new_id)

    def test_set_name(self):
        cl = Client()
        new_name = "Vali"
        cl.set_name(new_name)
        self.assertEqual(cl.get_name(), new_name)

    def test_set_cnp(self):
        cl = Client()
        new_cnp = 5030917297316
        cl.set_cnp(new_cnp)
        self.assertEqual(cl.get_cnp(), new_cnp)

    def test_set_age(self):
        cl = Client()
        new_age = 19
        cl.set_age(new_age)
        self.assertEqual(cl.get_age(), new_age)


class TestClientRepoFile(unittest.TestCase):
    def test_load_from_file(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        clients = file.load_from_file()
        num_clients = 10
        self.assertEqual(len(clients), num_clients)
        file = ClientsFile("hello")
        self.assertEqual(file.load_from_file(), None)

    def test_get_clients_list(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        clients = file.get_clients_list()
        num_clients = 10
        self.assertEqual(len(clients), num_clients)

    def test_get_client_pos(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        clients = file.get_clients_list()
        client_pos = 0
        correct_client_id = 1
        client = file.get_client_pos(clients, client_pos)
        client_id = client.get_id()
        self.assertEqual(client_id, correct_client_id)

    def test_add_client(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        prev_clients = file.get_clients_list()
        file.add_client(11, "Salut", 5030919297316, 19)
        clients = file.get_clients_list()
        num_clients = 11
        self.assertEqual(len(clients), num_clients)
        file.save_to_file(prev_clients)

    def test_del_client_by_id(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        prev_clients = file.get_clients_list()
        id = file.del_client_by_id(1)
        clients = file.get_clients_list()
        correct_len = 9
        self.assertEqual(len(clients), correct_len)
        file.save_to_file(prev_clients)

    def test_del_client_by_name(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        prev_clients = file.get_clients_list()
        id = file.del_client_by_name("Juice")
        clients = file.get_clients_list()
        correct_len = 9
        self.assertEqual(len(clients), correct_len)
        file.save_to_file(prev_clients)

    def test_del_client_by_cnp(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        prev_clients = file.get_clients_list()
        id = file.del_client_by_cnp(5030917297311)
        clients = file.get_clients_list()
        correct_len = 9
        self.assertEqual(len(clients), correct_len)
        file.save_to_file(prev_clients)

    def test_del_client_by_age(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        prev_clients = file.get_clients_list()
        id = file.del_client_by_age(25)
        clients = file.get_clients_list()
        correct_len = 9
        self.assertEqual(len(clients), correct_len)
        file.save_to_file(prev_clients)

    def test_mod_client_name(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        file.mod_client_name(9, "Popovici")
        self.assertEqual(file.get_client_by_id(9).get_name(), "Popovici")

    def test_mod_client_cnp(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        file.mod_client_cnp(9, 1234567891111)
        self.assertEqual(file.get_client_by_id(9).get_cnp(), 1234567891111)

    def test_mod_client_age(self):
        file = ClientsFile('/Users/valentinserban/Documents/fundamentele_programarii/laborator_7/Data/clients_test.txt')
        file.mod_client_age(9, 30)
        self.assertEqual(file.get_client_by_id(9).get_age(), 30)


class TestClientService(unittest.TestCase):
    def setUp(self) -> None:
        self.__serviceC = service_clients_file(" ")

    def test_add_client(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)
        self.assertEqual(self.__serviceC.get_num_clients(), 1)

    def test_del_client_by_id(self):
        id = 1
        self.__serviceC.del_client_by_id(id)
        self.assertEqual(self.__serviceC.get_num_clients(), 0)
        self.assertEqual(self.__serviceC.del_client_by_id("salut"), None)

    def test_del_client_by_name(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)
        self.__serviceC.del_client_by_name(name)
        self.assertEqual(self.__serviceC.get_num_clients(), 0)

    def test_del_client_by_cnp(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)
        self.__serviceC.del_client_by_cnp(cnp)
        self.assertEqual(self.__serviceC.get_num_clients(), 0)

    def test_del_client_by_age(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)
        self.__serviceC.del_client_by_age(age)
        self.assertEqual(self.__serviceC.get_num_clients(), 0)

    def test_mod_client_name(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)
        self.__serviceC.mod_client_name(1, "Valentin")
        self.assertEqual(self.__serviceC.get_client_by_id(1).get_name(), "Valentin")
        self.assertEqual(self.__serviceC.mod_client_name("salut", "Valentin"), None)

    def test_mod_client_cnp(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)
        self.__serviceC.mod_client_cnp(1, 1000000000000)
        self.assertEqual(self.__serviceC.get_client_by_id(1).get_cnp(), 1000000000000)

        self.__serviceC.mod_client_cnp(1, 5)
        self.assertEqual(self.__serviceC.mod_client_cnp(1, 5), None)

    def test_black_mod_client_age(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)
        self.__serviceC.mod_client_age(1, 20)
        self.assertEqual(self.__serviceC.get_client_by_id(1).get_age(), 20)

    def test_white_mod_client_age(self):
        id = 1
        name = "Serban"
        cnp = 5030917297316
        age = 19
        self.__serviceC.add_client(id, name, cnp, age)
        self.__serviceC.mod_client_age(1, 20)
        self.assertEqual(self.__serviceC.get_client_by_id(1).get_age(), 20)
        self.assertEqual(self.__serviceC.mod_client_age("salut", 20), None)
