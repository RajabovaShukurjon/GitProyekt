from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup
from  keyboards.inline.callback_data import course_callback, book_callback


# 1-usul
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Kurslar", callback_data="courses"),
        InlineKeyboardButton(text="Kitoblar", callback_data="books"),
    ],
    [
        InlineKeyboardButton(text="Mening github sahifamga o'tish", url="https://github.com/RajabovaShukurjon"),
    ],
    [
        InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat=""),
    ],
    [
        InlineKeyboardButton(text="Ulanish", switch_inline_query="Zo'r bot ekan"),
    ],
])



# 2-usul
coursesMenu = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(text="Pythob dasturlash Asoslari", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

django = InlineKeyboardButton(text="Django Web Dasturlash", callback_data=course_callback.new(item_name="django"))
coursesMenu.insert(django)

telegram = InlineKeyboardButton(text="Telegram bot", callback_data="course:telegram")
coursesMenu.insert(telegram)

algorithm = InlineKeyboardButton(text="Ma'lumotlar tuzilmasi va Algoritmlar", callback_data="course:algorithm")
coursesMenu.insert(algorithm)

back_button = InlineKeyboardButton(text="Ortga", callback_data="cancel")
coursesMenu.insert(back_button)



# 3-usul
books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Java. Dasturlash": "js_book",
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)

telegram_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="xarid qilish", url="https://telegram.me/xaridqilish")
    ]
])

algoritm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ko'rish", url="https://telegram.me/xaridqilish"),
    ]
])