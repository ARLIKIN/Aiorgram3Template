from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

class PrivateFilter(BaseFilter):
    """Фильтр для проверки типа чата"""
    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        return message.chat.type == ChatType.PRIVATE
