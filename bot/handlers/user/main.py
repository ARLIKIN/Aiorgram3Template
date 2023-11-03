from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

user_router = Router()


@user_router.message(Command("about"))
async def command(message: Message) -> None:
    await message.answer(f"Полное описание для, "
                         f"<b>{message.from_user.full_name}!</b>")
