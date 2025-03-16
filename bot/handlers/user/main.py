from typing import TYPE_CHECKING

from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(
    message: Message,
    session: AsyncSession,
    i18n: TranslatorRunner
) -> None:
    await message.answer(
        i18n.hello.user(username=html.quote(message.from_user.username)),
    )
