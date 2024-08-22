# クラス図 演習2
from abc import ABCMeta, abstractmethod 

# 抽象クラスとして定義（インターフェース）
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def calc_area(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

    def calc_area(self) -> int:
        return self.__width * self.__height


class Square(Shape):
    def __init__(self, length: int) -> None:
        self.__length = length

    def calc_area(self) -> int:
        return self.__length ** 2


class Client:
    def __init__(self, shape: Shape) -> None:
        self.__shape = shape