from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from handlers.keyboards import *


router = Router()











@router.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[btn_laptop],
                     [btn_PC]])
    await message.answer("Привет! я могу помочь тебе подобрать комплектующие для ПК или помочь с выбором ноутбука",
                         reply_markup=keyboard
                         )
    
    

@router.callback_query(F.data == 'laptop_data')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата  КНОПКА 1':
        await callback.message.answer(
            text='Выберите магазин',
            reply_markup=build.as_markup(resize_keyboard=True)
        )
 

    
   
