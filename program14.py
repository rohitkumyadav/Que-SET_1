'''
📌 Description:
Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.

Assume that the string only contains letters and spaces are used to separate words.
'''

str = "Hello World"

print("".join(reversed(str.swapcase())))


# Method 2

new_str  = str[::-1]

print(new_str.swapcase())

