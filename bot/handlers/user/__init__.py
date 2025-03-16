from aiogram import Router

from .main import user_router

all_user_router = Router()
all_user_router.include_routers(
    user_router
)
