from aiogram.types import ResponseParameters, KeyboardButton, ReplyKeyboardMarkup

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Mahsulotlar'),
            KeyboardButton(text="Qo'llanma"),
        ],
    ],
    resize_keyboard=True,
)