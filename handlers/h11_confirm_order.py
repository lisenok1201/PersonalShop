from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery

router = Router()

@router.callback_query(F.data=='confirm_order')
async def confirm_order (callback: CallbackQuery, bot: Bot):
    """Оформлене заказа"""
    user = callback.from_user
    phone = db_get_user_phone









