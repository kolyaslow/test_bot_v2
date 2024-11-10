from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router(name=__name__)


def create_numeric_keyboard(
    start_number: int = 1,
    amount_button: int = 9,
    step: float = 1,
) -> ReplyKeyboardMarkup:
    """
    Создание клавиатуры, где варианты ответов этот цифры от start_number с шагом step

    :param start_number: значение с которого необходимо начать формирование
    :param amount_button: общее коли-во кнопок
    :param step:  шаг с которым необходимо сформировать цифры. Если 1 то получим 1-2-3 и т.д
    """
    builder = ReplyKeyboardBuilder()

    # Получение текста для кнопок так как могут быть целые значения, а могут быть дробные
    text_buttons = [str(i * step) for i in range(start_number, amount_button)]

    for text in text_buttons:
        builder.button(text=text)

    # выравнивание клавиатуры
    if amount_button % 2 == 0:
        builder.adjust(2)
    else:
        builder.adjust(3)

    return builder.as_markup(resize_keyboard=True)
