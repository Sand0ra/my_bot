from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData




btn_laptop = InlineKeyboardButton(
    text='Ноутбук',
    callback_data='laptop_data'
)

btn_PC = InlineKeyboardButton(
    text='ПК',
    callback_data='PC_data'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[btn_laptop],[btn_PC]])

btn_EnterKG = InlineKeyboardButton(
    text='Enter.KG',
    callback_data='Enter.KG'
)

btn_UltraKG = InlineKeyboardButton(
    text='Ultra.KG',
    callback_data='Ultra.KG'
    
)
select_shop = InlineKeyboardMarkup(
    inline_keyboard=[[btn_EnterKG],[btn_UltraKG]])

build = InlineKeyboardBuilder()
build.row(select_shop, width=2)