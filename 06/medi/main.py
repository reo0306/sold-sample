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