'''📌 Description:
Write a Python program that prints the second smallest value in a list.

If the list is empty or only has one element, print None.'''


list1 = [1,5,3,2,4,5,4,6,9,3,45,64,3,56,4]

updated = sorted(list1)

print(f"Second largest element: {updated[1]}")