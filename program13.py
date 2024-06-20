'''
📌 Description:
Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.

If it does, print True. Else, print False.

This test should be case sensitive. Therefore, "A" should not be equivalent to "a".

If the length of the suffix is greater than the length of the string, print False.
'''

# Method 2

str = "Hello"

suffix = "ello"

print(str.endswith(suffix))

# Method 2

str_ind = str[-4:]

print(suffix == str_ind)