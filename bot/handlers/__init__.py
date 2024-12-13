from aiogram import Router

from .user import all_user_router
from .admin import all_admin_router
from ..filters.is_private import PrivateFilter

all_router = Router()

all_router.include_routers(
    all_admin_router,
    all_user_router
)

all_router.message.filter(PrivateFilter())
