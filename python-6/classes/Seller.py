from classes import Department, Employee


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department("sellers", 2)
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value

    def get_departament(self):
        return self.__department.get_department()

    def set_departament(self, value):
        self.__department.set_department(value)

    def calc_bonus(self):
        return self.__sales * 0.15
