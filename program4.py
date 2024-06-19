'''
📌Description:
Write a Python program that prints the first and last three characters of the string s as a single string.

If the string has less than six characters, print an empty string (blank output).

'''

string =  input("Enter the String: ")

if len(string)<6:
    print("")

else:
    print(string[0:3]+string[-3:])