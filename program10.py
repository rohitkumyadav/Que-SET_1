'''
📌 Description:
Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").

If it does, print True. Else, print False.

Before comparing the characters, you should convert the string to lowercase.

If the string contains spaces, ignore them before finding the result.

You may assume that the string doesn't contain any other symbols, only spaces (possibly).

Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'
'''
# Method 1

import string

chrs = set(string.ascii_lowercase)


def check_pangram(string):
    arr_str = set(string)

    return chrs.issubset(arr_str)

str = input("Enter the string: ").lower()

print(check_pangram(str))


