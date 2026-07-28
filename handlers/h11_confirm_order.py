from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from bot_utils.counting_products import counting_products_from_cart
from database.utils import db_get_user_phone
from config import MANAGER

router = Router()


@router.callback_query(F.data=='confirm_order')
async def confirm_order (callback: CallbackQuery, bot: Bot):
    """Оформление заказа"""
    user = callback.from_user
    phone = db_get_user_phone(user.id)

    mention = f'<a href="tg://user?id={user.id}">{user.full_name}</a>'
    user_text = f'Новый заказ от {mention}\nНомер телефона покупателя:{phone}'
    context = counting_products_from_cart(user.id, user_text)








