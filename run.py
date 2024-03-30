import logging
from bot import start_bot
import asyncio

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_bot())
