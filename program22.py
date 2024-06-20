"""
📌 Description:
Write a Python program that removes all occurrences of the element elem_to_remove from a list.

The output of the program should be the new list with the element removed.

If the element is not found in the list, print the message "Not Found".

If the list is empty, print "Empty List".
"""

a = [1,2,3,4,2,2,2,3,2]

while 1:
    if 2 in a:
        a.remove(2)
    else:
        break

print(a)