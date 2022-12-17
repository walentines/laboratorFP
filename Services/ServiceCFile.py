from Repository.ClientsFIle import ClientsFile
from main_with_generate import *
from Utils.validation_functions import *
from Repository.Clients import Clients

class service_clients_file:
    def __init__(self, mode):
        if(mode == "file"):
            self.__clients = ClientsFile('Data/clients.txt')
        else:
            self.__clients = Clients()

    def generate_clients(self, num_clients):
        cls = generate_multiple_clients(num_clients)

        return cls

    def check_if_id_exists(self, new_id):
        return self.__clients.check_if_id_exists(new_id)

    def verify_id(self, new_id):
        """
        Verifica daca id-ul este valid
        :param new_id:
        :return: True/False
        """
        return self.__clients.verify_id(new_id)

    def verify_cnp(self, new_cnp):
        """
        Verifica daca cnp-ul este valid
        :param new_cnp:
        :return: True/False
        """
        return self.__clients.verify_cnp(new_cnp)

    def add_client(self, id, name, cnp, age):
        """
        Adauga client
        :param id:
        :param name:
        :param cnp:
        :param age:
        :return:
        """
        val_id = validate_id_year(id)
        val_age = validate_id_year(age)
        val_cnp = validate_cnp(cnp)
        if (val_id == False or val_age == False or val_cnp == False):
            return

        id = int(id)
        age = int(age)
        cnp = int(cnp)

        if (self.verify_id(id) == False or self.verify_cnp(cnp) == False):
            return

        self.__clients.add_client(id, name, cnp, age)

    def del_client_by_id(self, client_id):
        """
        Sterge un client dupa id
        :param client_id:
        :return:
        """
        val_id = validate_id_year(client_id)
        if (val_id == False):
            return

        client_id = int(client_id)

        client_id = self.__clients.del_client_by_id(client_id)

        return client_id

    def del_client_by_name(self, name):
        """
        Sterge un client dupa nume
        :param name:
        :return:
        """
        id_list = self.__clients.del_client_by_name(name)

        return id_list

    def del_client_by_age(self, age):
        """
        Sterge un client dupa varsta
        :param age:
        :return:
        """
        val_age = validate_id_year(age)
        if (val_age == False):
            return

        age = int(age)

        id_list = self.__clients.del_client_by_age(age)

        return id_list

    def del_client_by_cnp(self, cnp):
        """
        Sterge un client dupa cnp
        :param cnp:
        :return:
        """
        val_cnp = validate_cnp(cnp)
        if (val_cnp == False):
            return

        cnp = int(cnp)

        id_list = self.__clients.del_client_by_cnp(cnp)

        return id_list

    def get_client_by_id(self, id):
        """
        Returneaza un client dupa id
        :param id:
        :return:
        """
        val_id = validate_id_year(id)
        if (val_id == False):
            return

        id = int(id)

        client = self.__clients.get_client_by_id(id)

        return client

    def mod_client_name(self, id, name):
        """
        Modifica numele unui client
        :param id:
        :param name:
        :return:
        """
        val_id = validate_id_year(id)
        if (val_id == False):
            return

        id = int(id)

        self.__clients.mod_client_name(id, name)

    def mod_client_cnp(self, id, cnp):
        """
        Modifica cnp-ul unui client
        :param id:
        :param cnp:
        :return:
        """
        val_id = validate_id_year(id)
        val_cnp = validate_cnp(cnp)
        if (val_id == False or val_cnp == False):
            return

        id = int(id)
        cnp = int(cnp)

        self.__clients.mod_client_cnp(id, cnp)

    def mod_client_age(self, id, age):
        """
        Modifica varsta unui client
        :param id:
        :param age:
        :return:
        """
        val_id = validate_id_year(id)
        val_age = validate_id_year(age)
        if (val_id == False or val_age == False):
            return

        id = int(id)
        age = int(age)

        self.__clients.mod_client_age(id, age)

    def add_movie_client(self, id, movie_id):
        """
        Adauga un film pentru un client
        :param id:
        :param movie_id:
        :return:
        """
        val_id = validate_id_year(id)
        val_mv_id = validate_id_year(movie_id)
        if (val_id == False or val_mv_id == False):
            return

        id = int(id)
        movie_id = int(movie_id)

        self.__clients.add_movie_client(id, movie_id)

    def del_movie_client(self, id, movie_id):
        """
        Sterge un film pentru clientul cu id-ul respectiv
        :param id:
        :param movie_id:
        :return:
        """
        val_id = validate_id_year(id)
        val_mv_id = validate_id_year(movie_id)
        if (val_id == False or val_mv_id == False):
            return

        id = int(id)
        movie_id = int(movie_id)

        self.__clients.del_movie_client(id, movie_id)

    def search_client_by_id(self, id):
        """
        Cauta clienti dupa id
        :param id:
        :return:
        """
        val_id = validate_id_year(id)
        if (val_id == False):
            return

        id = int(id)

        return [self.get_client_by_id(id)]

    def search_client_by_name(self, name):
        """
        Cauta clienti dupa nume
        :param name:
        :return:
        """
        return self.__clients.search_client_by_name(name)

    def search_client_by_cnp(self, cnp):
        """
        Cauta clienti dupa cnp
        :param cnp:
        :return:
        """
        val_cnp = validate_cnp(cnp)
        if (val_cnp == False):
            return

        cnp = int(cnp)

        return self.__clients.search_client_by_cnp(cnp)

    def search_client_by_age(self, age):
        """
        Cauta clienti dupa varsta
        :param age:
        :return:
        """
        val_age = validate_id_year(age)
        if (val_age == False):
            return

        age = int(age)

        return self.__clients.search_client_by_age(age)

    def get_num_clients(self):
        """
        Returneaza numarul de clienti
        :return:
        """
        return self.__clients.get_num_clients()

    def get_clients_list(self):
        """
        Returneaza lista de clienti
        :return:
        """
        return self.__clients.get_clients_list()
