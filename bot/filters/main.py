from aiogram.filters import Filter
from aiogram.types import Message


class IsAdmin(Filter):
    def __init__(self):
        self.id_admin = 1111

    async def __call__(self,message: Message) -> bool:
        return message.from_user.id == self.id_admin
