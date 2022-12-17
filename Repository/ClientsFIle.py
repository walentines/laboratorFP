from Domain.Client import Client


class ClientsFile:
    def __init__(self, file):
        self.__filename = file

    def check_if_id_exists(self, new_id):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_id() == new_id):
                return True

        return False

    def build_client_movie(self, id, name, cnp, age, movies):
        id = int(id)
        cnp = int(cnp)
        age = int(age)
        cl = Client()
        cl.set_id(id)
        cl.set_name(name)
        cl.set_cnp(cnp)
        cl.set_age(age)
        if(len(movies[0]) == 0):
            return cl
        for m in movies:
            m = int(m)
            cl.add_movie_id(m)

        return cl

    def build_client(self, id, name, cnp, age):
        id = int(id)
        cnp = int(cnp)
        age = int(age)
        cl = Client()
        cl.set_id(id)
        cl.set_name(name)
        cl.set_cnp(cnp)
        cl.set_age(age)

        return cl

    def load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except:
            # raise ValueError("Maybe this file is corrupted")
            return

        clients = []
        lines = f.readlines()
        for line in lines:
            id, name, cnp, age, movies, _ = line.split(';')
            movies = movies.split(',')
            cl = self.build_client_movie(id, name, cnp, age, movies)
            clients.append(cl)
        f.close()

        return clients

    def movie_to_string(self, movie_id_list):
        s = ''
        for movie_id in range(0, len(movie_id_list) - 1):
            s += str(movie_id_list[movie_id]) + ','
        try:
            s += str(movie_id_list[-1])
        except:
            s = ''
        return s

    def save_to_file(self, client_list):
        with open(self.__filename, 'w') as f:
            for client in client_list:
                client_string = str(client.get_id()) + ';' + str(client.get_name()) + ';' + str(
                    client.get_cnp()) + ';' + str(client.get_age()) + ';' + self.movie_to_string(
                    client.get_movie_id_list()) + ';' + '\n'
                f.write(client_string)

    def add_client(self, id, name, cnp, age):
        client = self.build_client(id, name, cnp, age)
        all_clients = self.get_clients_list()
        if (client in all_clients):
            print("Client is duplicate!")
            return
        all_clients.append(client)
        self.save_to_file(all_clients)

    def get_client_pos(self, all_clients, i):
        """
        Returneaza pozitia unui client in lista
        :param i:
        :return:
        """
        return all_clients[i]

    def get_client_by_id(self, id):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_id() == id):
                return client

    def verify_id(self, id):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_id() == id):
                print("ID-ul exista deja in lista!")
                return False

        return True

    def verify_cnp(self, cnp):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_cnp() == cnp):
                print("CNP-ul exista deja in lista!")
                return False

        return True

    def get_clients_list(self):
        return self.load_from_file()

    def get_num_clients(self):
        return len(self.load_from_file())

    def del_client_by_id(self, id):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_id() == id):
                all_clients.remove(client)

        self.save_to_file(all_clients)

        return id

    def del_client_by_name(self, name):
        all_clients = self.get_clients_list()
        id_list = list()

        i = 0
        while (i < len(all_clients)):
            client = self.get_client_pos(all_clients, i)
            if (name.lower() in client.get_name().lower()):
                id_list.append(client.get_id())
                all_clients.remove(client)
            else:
                i += 1

        self.save_to_file(all_clients)

        return id_list

    def del_client_by_cnp(self, cnp):
        all_clients = self.get_clients_list()
        id_list = list()
        i = 0
        while (i < len(all_clients)):
            client = self.get_client_pos(all_clients, i)
            if (cnp == client.get_cnp()):
                id_list.append(client.get_id())
                all_clients.pop(i)
            else:
                i += 1
        self.save_to_file(all_clients)

        return id_list

    def del_client_by_age(self, age):
        all_clients = self.get_clients_list()
        id_list = list()

        i = 0
        while (i < len(all_clients)):
            client = self.get_client_pos(all_clients, i)
            if (age == client.get_age()):
                id_list.append(client.get_id())
                all_clients.remove(client)
            else:
                i += 1

        self.save_to_file(all_clients)

        return id_list

    def mod_client_name(self, id, name):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_id() == id):
                client.set_name(name)

        self.save_to_file(all_clients)

    def mod_client_cnp(self, id, cnp):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_id() == id):
                client.set_cnp(cnp)

        self.save_to_file(all_clients)

    def mod_client_age(self, id, age):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_id() == id):
                client.set_age(age)

        self.save_to_file(all_clients)

    def add_movie_client(self, id, movie_id):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_id() == id):
                client.add_movie_id(movie_id)

        self.save_to_file(all_clients)

    def del_movie_client(self, id, movie_id):
        all_clients = self.get_clients_list()
        for client in all_clients:
            if (client.get_id() == id):
                client.del_movie_id(movie_id)

        self.save_to_file(all_clients)

    def search_client_by_name(self, name):
        all_clients = self.get_clients_list()
        client_list = list()
        for client in all_clients:
            if (name.lower() in client.get_name().lower()):
                client_list.append(client)

        return client_list

    def search_client_by_cnp(self, cnp):
        all_clients = self.get_clients_list()
        client_list = list()
        for client in all_clients:
            if (cnp == client.get_cnp()):
                client_list.append(client)

        return client_list

    def search_client_by_age(self, age):
        all_clients = self.get_clients_list()
        client_list = list()
        for client in all_clients:
            if (age == client.get_age()):
                client_list.append(client)

        return client_list
