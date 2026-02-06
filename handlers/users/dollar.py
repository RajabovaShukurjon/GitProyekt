from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
import requests

from keyboards.default.startMenuKeys import menuStart
from loader import dp

@dp.message_handler(Command("dollar"))
async def bot_start(message: types.Message):


    API_KEY = '6b4e2e31232b5b03a5eb2eae'

    currency = 'USD'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    kurs = response.json()['conversion_rate']
    print(f"1 dollar kursi {kurs} so'mga teng")
    await message.answer(f"1 dollar, {kurs} so'mga teng")
