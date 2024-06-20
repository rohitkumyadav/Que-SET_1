'''
📌 Description:
Write a Python program that prints the largest and smallest values in a list

Print the two values on the same line, separated by a space.

The largest value should appear first and the smallest value should appear second.

You may assume that the list only contains numeric values.

If the list is empty, print None.
'''


a = [3,4,5,6]

max_ = max(a)
min_ = min(a)

print(f"{max_} {min_}")