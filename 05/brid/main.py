from abc import ABCMeta, abstractmethod


class MessageApp(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        pass


class LINE(MessageApp):
    def send(self):
        print("LINEでメッセージを送信しました")


class Twitter(MessageApp):
    def send(self):
        print("Twitterでメッセージを送信しました")


class Facebook(MessageApp):
    def send(self):
        print("Facebookでメッセージを送信しました")


class OS(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._app = None

    def set_app(self, app: MessageApp):
        self._app = app

    @abstractmethod
    def send_message(self):
        pass


class IOS(OS):
    def send_message(self):
        print("iOSでメッセージ送信")

        if self._app:
            self._app.send()
        else:
            raise Exception("アプリが指定されていません")


class Android(OS):
    def send_message(self):
        print("Androidでメッセージ送信")

        if self._app:
            self._app.send()
        else:
            raise Exception("アプリが指定されていません")


if __name__ == "__main__":
    line = LINE()
    twitter = Twitter()
    facebook = Facebook()

    ios = IOS()
    android = Android()

    ios.set_app(line)
    ios.send_message()

    android.set_app(facebook)
    android.send_message()