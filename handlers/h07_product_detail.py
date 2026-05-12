from aiogram import Router, F, Bot
from aiogram.client import bot
from aiogram.types import CallbackQuery


from database.utils import db_get_product_by_id, db_get_user_cert

router = Router()

@router.callback_query(F.data.startwith('product_view_'))
async def show_product_view_(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    messages_id = callback.message.message_id

    await bot.delete_message(chat_id, messages_id)

    product_id=int(callback.data.split('_')[-1])
    product=db_get_product_by_id(product_id)
    users_cart=db_get_user_cert(chat_id)







