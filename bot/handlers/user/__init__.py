from aiogram import Router

from .main import user_router
from .dialogs.main.diajogs import start_dialog

all_user_router = Router()
all_user_router.include_routers(
    user_router,
    start_dialog
)
