from typing import TYPE_CHECKING

from aiogram import Router, html
from aiogram.filters import Command
from aiogram.types import Message
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from bot.filters.is_admin import IsAdmin

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

admin_router = Router()
admin_router.message.filter(IsAdmin())


@admin_router.message(Command("admin"))
async def command(
    message: Message,
    session: AsyncSession,
    i18n: TranslatorRunner
) -> None:
    await message.answer(
        i18n.admin.mes.hello(username=html.quote(message.from_user.username)),
    )
