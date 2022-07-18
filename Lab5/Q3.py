class myIterator:
    __num = 0

    def __iter__(self):
        self.__num = 1
        return self

    def __next__(self):
        x = self.__num
        self.__num = self.__num + 1
        return x


__myIterator = iter(myIterator())

for i in range(0, 100):
    print(next(__myIterator))
