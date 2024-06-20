'''
Description:
Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.

You may assume that the string only contains letters and spaces to separate the words.

Spaces should be preserved in the final string.
'''

str = "Hello World".lower()

str1 = str.split()

a = str1[0]
b= str1[1]

print("".join(sorted(a)) +" "+"".join(sorted(b))  )
