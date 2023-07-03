from request import get_conversion_rate_and_time
from Buttons import currencies_button

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
API_TOKEN = '5730119623:AAG6Gz44u-mCJtA6hQwSUib4S1ITnd1urqM'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    global output_message
    frist_name = message.chat.first_name
    if message.text == '/start':
        output_message = f"Assalomu Aleykum Xurmatli {frist_name}!\n" \
                         f"Botdan Foydalanishni bimalasangiz /help ni jo'nating yoki\n" \
                         f"Botdan foydalanish uchun tugmalarni bosing."
    elif message.text == '/help':
        output_message = f"Xurmatli {frist_name}!\n" \
                         f"Bu Bot sizga hozirgi vaqtdagi\n" \
                         f"Valyuta kursini topishda yordam beradi."
    await message.reply(output_message, reply_markup=currencies_button)



@dp.message_handler(Text(equals='UZS 🔄 RUB₽'))
async def UZS_RUB(message: types.Message):
    output_message = get_conversion_rate_and_time('RUB')
    await message.answer(output_message)



@dp.message_handler(Text(equals='UZS 🔄 USD$'))
async def UZS_USD(message: types.Message):
    output_message = get_conversion_rate_and_time('USD')
    await message.answer(output_message)



@dp.message_handler(Text(equals='UZS🔄 EUR€'))
async def UZS_EUR(message: types.Message):
    output_message = get_conversion_rate_and_time('EUR')
    await message.answer(output_message)






executor.start_polling(dp, skip_updates=True)