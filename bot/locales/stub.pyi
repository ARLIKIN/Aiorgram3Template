from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    hello: Hello
    user: User
    admin: Admin


class Hello:
    @staticmethod
    def user(*, username) -> Literal["""Привет, { $username }."""]: ...


class User:
    button: UserButton

    @staticmethod
    def pressed() -> Literal["""Начинаем работать"""]: ...


class UserButton:
    @staticmethod
    def hello() -> Literal["""Привет"""]: ...


class Admin:
    mes: AdminMes


class AdminMes:
    @staticmethod
    def hello(*, username) -> Literal["""Приветствую админа

{ $username }"""]: ...

