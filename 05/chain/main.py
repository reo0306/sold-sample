from __future__ import annotations
import re
from abc import ABCMeta, abstractmethod


class ValidationHandler(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.__next_handler = None

    def set_handler(self, handler: ValidationHandler):
        self.__next_handler = handler
        return handler

    @abstractmethod
    def _exec_validation(self, input: str) -> bool:
        pass

    @abstractmethod
    def _get_error_message(self):
        pass

    def validate(self, input: str) -> bool:
        result = self._exec_validation(input)

        if not result:
            self._get_error_message()
            return False
        elif self.__next_handler:
            return self.__next_handler.validate(input)
        else:
            return True

class NotNullValidationHandler(ValidationHandler):
    def _exec_validation(self, input: str) -> bool:
        result = False

        if input:
            result = True

        print(f"NotNullValidationの結果: {result}")
        return result

    def _get_error_message(self):
        print("何も入力されていません")


class AlphabetValidationHandler(ValidationHandler):
    def _exec_validation(self, input: str) -> bool:
        reg = re.compile("^[a-zA-Z]+$")

        result = bool(re.search(reg, input))

        print(f"AlpabetValidationHandlerの結果: {result}")
        return result

    def _get_error_message(self):
        print("半角英字で入力してください")


class MinLengthValidationHandler(ValidationHandler):
    def _exec_validation(self, input: str) -> bool:
       result = len(input) >= 8
       print(f"MinLengthValidationHandlerの結果: {result}")

       return result

    def _get_error_message(self):
        print("8文字以上で入力してください")


if __name__ == "__main__":
    not_null_handler = NotNullValidationHandler()
    alphabet_handler = AlphabetValidationHandler()
    min_length_handler = MinLengthValidationHandler()

    # not_null -> alphabet -> min_length
    not_null_handler.set_handler(alphabet_handler).set_handler(min_length_handler)

    result = not_null_handler.validate("helloworld")
    if result:
        print("全てのバリデーションに通過しました")