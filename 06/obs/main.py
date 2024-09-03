from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, name: str):
        pass


class StoreObserver(Observer):
    def update(self, name: str):
        print(f"{name}が入荷されました。仕入れが可能です")


class PersonalObserver(Observer):
    def update(self, name: str):
        print(f"{name}が入荷されました。購入が可能です")


class ItemSubject(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observers: list[Observer] = []

    def attach(self, observer: Observer):
        self.__observers.append(observer)

    def detach(self, observer: Observer):
        self.__observers.remove(observer)

    def notify(self):
        for obs in self.__observers:
            obs.update(self.__name)

    @abstractmethod
    def restock(self):
        pass


class TvGameSubject(ItemSubject):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__in_stock = False

    def restock(self):
        print("TVゲームの入荷")
        self.__in_stock = True
        self.notify()


if __name__ == "__main__":
    store = StoreObserver()
    person = PersonalObserver()
    tv_game = TvGameSubject("New RPG Game")

    tv_game.attach(store)
    tv_game.attach(person)
    tv_game.restock()
