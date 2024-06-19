''''
📌Description
Write a Python program that prints the string s without the character at index n.

If the index n is out of range, print the string s intact.

If the string s is empty, print the string s intact.
'''

string = input("Enter The string: ")

n = int(input("Enter the index: "))

if len(string)<n or string == "":
    print(string)


else:
    strr = ""
    for i in range(len(string)): # 0,1,2,3,4
        if i != n:
            strr+=string[i]

    print(strr)
            