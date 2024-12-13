from bot import start_bot
import asyncio
import logging
import subprocess


if __name__ == '__main__':
    subprocess.run(['alembic', 'upgrade', 'head'])
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_bot())
