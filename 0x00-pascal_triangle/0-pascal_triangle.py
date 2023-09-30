#!/usr/bin/python3
"""A module for working with pascal
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]

    for i in range(1, n):
        previous_row = pascal[i - 1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(previous_row[j - 1] + previous_row[j])

        new_row.append(1)
        pascal.append(new_row)

    return pascal

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)

