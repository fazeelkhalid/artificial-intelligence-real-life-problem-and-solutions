def reverse(fileData):
    file = open("Reverse.txt", "w")

    for i in range(len(fileData) - 1, 0, -1):
        file.write(fileData[i])

    file.close()


file = open("Alphabets.txt", "r")
fileData = file.read()
file.close()

reverse(fileData)
