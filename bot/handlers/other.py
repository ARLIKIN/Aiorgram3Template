from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

other_router = Router()


@other_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


@other_router.message(F.text == 'Name')
async def user_name(message: Message) -> None:
    await message.answer(message.from_user.full_name)
