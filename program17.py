'''
📌 Description:
Write a Python program that multiplies all the items in a list by the value of the variable factor.

The program must print the list as the output.

The program should also allow multiplying the variable factor by a string in case the list contains strings.

You may assume that the value of factor will be a positive integer.
'''


a = [3,4,5,60]
b = ["a","b","c"]
new = []

for i in a:
    new.append(i*2)
print(new)