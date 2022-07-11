class circle():
    __radius = 0
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return ((self.__radius * self.__radius) * 3.1415926)
    
    def circlePerimeter(self):
        return ((2 * self.__radius) * 3.1415926)


def printinfo(area, per):
    print("Area of the circle : ")
    print(area)

    print("Perimeter of the circle : ")
    print(per)
    
    
cir = circle(10)
printinfo(cir.area(), cir.circlePerimeter())
