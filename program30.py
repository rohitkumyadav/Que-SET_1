'''
📌 Description:
Write a Python program that creates and print a dictionary that maps each element in a list to its corresponding frequency (how many times it occurs in the list).

The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a".'''

list1 = ["a","a","b","b","a","c","d","e","d","d"]

dict1 = {}

for i in list1:
    if i in dict1:
        dict1[i] +=1
    
    else:
        dict1[i] =1


print(dict1)