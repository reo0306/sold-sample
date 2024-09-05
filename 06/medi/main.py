from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def register_user(self, user: User):
        pass

    @abstractmethod
    def send_message(self, msg: str, sendUser: User):
        pass


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.__members = []

    def register_user(self, user: User):
        self.__members.append(user)

    def send_message(self, msg: str, sendUser: User):
        for member in self.__members:
            if member != sendUser:
                member.receive(msg)


class User(metaclass=ABCMeta):
    def __init__(self, mediator: Mediator, name: str) -> None:
        self._mediator = mediator
        self._name = name

    @abstractmethod
    def send(self, msg: str):
        pass

    @abstractmethod
    def receive(self, msg: str):
        pass


class ChatUser(User):
    def __init__(self, mediator: Mediator, name: str) -> None:
        super().__init__(mediator, name)

    def send(self, msg: str):
        print(f"{self._name} -> メッセージ送信")

        self._mediator.send_message(f"{msg} from {self._name}", self)

    def receive(self, msg: str):
        print(f"{self._name} -> メッセージ受信: {msg}")


if __name__ == "__main__":
    chart_room = ChatRoom()

    yamada = ChatUser(chart_room, "yamada")
    suzuki = ChatUser(chart_room, "suzuki")
    tanaka = ChatUser(chart_room, "tanaka")

    chart_room.register_user(yamada)
    chart_room.register_user(suzuki)
    chart_room.register_user(tanaka)

    yamada.send("こんにちは")
    tanaka.send("こんばんは")
