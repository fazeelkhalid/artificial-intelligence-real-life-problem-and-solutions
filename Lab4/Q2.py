class queue:
    __item = []
    def __init__(self):
        self.__item = []
        
    def enqueue(self, item):
        self.__item.insert(0,item)

    def dequeue(self):
        return self.__item.pop()


q = queue()
for i in range(1,10):
    q.enqueue(i)

for i in range(1,10):
    print(q.dequeue())
