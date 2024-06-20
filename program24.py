"""
📌 Description:
Write a Python program that counts the number of elements in a list with value greater than 3.

You may assume that the list only contains numbers.

Print the final count.
"""
list1 = [1,2,3,4,5,6,7,8,9]

new_list = []

for i in list1:
    if i>3:
        new_list.append(i)

print(new_list)