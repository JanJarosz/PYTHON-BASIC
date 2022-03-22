"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import pytest
import os
import tempfile


l = []
os.chdir('path') #path to folder with  files
for file in os.listdir('path'):
    with open(file) as f:
        l.append(f.read())

temp = tempfile.NamedTemporaryFile()
with open(temp.name, 'w') as fp:
    fp.write(','.join(l))

with open(temp.name) as fp:
    check = fp.read().strip().split(',')
results = list(map(int, check))



def test_read_filesfromtask():
    assert results == [59,99,14,1,95,99,80,66,37,15,91,74,67,39,90,40,32,69,48,82]# or other numbers which you expect
