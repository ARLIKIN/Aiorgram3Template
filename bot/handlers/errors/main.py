import logging

from aiogram_dialog import DialogManager, StartMode, ShowMode

from bot.states.state_user import StartSG


async def on_unknown_intent(event, dialog_manager: DialogManager):
    logging.error("Restarting dialog: %s", event.exception)
    await dialog_manager.start(
        StartSG.start, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND,
    )


async def on_unknown_state(event, dialog_manager: DialogManager):
    logging.error("Restarting dialog: %s", event.exception)
    await dialog_manager.start(
        StartSG.start, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND,
    )