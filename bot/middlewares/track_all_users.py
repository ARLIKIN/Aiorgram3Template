from typing import Callable, Awaitable, Dict, Any, cast

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from cachetools import TTLCache
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.crud.insert import upsert_user

class TrackAllUsersMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.cache = TTLCache(
            maxsize=1000,
            ttl=60 * 60 * 6,
        )

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        event = cast(Message, event)
        user_id = event.from_user.id

        if user_id not in self.cache:
            session: AsyncSession = data["session"]
            await upsert_user(
                session=session,
                telegram_id=event.from_user.id,
                username=event.from_user.username,
                fullname=event.from_user.full_name,
                lang_tg=event.from_user.language_code
            )
            self.cache[user_id] = None
        return await handler(event, data)