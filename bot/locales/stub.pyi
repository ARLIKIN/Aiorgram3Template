from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    hello: Hello
    button: Button


class Hello:
    @staticmethod
    def user(*, username) -> Literal["""Привет, { $username }."""]: ...


class Button:
    @staticmethod
    def button() -> Literal["""Нажми на меня!"""]: ...

    @staticmethod
    def pressed() -> Literal["""Начинаем работать"""]: ...

