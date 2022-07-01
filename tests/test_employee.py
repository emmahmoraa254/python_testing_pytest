from src.employee import Employee


def test_get_salary():
    E1 = Employee('Emmah', 'Moraa', '02', '500')

    assert E1.get_salary() == '500'



def test_full_name():
    E1 = Employee('Emmah', 'Moraa', '02', '500')

    assert E1.full_name() == 'Emmah Moraa'
