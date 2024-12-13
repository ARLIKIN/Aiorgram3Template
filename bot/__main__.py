import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from bot.handlers.user import all_user_router
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.service import TgKeys
from bot.handlers.admin import all_admin_router
from bot.service.i18n import create_translator_hub

logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(filename)s:%(lineno)d "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

log = logging.getLogger(__name__)


async def start_bot():
    bot = Bot(
        token=TgKeys.TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(
        storage=MemoryStorage(),
        fsm_strategy=FSMStrategy.USER_IN_CHAT
    )

    dp.include_routers(
        all_admin_router,
        all_user_router
    )
    translator_hub: TranslatorHub = create_translator_hub()
    dp.update.middleware(TranslatorRunnerMiddleware())
    setup_dialogs(dp)
    await dp.start_polling(bot, _translator_hub=translator_hub)
