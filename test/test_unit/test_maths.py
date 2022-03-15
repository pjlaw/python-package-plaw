from python_package_plaw.maths import add_numbers, subtract_numbers

def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(10, 100) == 110

def test_subtract_numbers():
    assert subtract_numbers(1, 2) == -1
    assert subtract_numbers(10, 2) == 8
    