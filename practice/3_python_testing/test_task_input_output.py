"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
import pytest
from unittest import mock
from scripts import task_input_output

@mock.patch('scripts.task_input_output.get_input')
def test_read_numbers_without_text_input(mock_get_input):
    mock_get_input.return_value = [1, 2, 3, 4]
    assert task_input_output.read_numbers(4) == 2.5

@mock.patch('scripts.task_input_output.get_input')
def test_read_numbers_without_text_input(mock_get_input):
    mock_get_input.return_value = [1, 2, 3, 4]
    with pytest.raises(AssertionError):
        assert task_input_output.read_numbers(4) == 3.5

@mock.patch('scripts.task_input_output.get_input')
def test_read_numbers_with_text_input(mock_get_input):
    mock_get_input.return_value = [1, 2, 3, 4, 'abracadabra']
    assert task_input_output.read_numbers(5) == 2.5

@mock.patch('scripts.task_input_output.get_input')
def test_read_numbers_with_text_input(mock_get_input):
    mock_get_input.return_value = [1, 2, 3, 4, 'abracadabra']
    with pytest.raises(AssertionError):
        assert task_input_output.read_numbers(5) == 3.5


'''
I had to rewrite input_output task to this form:

def get_input(n):
    l = []
    for i in range(n):
        l.append(input('Enter yor number'))
    return l

def read_numbers(n: int) -> str:
    denominator = 0
    nominator = 0
    l = get_input(n)
    for item in l:
        try:
            nominator += float(item)
            denominator += 1
        except TypeError:
            pass
        except ValueError:
            pass
    try:
        average = nominator / denominator
    except ZeroDivisionError:
        print('No number entered')
        return None


    return average
'''
