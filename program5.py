'''
📌Description:
Write a Python program that prints the string s without the characters located at even indices.

If the string is empty or only has one character, print it intact.
'''



string = input("Enter the String: ")

if len(string) == "" or len(string) == 1:
    print(string)

else:
    for i in range(len(string)):
        if i%2 ==0:
            continue
        else:
            print(string[i], end="")