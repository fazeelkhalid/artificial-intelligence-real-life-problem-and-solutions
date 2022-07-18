class rectangle():
    __length = 0
    __width = 0

    def __init__(self, length, width):

        self.__length = length
        self.__width = width

    def area(self):
        return self.__length*self.__width

    def length(self):
        return self.__length

    def width(self):
        return self.__width


class Trapezium(rectangle):
    __height = 0

    def __init__(self, length, width, height):
        rectangle.__init__(self, length, width)
        self.__height = height

    def area(self):
        return (0.5) * (rectangle.length(self) + rectangle.width(self)) * self.__height


def printArea(area):
    print("Area of the Trapezium : ")
    print(area)


Trap = Trapezium(10, 23, 1)
printArea(Trap.area())
