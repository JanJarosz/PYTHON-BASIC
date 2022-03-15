"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os
l = []
for file in os.listdir():
    with open(file) as f:
        l.append(f.read())

with open('result.txt', 'w') as f:
    f.write(','.join(l))
