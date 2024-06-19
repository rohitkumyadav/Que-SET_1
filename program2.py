''' 📌Description:
Write a Python program that prints the character at index i in the string s.

If the index is out of range, the program should print "i is out of range"

If the string is empty, the program should print "Empty String"'''


string = "Hello"
print(string[2])

string = "Pizza"
print(string[4])

string = ""
if string == "":
    print("Empty String")

string = "World"

if len(string)<15:
    print("i is out of range")