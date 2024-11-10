from admin.common import create_numeric_keyboard
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_message = """
Здравствуйте! Вас приветствует бот <b><em>SUP & Chill</em></b>.

Давайте запишем вас, понадобится  ответить <b>всего на 4 вопроса</b>, начнём:
 - Сколько сапов бронировать? <i>Выберите количество сапов или напишите свой вариант</i>.
"""
router = Router(name=__name__)


@router.message(CommandStart())
async def handler_start(message: Message):
    await message.answer(
        text=start_message, reply_markup=create_numeric_keyboard(amount_button=6)
    )
