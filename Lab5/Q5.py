def AMCount():
    file = open("STORY.txt", "r")
    readData = file.read()
    countA = 0
    countM = 0
    for i in readData:
        if(i == 'a' or i == 'A'):
            countA += 1
        elif(i == 'm' or i == 'M'):
            countM += 1

    print("Count of A and a : ", countA)
    print("Count of M and m : ", countM)


AMCount()
