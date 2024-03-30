from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.states.state_user import StartSG

user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(
        message: Message,
        dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)
