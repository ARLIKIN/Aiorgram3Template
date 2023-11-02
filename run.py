from bot import start_bot
import asyncio
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_bot())
