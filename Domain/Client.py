class Client:
    def __init__(self):
        # self.__id = -1
        # self.__name = ""
        # self.__cnp = 0
        # self.__age = 0
        # self.__movies = list()
        self.__dict = {"id": -1, "name": "", "cnp": 0, "age": 0, "movies": list()}

    def __str__(self):
        if(len(self.__dict["movies"]) > 0):
            # return "ID Client: " + str(self.__id) + "\n" + "Nume Client: " + str(self.__name) + "\n" + "CNP Client: " + str(self.__cnp) + "\n" + "Varsta Client: " + str(self.__age) + "\n" + "Numar filme inchiriate: " + str(self.get_movies_len())
            return "ID Client: " + str(self.__dict["id"]) + "\n" + "Nume Client: " + str(self.__dict["name"]) + "\n" + "CNP Client: " + str(self.__dict["cnp"]) + "\n" + "Varsta Client: " + str(self.__dict["age"]) + "\n" + "Numar filme inchiriate: " + str(self.get_movies_len())
        # return "ID Client: " + str(self.__id) + "\n" + "Nume Client: " + str(self.__name) + "\n" + "CNP Client: " + str(self.__cnp) + "\n" + "Varsta Client: " + str(self.__age) + "\n" + "Nu are filme inchiriate"
        return "ID Client: " + str(self.__dict["id"]) + "\n" + "Nume Client: " + str(self.__dict["name"]) + "\n" + "CNP Client: " + str(self.__dict["cnp"]) + "\n" + "Varsta Client: " + str(self.__dict["age"]) + "\n" + "Nu are filme inchiriate"

    def __eq__(self, cl1):
        # return self.__cnp == cl1.get_cnp()
        return self.__dict["cnp"] == cl1.get_cnp()

    def get_id(self):
        """
        Returneaza id
        :return:
        """
        # return self.__id
        return self.__dict["id"]

    def get_name(self):
        """
        Returneaza nume
        :return:
        """
        # return self.__name
        return self.__dict["name"]

    def get_cnp(self):
        """
        Returneaza cnp
        :return:
        """
        # return self.__cnp
        return self.__dict["cnp"]

    def get_age(self):
        """
        Returneaza varsta
        :return:
        """
        # return self.__age
        return self.__dict["age"]

    def get_movies_len(self):
        """
        Returneaza lungimea listei de filme
        :return:
        """
        # return len(self.__movies)
        return len(self.__dict["movies"])

    def set_id(self, new_id):
        """
        Seteaza id
        :param new_id:
        :return:
        """
        # self.__id = new_id
        self.__dict["id"] = new_id

    def set_name(self, new_name):
        """
        Seteaza nume
        :param new_name:
        :return:
        """
        # self.__name = new_name
        self.__dict["name"] = new_name

    def set_cnp(self, new_cnp):
        """
        Seteaza cnp
        :param new_cnp:
        :return:
        """
        # self.__cnp = new_cnp
        self.__dict["cnp"] = new_cnp

    def set_age(self, new_age):
        """
        Seteaza varsta
        :param new_age:
        :return:
        """
        # self.__age = new_age
        self.__dict["age"] = new_age

    def add_movie_id(self, new_movie_id):
        """
        Adauga film la lista de filme
        :param new_movie_id:
        :return:
        """
        # self.__movies.append(new_movie_id)
        self.__dict["movies"].append(new_movie_id)

    def del_movie_id(self, movie_id):
        """
        Sterge film din lista de filme
        :param movie_id:
        :return:
        """
        # self.__movies.remove(movie_id)
        self.__dict["movies"].remove(movie_id)

    def get_movie_id_list(self):
        """
        Returneaza lista de filme
        :return:
        """
        # return self.__movies
        return self.__dict["movies"]
