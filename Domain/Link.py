class Link:
    def __init__(self):
        self.__linkid = 0
        self.__linkc = 0
        self.__linkm = 0

    def __str__(self):
        return "Link_ID: " + str(self.__linkid) + "\n" + "Client_ID: " + str(self.__linkc) + "\n" + "Movie_ID: " + str(self.__linkm)

    def get_id_client(self):
        """
        returneaza id-ul clientului
        :return:
        """
        return self.__linkc

    def get_id_movie(self):
        """
        Returneaza id-ul filmului
        :return:
        """
        return self.__linkm

    def set_id_client(self, new_id):
        """
        Seteaza id-ul clientului
        :param new_id:
        :return:
        """
        self.__linkc = new_id

    def set_id_movie(self, new_id):
        """
        Seteaza id-ul filmului
        :param new_id:
        :return:
        """
        self.__linkm = new_id

    def get_id(self):
        """
        Returneaza id-ul inchirierii
        :return:
        """
        return self.__linkid

    def set_id_link(self, new_id):
        """
        Seteaza id-ul inchirierii
        :param new_id:
        :return:
        """
        self.__linkid = new_id
