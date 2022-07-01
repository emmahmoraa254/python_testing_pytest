from .employee import Employee

E1 = Employee('Emmah', 'Moraa', '02', '500')


def test_employee_salary():

    assert E1.get_salary() == '500'


def test_full_name():

    assert E1.full_name() == 'Emmah Moraa'
