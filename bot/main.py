import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from bot.dialogs.user.main.diajogs import start_dialog
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.misc import TgKeys
from bot.handlers.user import user_router
from bot.handlers.admin import admin_router
from bot.misc.i18n import create_translator_hub

logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(filename)s:%(lineno)d "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

log = logging.getLogger(__name__)


async def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(
        storage=MemoryStorage(),
        fsm_strategy=FSMStrategy.USER_IN_CHAT
    )

    # todo Register all the routers from handlers package
    dp.include_routers(
        admin_router,
        user_router,
        start_dialog
    )
    translator_hub: TranslatorHub = create_translator_hub()
    dp.update.middleware(TranslatorRunnerMiddleware())
    setup_dialogs(dp)
    await dp.start_polling(bot, _translator_hub=translator_hub)
