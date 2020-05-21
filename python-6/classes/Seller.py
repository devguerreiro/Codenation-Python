from classes import Employee


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(
            code=code,
            name=name,
            salary=salary,
            department_name="sellers",
            department_code=2,
        )
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value

    def calc_bonus(self):
        return self.__sales * 0.15
