from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.filters.main import IsAdmin
admin_router = Router()


@admin_router.message(IsAdmin(), Command("admin"))
async def command(message: Message) -> None:
    await message.answer(f"Hello Administrator, <b>{message.from_user.full_name}!</b>")
