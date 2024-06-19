"""
📌Description:
Write a Python program that check if a string only contains numbers.

If it does, print True. Else, print False.
"""

string = input("Enter the String: ")

if string.isdigit():
    print("True")

else:
    print("False")