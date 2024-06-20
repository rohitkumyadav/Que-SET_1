"""
📌 Description:
Write a Python program that prints a list with the elements that listA and listB have in common.

If they don't have any elements in common, print an empty list.

The program should not assume that the lists have the same length.

You may assume that each element will only appear once in each list.
"""

list1 = [1,2,3,4]
list2 = [1,2,3]

new_list = []

for i in list1:  # 1,2,3,4
    if i in list2:
        new_list.append(i)


print(new_list)
