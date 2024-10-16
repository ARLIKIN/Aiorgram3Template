from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from aiogram.enums import ParseMode

from bot.misc import TgKeys
from bot.handlers.user import user_router
from bot.handlers.admin import admin_router
from bot.handlers.other import other_router


async def start_bot():
    dp = Dispatcher(
        storage=MemoryStorage(),
        fsm_strategy=FSMStrategy.USER_IN_CHAT
    )
    # todo Register all the routers from handlers package
    dp.include_routers(
        admin_router,
        user_router,
        other_router
    )
    bot = Bot(token=TgKeys.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
