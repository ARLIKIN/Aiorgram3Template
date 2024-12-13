import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import ExceptionTypeFilter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from aiogram_dialog.api.exceptions import UnknownIntent, UnknownState
from fluentogram import TranslatorHub
from sqlalchemy.ext.asyncio import async_sessionmaker

from bot.database.engine import engine
from bot.handlers import all_router
from bot.handlers.errors.main import on_unknown_intent, on_unknown_state
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.middlewares.session import DbSessionMiddleware
from bot.middlewares.track_all_users import TrackAllUsersMiddleware
from bot.service import Config
from bot.service.i18n import create_translator_hub

logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(filename)s:%(lineno)d "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

log = logging.getLogger(__name__)


async def start_bot():
    bot = Bot(
        token=Config.TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(
        storage=MemoryStorage(),
        fsm_strategy=FSMStrategy.USER_IN_CHAT
    )
    dp.include_router(all_router)

    dp.errors.register(
        on_unknown_intent,
        ExceptionTypeFilter(UnknownIntent),
    )
    dp.errors.register(
        on_unknown_state,
        ExceptionTypeFilter(UnknownState),
    )

    sessionmaker = async_sessionmaker(engine(), expire_on_commit=False)
    dp.update.outer_middleware(DbSessionMiddleware(sessionmaker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())

    translator_hub: TranslatorHub = create_translator_hub()
    dp.update.middleware(TranslatorRunnerMiddleware())
    dp.errors.middleware(TranslatorRunnerMiddleware())

    setup_dialogs(dp)
    await dp.start_polling(bot, _translator_hub=translator_hub)
