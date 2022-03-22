"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import os
import io
import tempfile


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

words = generate_words()
w1 = '\n'.join(words)
w2_temp = words[::-1]
w2 = ','.join(w2_temp)


temp1 = tempfile.NamedTemporaryFile()
temp2 = tempfile.NamedTemporaryFile()
with io.open(temp1.name, 'w', encoding = 'utf8') as f:
    f.write(w1)

with io.open(temp2.name, 'w', encoding = 'cp1252') as f:
    f.write(w2)

with open(temp1.name, 'r') as f:
    check1 = f.read().strip().split('\n')

with open(temp2.name, 'r') as f:
    check2 = f.read().strip().split(',')

def test_read_write2_newline_separated():
    assert check1 == words
def test_read_write2_comma_separated():
    assert check2 == words[::-1]
