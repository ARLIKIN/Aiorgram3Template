from typing import TYPE_CHECKING

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton as keyBtn
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def main_menu(i18n: TranslatorRunner) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.row(keyBtn(text=i18n.user.button.hello()))
    return kb.as_markup(resize_keyboard=True)
