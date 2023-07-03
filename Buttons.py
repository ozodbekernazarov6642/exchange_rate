from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

uzs_rub = KeyboardButton(text='UZS 🔄 RUB₽')
uzs_usd = KeyboardButton(text='UZS 🔄 USD$')
uzs_eur = KeyboardButton(text='UZS🔄 EUR€')


currencies_button = ReplyKeyboardMarkup(one_time_keyboard=True,  resize_keyboard=True, row_width=2).add(uzs_usd, uzs_eur, uzs_rub)
