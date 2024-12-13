from typing import TYPE_CHECKING

from aiogram import html
from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def get_hello(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> dict[str, str]:
    username = html.quote(event_from_user.full_name)
    return {"hello_user": i18n.hello.user(username=username),
            "button_button": i18n.button.button()}
