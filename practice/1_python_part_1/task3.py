"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
  words = []
  final = ''

  for line in lines:
    unique =[]
    temp = line.split()

    for i in temp:
      if i not in unique:
        unique.append(i)  
    if word_number > len(unique)-1:
      pass
    else:
      words.append(unique[word_number])

  for word in words:
    final = final + word +' '
  
  return final[:-1]
