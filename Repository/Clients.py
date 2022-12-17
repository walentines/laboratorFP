from Domain.Client import Client
from Utils.validation_functions import *


class Clients:
    def __init__(self):
        self.__clients_list = list()

    def check_if_id_exists(self, new_id):
        for client in self.__clients_list:
            if(client.get_id() == new_id):
                return True

        return False

    def verify_id(self, new_id):
        """
        Verifica daca id-ul este valid
        :param new_id:
        :return: True/False
        """
        if self.check_if_id_exists(new_id):
           print("ID-ul exista deja in lista!")
           return False

        return True


    def verify_cnp(self, new_cnp):
        """
        Verifica daca cnp-ul este valid
        :param new_cnp:
        :return: True/False
        """
        for client in self.__clients_list:
            if (client.get_cnp() == new_cnp):
                print("CNP-ul exista deja in lista!")
                return False

        return True

    def add_client(self, id, name, cnp, age):
        """
        Adauga client
        :param id:
        :param name:
        :param cnp:
        :param age:
        :return:
        """
        new_client = Client()
        new_client.set_id(id)
        new_client.set_name(name)
        new_client.set_cnp(cnp)
        new_client.set_age(age)
        self.__clients_list.append(new_client)

    def get_client_pos(self, i):
        """
        Returneaza pozitia unui client in lista
        :param i:
        :return:
        """
        return self.__clients_list[i]

    def del_client_by_id(self, client_id):
        """
        Sterge un client dupa id
        :param client_id:
        :return:
        """
        for client in self.__clients_list:
            if (client.get_id() == client_id):
                self.__clients_list.remove(client)

        return client_id

    def del_client_by_name(self, name):
        """
        Sterge un client dupa nume
        :param name:
        :return:
        """
        id_list = list()

        i = 0
        while (i < len(self.__clients_list)):
            client = self.get_client_pos(i)
            if (name.lower() in client.get_name().lower()):
                id_list.append(client.get_id())
                self.__clients_list.remove(client)
            else:
                i += 1

        return id_list

    def del_client_by_age(self, age):
        """
        Sterge un client dupa varsta
        :param age:
        :return:
        """
        id_list = list()

        i = 0
        while (i < len(self.__clients_list)):
            client = self.get_client_pos(i)
            if (age == client.get_age()):
                id_list.append(client.get_id())
                self.__clients_list.remove(client)
            else:
                i += 1

        return id_list

    def del_client_by_cnp(self, cnp):
        """
        Sterge un client dupa cnp
        :param cnp:
        :return:
        """
        id_list = list()

        i = 0
        while (i < len(self.__clients_list)):
            client = self.get_client_pos(i)
            if (cnp == client.get_cnp()):
                id_list.append(client.get_id())
                self.__clients_list.remove(client)
            else:
                i += 1

        return id_list

    def get_client_by_id(self, id):
        """
        Returneaza un client dupa id
        :param id:
        :return:
        """
        for client in self.__clients_list:
            if (client.get_id() == id):
                return client

    def get_num_clients(self):
        """
        Returneaza numarul de clienti
        :return:
        """
        return len(self.__clients_list)

    def mod_client_name(self, id, name):
        """
        Modifica numele unui client
        :param id:
        :param name:
        :return:
        """
        for client in self.__clients_list:
            if (client.get_id() == id):
                client.set_name(name)

    def mod_client_cnp(self, id, cnp):
        """
        Modifica cnp-ul unui client
        :param id:
        :param cnp:
        :return:
        """
        for client in self.__clients_list:
            if (client.get_id() == id):
                client.set_cnp(cnp)

    def mod_client_age(self, id, age):
        """
        Modifica varsta unui client
        :param id:
        :param age:
        :return:
        """
        for client in self.__clients_list:
            if (client.get_id() == id):
                client.set_age(age)

    def add_movie_client(self, id, movie_id):
        """
        Adauga un film pentru un client
        :param id:
        :param movie_id:
        :return:
        """
        for client in self.__clients_list:
            if (client.get_id() == id):
                client.add_movie_id(movie_id)

    def del_movie_client(self, id, movie_id):
        """
        Sterge un film pentru clientul cu id-ul respectiv
        :param id:
        :param movie_id:
        :return:
        """
        for client in self.__clients_list:
            if (client.get_id() == id):
                client.del_movie_id(movie_id)

    def get_clients_list(self):
        """
        Returneaza lista de clienti
        :return:
        """
        return self.__clients_list

    def search_client_by_name(self, name):
        """
        Cauta clienti dupa nume
        :param name:
        :return:
        """
        client_list = list()
        for client in self.__clients_list:
            if (name.lower() in client.get_name().lower()):
                client_list.append(client)

        return client_list

    def search_client_by_cnp(self, cnp):
        """
        Cauta clienti dupa cnp
        :param cnp:
        :return:
        """
        client_list = list()
        for client in self.__clients_list:
            if (cnp == client.get_cnp()):
                client_list.append(client)

        return client_list

    def search_client_by_age(self, age):
        """
        Cauta clienti dupa varsta
        :param age:
        :return:
        """
        client_list = list()
        for client in self.__clients_list:
            if (age == client.get_age()):
                client_list.append(client)

        return client_list