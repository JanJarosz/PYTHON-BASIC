"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
  final = ''
  unique =[]
  temp = line.split()
  for i in temp:
    if i not in unique:
      unique.append(i)  
  for word in unique:
    final = final + word +' '
  return final[:-1]

'''
or a littke bit simplier

def remove_duplicated_words(line: str) -> str:
  final = ''
  temp = line.split()
  unique = set(temp)
  for word in unique:
    final = final + word +' '
  return final[:-1]
'''
