'''
📌 Description:
Write a Python program that prints the elements of a list followed their corresponding indices.

Each element and its index must be on the same line separated by a space.

If the list is empty, print "Empty List".
'''

list1  = ["a","b","c","d","e"]

for index,value in enumerate(list1):
    print(value,index)