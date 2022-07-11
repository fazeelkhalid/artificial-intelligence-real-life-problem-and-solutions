list_ = list()

for i in range(0,20,2):
    list_.append(i);

squareList = list(map(lambda element: element ** 2, list_))
CubeList = list(map(lambda element: element ** 3, list_))
print("Original list:")
print(list_)
print("\n\nSquare of list numbers:")
print(squareList)
print("\n\nCube of list numbers:")
print(CubeList)
