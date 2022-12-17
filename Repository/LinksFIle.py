from Domain.Link import Link
from Repository.ClientsFIle import ClientsFile

class LinksFile:
    def __init__(self, file):
        self.__filename = file

    def build_links(self, id, id_c, id_m):
        id = int(id)
        id_c = int(id_c)
        id_m = int(id_m)
        lk = Link()
        lk.set_id_link(id)
        lk.set_id_movie(id_m)
        lk.set_id_client(id_c)

        return lk

    def load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except:
            print("Maybe this file is corrupted!")
            return

        links = []
        lines = f.readlines()
        for line in lines:
            id, id_c, id_m, _ = line.split(';')
            lk = self.build_links(id, id_c, id_m)
            links.append(lk)
        f.close()

        return links

    def save_to_file(self, link_list):
        with open(self.__filename, 'w') as f:
            for link in link_list:
                link_string = str(link.get_id()) + ';' + str(link.get_id_client()) + ';' + str(link.get_id_movie()) + ';' + '\n'
                f.write(link_string)

    def get_link_list(self):
        return self.load_from_file()

    def add_link(self, id_c, id_m):
        all_links = self.get_link_list()
        if(self.get_num_links(all_links) == 0):
            id = 1
        else:
            id = self.get_link_list()[-1].get_id() + 1
        lk = self.build_links(id, id_c, id_m)
        if(lk in all_links):
            print("Inchirierea este deja existenta")
            return
        all_links.append(lk)
        self.save_to_file(all_links)

    def get_link_by_id(self, id):
        """
        Returneaza un link dupa id
        :param id:
        :return:
        """
        all_links = self.get_link_list()
        for link in all_links:
            if (link.get_id() == id):
                return link

    def del_link(self, id):
        """
        Sterge o inchirirere
        :param id:
        :return:
        """
        all_links = self.get_link_list()
        link = self.get_link_by_id(id)
        all_links.pop(id - 1)
        self.save_to_file(all_links)

    def dict_for_most_rented_movies(self):
        all_links = self.get_link_list()
        dict_movies = dict()
        for link in all_links:
            movie_id = link.get_id_movie()
            if (movie_id in dict_movies):
                dict_movies[movie_id] += 1
            else:
                dict_movies[movie_id] = 1

        return dict_movies

    def get_link_pos(self, all_links, i):
        """
        Returneaza pozitia unei inchirieri in lista
        :param i:
        :return:
        """
        return all_links[i]

    def get_num_links(self, all_links):
        return len(all_links)

    def del_link_client(self, client_id):
        """
        Sterge inchirierea unui client
        :param client_id:
        :return:
        """
        all_links = self.get_link_list()
        i = 0
        while (i < self.get_num_links(all_links)):
            link = self.get_link_pos(all_links, i)
            if (link.get_id_client() == client_id):
                all_links.pop(i)
            else:
                i += 1
        self.save_to_file(all_links)

    def del_link_movie(self, movie_id):
        """
        Sterge inchirierea dupa id-ul filmului
        :param movie_id:
        :return:
        """
        all_links = self.get_link_list()
        i = 0
        while (i < self.get_num_links(all_links)):
            link = self.get_link_pos(all_links, i)
            if (link.get_id_movie() == movie_id):
                all_links.remove(link)
            else:
                i += 1

        self.save_to_file(all_links)

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

    def get_id_clients(self):
        """
        Returneaza id-ul clientilor
        :return:
        """
        all_links = self.get_link_list()
        clients_id = set()
        for link in all_links:
            clients_id.add(link.get_id_client())

        return clients_id