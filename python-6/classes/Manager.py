from classes import Employee


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(
            code=code,
            name=name,
            salary=salary,
            department_name="managers",
            department_code=1,
        )

    def calc_bonus(self):
        return round(self.get_salary() * 0.15, 3)
