def Sort_Tuple(tuple_1):
    for i in range(0, len(tuple_1)):
        for j in range(0, len(tuple_1)-i-1):
            if (tuple_1[j][1] > tuple_1[j + 1][1]):
                temp = tuple_1[j]
                tuple_1[j] = tuple_1[j + 1]
                tuple_1[j + 1] = temp
    return tuple_1


tuple1 = [('a', 23), ('b', 37), ('c', 11), ('d', 29)]

print(Sort_Tuple(tuple1))
