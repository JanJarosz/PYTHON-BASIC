"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""


import pytest
from scripts.task_exceptions import division

def test_division_ok(capfd):
    division(10, 5)
    out, err = capfd.readouterr()
    assert out == 'Division Finished\n'
    assert division(10, 5) == 2

def test_division_by_zero(capfd):
    division(1, 0)
    out, err = capfd.readouterr()
    assert out == 'Division by 0\nDivision Finished\n'

def test_division_by_one(capfd):
    division(1, 1)
    out, err = capfd.readouterr()
    assert out == 'Deletion on 1 get the same result\nDivision Finished\n'




#or

    
'''
import pytest
from scripts.task_exceptions import division

ingridients = [
    (10, 5, 2),
    (10, 1, 10),
    (10, 0, None)
]

@pytest.mark.parametrize('a, b, quotient', ingridients)
def test_division(a, b, quotient):
    assert division(a, b ) == quotient


'''
