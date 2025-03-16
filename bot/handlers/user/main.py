from typing import TYPE_CHECKING

from aiogram import Router, html, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from bot.keyboards.inline.user_inline import hello_button

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
        reply_markup=await hello_button(i18n)
    )


@user_router.callback_query(F.data == 'hello')
async def process_start_command(
    callback: CallbackQuery,
    session: AsyncSession,
    i18n: TranslatorRunner
) -> None:
    await callback.answer(
        i18n.user.pressed()
    )
