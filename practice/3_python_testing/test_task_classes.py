"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import pytest
import datetime as dt
from scripts.task_classes import Teacher
from scripts.task_classes import Student
from scripts.task_classes import Homework


# FIXTURES
@pytest.fixture()
def teacher():
    return Teacher('Johnny', "Bean")

@pytest.fixture()
def homework():
    return Homework('do somersault', 0)

@pytest.fixture()
def student():
    return Student('Donald', 'Duck')



#TESTS
def test_teacher_name(teacher):
    assert teacher.first_name == 'Johnny' and teacher.last_name == "Bean"

def test_teacher_create_homework(homework):
    assert homework.text == 'do somersault' and homework.number_of_days == 0

def test_student_name(student):
    assert student.first_name == 'Donald' and student.last_name == 'Duck'

def test_student_do_homework(capfd, homework, student):
    student.do_homework(homework)
    out, err = capfd.readouterr()
    assert out == "You are late\n"

def test_homework_init(homework):
    assert homework.text == 'do somersault'
    assert homework.number_of_days == 0
    assert  homework.deadline == homework.created + dt.timedelta(days = 0)

def test_homework_is_active(homework):
    assert homework.is_active() == False
