"""
📌 Description:
Write a Python program that prints (as a list) the elements of listA that are not in listB as a list.

If the lists have the same elements, print an empty list.

If listA is an empty list, print an empty list.
"""

listA = [1,2,3,4,5,6]

listB = [1,2,3]

for i in listB:
    if i in listA:
        listA.remove(i)


print(listA)