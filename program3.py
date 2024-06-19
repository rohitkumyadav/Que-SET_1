''''
📌Description:
Write a Python Program that prints the reversed version of a string.

The program must preserve uppercase and lowercase letters.

If the string is empty, print it intact.
'''

string1 = "Hello"
print(string1[::-1])
# or
print("".join(reversed(string1)))

string2 = "Wo"
print(string2[::-1])

string3 = ""
print(string3)