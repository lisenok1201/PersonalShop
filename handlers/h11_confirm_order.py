from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from bot_utils.counting_products import counting_products_from_cart
from database.utils import db_get_user_phone, db_save_order_histore, db_clean_fanal_cart
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

    if not context:
        await callback.message.edit_text('Корзины пуста!')
        await callback.answer()
        return

    if not MANAGER:
        await callback.message.edit_text('Данные менеджера отсутствуют!')
        await callback.answer()
        return

    count, text, total_price, cart_id = context

    await bot.send_message(MANAGER, text, parse_mode = 'HTML')

    db_save_order_histore(user.id)
    db_clean_fanal_cart(callback.from_user.id)

    await callback.massage.edit_text('Заказ принят.Ожидайте обратной связи')
    await callback.answer('Заказ принят')





