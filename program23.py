"""
📌 Description:
Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.

The original list should be mutated (modified).

The program must print the final version of the list.
"""

a = [1,2,3,2,1,2,1]

a = set(a)

print(list(a))