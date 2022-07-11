class rectangle():
    __length = 0
    __width = 0
    def __init__(self, length, width):
        
        self.__length = length
        self.__width  = width
        
    def area(self):
        return self.__length*self.__width

def printArea(area):
    print("Area of the rectangle : " )
    print(area)
    
rect = rectangle(10,23)
printArea(rect.area())
