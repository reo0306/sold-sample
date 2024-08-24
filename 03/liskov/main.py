from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def get_area(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self) -> None:
        self.__width = 0
        self.__height = 0

    @property
    def width(self) -> int:
        return self.__width
    
    @width.setter
    def width(self, width: int):
        self.__width = width
    
    @property
    def height(self) -> int:
        return self.__height
    
    @height.setter
    def height(self, height: int):
        self.__height = height

    def get_area(self) -> int:
        return self.__width * self.__height
    

class Square(Shape):
    def __init__(self) -> None:
        self.__length = 0
    
    @property
    def length(self) -> int:
        return self.__length
    
    @length.setter
    def length(self, length):
        self.__length = length
    
    def get_area(self) -> int:
        return self.__length ** 2

# RectangleとSquareはShape型を実装しているので、関数の引数に渡せる
# 一つのコードで複数のオブジェクトの切り替えができる。このことをポリモーフィズムという
def f(shape: Shape):
    print(shape.get_area())


if __name__ == "__main__":
    r1 = Rectangle()
    r1.width = 3
    r1.height = 4
    f(r1)

    r2 = Square()
    r2.length = 3
    f(r2)


