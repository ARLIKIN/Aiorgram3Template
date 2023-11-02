from bot.misc import TgKeys
from bot.handlers.user import user_router
from bot.handlers.admin import admin_router
from bot.handlers.other import other_router
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


async def start_bot():
    dp = Dispatcher()
    # todo Register all the routers from handlers package
    dp.include_routers(
        admin_router,
        user_router,
        other_router
    )
    bot = Bot(token=TgKeys.TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
