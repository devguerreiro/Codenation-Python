class Department:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    def get_department(self):
        return self.__name

    def set_department(self, value):
        self.__name = value
