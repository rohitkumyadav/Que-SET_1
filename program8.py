'''
📌 Description:
Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

curr_char and new_char are variables that contain strings with a single character.

You may assume that new_char will not be an empty string.

The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

If no match is found, print the initial string.
'''

string = input("Enter the String: ")

curr_str = input("Enter the current string[single char]: ")

new_str = input("Enter the new string[single str]: ")

if curr_str not in string:
    print(string)

else:
    new_string = string.replace(curr_str,new_str)
    print(f"String After updation is {new_string}")