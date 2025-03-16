import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()


class Config:
    TOKEN: Final = os.getenv('TOKEN', 'define me!')
    DEBUG: Final = os.getenv('DEBUG', 'False') == 'True'
    POSTGRES_DB: Final = os.getenv('POSTGRES_DB', 'Database')
    POSTGRES_USER: Final = os.getenv('POSTGRES_USER', 'define me!')
    POSTGRES_PASSWORD: Final = os.getenv('POSTGRES_PASSWORD', 'define me!')
