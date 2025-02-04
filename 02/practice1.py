#クラス図 演習1
class Employee:
    def __init__(self, emp_id: int, name: str, salary: int) -> None:
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = name

    def _work(self) -> None:
        print("働きます")

    # def get_salary(self) -> int:
    #    return self.__salary

    #def set_salary_(self, salary: int) -> None:
    #    self.__salary = salary

    # プロパティデコレーターの方法
    # gettrとして使える
    @property
    def salary(self) -> int:
        return self.__salary

    # setter
    @salary.setter
    def salary(self, salary: int) -> None:
        self.__salary = salary
