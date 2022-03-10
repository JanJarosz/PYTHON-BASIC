"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
  l = []
  with open(filename) as opened_file:
    for line in opened_file:
      l.append(line.replace('\n',''))
  for digit in l:
    if digit.isdigit() or digit.startswith('-') and digit [1:].isdigit() == True:
      l[l.index(digit)] = int(l[l.index(digit)])
    else:
      return print('Invalid file. Every line must be an integer')
  return (min(l),max(l))
