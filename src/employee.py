from .person import Person


class Employee(Person):
    def __init__(self, first_name, last_name, employee_id, salary):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        self.salary = salary

    def get_salary(self):
        return f'{self.salary}'
