from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    hello: Hello
    button: Button
    admin: Admin


class Hello:
    @staticmethod
    def user(*, username) -> Literal["""Привет, { $username }."""]: ...


class Button:
    @staticmethod
    def button() -> Literal["""Нажми на меня!"""]: ...

    @staticmethod
    def pressed() -> Literal["""Начинаем работать"""]: ...


class Admin:
    mes: AdminMes


class AdminMes:
    @staticmethod
    def hello(*, username) -> Literal["""Приветствую админа

{ $username }"""]: ...

