list1 = [[1,2,3],[4,5,6],[7,8,9]]

new_list = []
counter = 0

while counter<len(list1):
    for i in list1[counter]:
        new_list.append(i)
    counter +=1

print(new_list)