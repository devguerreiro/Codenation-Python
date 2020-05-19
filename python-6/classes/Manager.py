from classes import Department, Employee


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department("managers", 1)

    def calc_bonus(self):
        return round(self.get_salary() * 0.15, 3)

    def get_departament(self):
        return self.__department.get_department()

    def set_departament(self, value):
        self.__department.set_department(value)
