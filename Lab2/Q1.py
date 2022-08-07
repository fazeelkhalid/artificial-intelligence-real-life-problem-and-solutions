#Question 1
list1 = [1, 2, 3, 5, 654, 344, 121]
list2 = [11, 2, 3, 5, 654, 344]
list3 = []
if(len(list1) >= len(list2)):
    for i in range(0, len(list2), 1):
        list3.append(list2[i])
        list3.append(list1[i])

    for i in range(len(list2), len(list1), 1):
        list3.append(list1[i])

else:
    for i in range(0, len(list1), 1):
        list3.append(list2[i])
        list3.append(list1[i])

    for i in range(len(list1), len(list2), 1):
        list3.append(list2[i])

print('\nList 3 : ')
for i in range(0, len(list3), 1):
    print(list3[i])
