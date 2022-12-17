class Movie:
    def __init__(self):
        self.__id = -1
        self.__title = ""
        self.__description = ""
        self.__type = ""
        self.__year = 0

    def __str__(self):
        return "ID Film: " + str(self.__id) + "\n" + "Titlu Film: " + str(self.__title) + "\n" + "Descriere Film: " + str(self.__description) + "\n" + "Tip Film: " + str(self.__type) + "\n" + "An aparitie Film: " + str(self.__year)

    def __eq__(self, mv1):
        return self.__id == mv1.get_id()

    def get_id(self):
        """
        Returneaza id-ul filmului
        :return:
        """
        return self.__id

    def get_title(self):
        """
        Returneaza titlul filmului
        :return:
        """
        return self.__title

    def get_description(self):
        """
        Returneaza descrierea filmului
        :return:
        """
        return self.__description

    def get_type(self):
        """
        Returneaza genul filmului
        :return:
        """
        return self.__type

    def get_year(self):
        """
        Returneaza anul filmului
        :return:
        """
        return self.__year

    def set_id(self, new_id):
        """
        Seteaza id-ul unui film
        :param new_id:
        :return:
        """
        self.__id = new_id

    def set_title(self, new_title):
        """
        Seteaza titlul
        :param new_title:
        :return:
        """
        self.__title = new_title

    def set_description(self, new_description):
        """
        Seteaza descrierea
        :param new_description:
        :return:
        """
        self.__description = new_description

    def set_type(self, new_type):
        """
        Seteaza genul
        :param new_type:
        :return:
        """
        self.__type = new_type

    def set_year(self, new_year):
        """
        Seteaza anul
        :param new_year:
        :return:
        """
        self.__year = new_year
