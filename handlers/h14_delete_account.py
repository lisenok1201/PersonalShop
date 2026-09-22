from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from config import MANAGER_ID
from keyboards.inline import delete_confirm_kb, get_settings_menu
from keyboards.reply import start_kb

router = Router()

@router.callback_query(F.data=='delete_account')
async def handle_delet_account(callback: CallbackQuery):
    """"""
    await callback.message.edit_text(
        'ВЫ уверены? \nДанные будут удалены',
        reply_markup=delete_confirm_kb()
    )

@router.callback_query(F.data=='confirm_delete')
async def handel_confirm_delete(callback: CallbackQuery, bot: Bot):
    telegram_id = callback.from_user.id
    full_name = callback.from_user.full_name

    success = db_delet_user_by_telegram_id(telegram_id)

    if success:
        try:
            await callback.message.delete()
        except TelegramBadRequest:
            pass

        await callback.message.answer(text="Ваш аккаунт удален.\nДля повторной работы необходимо зарегистрироваться",
        reply_markup=start_kb())
        await bot.send_message(MANAGER_ID,f"Пользователь {full_name} удалил аккаунт{telegram_id}")
    else:
        await callback.message.edit_text("Произошла ошибка при удалении", reply_markup=get_settings_menu())


