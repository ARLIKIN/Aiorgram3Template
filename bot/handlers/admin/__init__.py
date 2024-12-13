from aiogram import Router

from .main import admin_router

all_admin_router = Router()
all_admin_router.include_routers(
    admin_router
)
