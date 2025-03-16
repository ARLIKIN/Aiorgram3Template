from sqlalchemy.ext.asyncio import create_async_engine

from bot.config_data import Config

if Config.DEBUG:
    ENGINE = f"sqlite+aiosqlite:///bot/database/{Config.POSTGRES_DB}.db"
else:
    ENGINE = (
        f'postgresql+asyncpg://'
        f'{Config.POSTGRES_USER}:'
        f'{Config.POSTGRES_PASSWORD}'
        f'@postgres_db_container/{Config.POSTGRES_DB}'
    )


def engine():
    return create_async_engine(ENGINE)
