actualList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Actual list:")
print(actualList)

print("\nOdd numbers:")
print(list(filter(lambda x: x % 2 != 0, actualList)))

print("\nEven numbers from the said list:")
print(list(filter(lambda x: x % 2 == 0, actualList)))
