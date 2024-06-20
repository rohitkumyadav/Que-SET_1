'''
📌 Description:
Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.

If it does, print True. Else, print False.

This test should be case sensitive. For example, "A" should not be equivalent to "a".

If the length of the prefix is greater than the length of the string, print False.
'''

# Method 1
string = "Hello"

prefix = "He"

new_str  = string[:2]

print(prefix ==new_str)


# Method 2   

if string.startswith(new_str):    # or 'endwith'
    print(True)

else:
    print(False)

