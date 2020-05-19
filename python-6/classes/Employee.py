from abc import ABC, abstractmethod


# classes abstratas não podem ser instânciadas
class Employee(ABC):
    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self.__salary = salary

    # métodos abstratos devem ser implementados pela classe filho
    @abstractmethod
    def calc_bonus(self):
        pass

    # todos os funcionários terão 8 horas de carga horária
    def get_hours(self):
        return 8

    def get_salary(self):
        return self.__salary
