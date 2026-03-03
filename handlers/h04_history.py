from aiogram.types import Message
from aiogram import Router, F

from database.utils import db_get_last_orders

router = Router()

@router.message(F.text == '📒 История')
async def show_order_history(message:Message):
    '''Демонстрация 5 последних позиий'''
    chat_id = message.chat.id
    orders = db_get_last_orders(chat_id)
    if not orders:
        await message.answer('У вас нет заказов⛔️')
        return

    text = "5 последних позиций\n"
    for item in orders:
        order = item['order']
        line_price = float(order.finall_price)
        text += f"👍{order.product_name} {order.quantity} шт {line_price:.2f} ₽"

    await message.answer(text)
