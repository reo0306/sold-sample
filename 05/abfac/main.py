from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def press(self):
        pass


class CheckBox(metaclass=ABCMeta):
    @abstractmethod
    def switch(self):
        pass


class GUIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


class WindowsButton(Button):
    def press(self):
        print("Windowsのボタンが押されました")


class WindowsCheckBox(CheckBox):
    def switch(self):
        print("Windowsのチェックボックスが切り替えられました")


class WindowsGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()


class MacButton(Button):
    def press(self):
        print("Macのボタンが押されました")


class MacCheckBox(CheckBox):
    def switch(self):
        print("Macのチェックボックスが切り替えられました")


class MacGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> CheckBox:
        return MacCheckBox()


def run(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.press()
    checkbox.switch()


if __name__ == "__main__":
    run(WindowsGUIFactory())
    run(MacGUIFactory())