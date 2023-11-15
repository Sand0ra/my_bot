from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from keyboards import *
from enterKG import scrape_enterKG , lst_urls, lst_names, lst_prices
from ultraKG import scrape_UltraKG, list_name, list_price, list_url
import time
router = Router()











@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! я могу помочь тебе подобрать комплектующие для ПК или помочь с выбором ноутбука",
                         reply_markup=select_type.as_markup()
                         )
    





@router.callback_query(F.data == 'laptop_data')
async def laptop_press(callback: CallbackQuery):
    
    await callback.message.answer(
        text='"Ноутбук" отличный выбор \nТеперь выберите магазин!',
        reply_markup=select_shop.as_markup()
    )
    
    @router.callback_query(F.data == 'Back_data')
    async def back_press(callback: CallbackQuery):
        await callback.message.answer("Так что же тебя интересует Ноуты или все таки ПК",
                    reply_markup=select_type.as_markup()
                    )
        
    @router.callback_query(F.data == 'Ultra.KG')
    async def Ultra_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_UltraKG(laptop_2)
        await callback.message.answer(text=f'<i>{list_name[0]}</i>\n\n <b>Цена</b> <i>{list_price[0]}</i>🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup())
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]
        

    @router.callback_query(F.data == 'next_to_ultraKG')
    async def next_press(callback: CallbackQuery):
        await callback.message.edit_text(text=f'<i>{list_name[0]}</i>\n\n<b>Цена:</b> <i>{list_price[0]}</i>🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup()
                                    )
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]
        
        
        
    @router.callback_query(F.data == 'Enter.KG')
    async def Enter_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_enterKG(laptop)
        await callback.message.answer(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_or_back.as_markup())
        time.sleep(2) 
        del lst_prices[0], lst_urls[0], lst_names[0]
            
            
            
    @router.callback_query(F.data == 'next')
    async def next_press(callback: CallbackQuery):
        await callback.message.edit_text(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена:</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_or_back.as_markup()
                                    )
        time.sleep(2) 
        del lst_prices[0], lst_urls[0], lst_names[0]
        

    @router.callback_query(F.data == 'Back_data')
    async def back_press(callback: CallbackQuery):
        await callback.message.answer("Так что же тебя интересует? \n Ноуты или все таки ПК",
                    reply_markup=select_type.as_markup())





@router.callback_query(F.data == 'PC_data')
async def full_pc_press(callback: CallbackQuery):
    await callback.message.answer(
        text='Отлично теперь \nВыберите конфигурацию',
        reply_markup=select_configuration.as_markup()
    )
      
    @router.callback_query(F.data == 'Full_data')
    async def Full_PC(callback: CallbackQuery):
        await callback.message.answer(
            text='https://qptr.ru/ADhR \nИгровой компьютер на базе Intel Pentium',
            reply_markup=first_fullBlock.as_markup()
        )
        
    @router.callback_query(F.data == 'back_to_configuration')
    async def back_press(callback: CallbackQuery):
        await callback.message.answer(
        text='Отлично теперь \nВыберите конфигурацию',
        reply_markup=select_configuration.as_markup()
    )
    @router.callback_query(F.data == 'next_setup_2')
    async def next_press(callback: CallbackQuery):
        await callback.message.answer('https://qptr.ru/6Cod \n Игровой компьютер на базе Intel i5',
                                    reply_markup=second_fullBlock.as_markup()
                                    )
        
    @router.callback_query(F.data == 'next_setup_3')
    async def next_press(callback: CallbackQuery):
        await callback.message.answer('https://qptr.ru/sa50 \n Игровой компьютер на базе Intel i7',
                                    reply_markup=third_fullBlock.as_markup()
                                    )       

        


@router.callback_query(F.data == 'components_data')
async def components_PC(callback: CallbackQuery):
    await callback.message.answer(
        text='"Компоненты" отличный выбор \nТеперь выберите магазин!',
        reply_markup=select_shop_2.as_markup()
    )
    
    
@router.callback_query(F.data == 'Enter.KG_2')
async def back_press(callback: CallbackQuery):
    await callback.message.answer(text='С какого компонента вы предпочли бы начать свое погружение в мир сборки ПК?',
    reply_markup=button_select_components.as_markup())
    
@router.callback_query(F.data == 'btn_videocard')
async def videocard_press(callback: CallbackQuery):
    await callback.message.answer('Подождите идет парсинг данных...')
    scrape_enterKG(videocard)
    await callback.message.answer(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                parse_mode='HTML',
                                reply_markup=button_norex.as_markup())
    time.sleep(2) 
    del lst_prices[0], lst_urls[0], lst_names[0]

@router.callback_query(F.data == 'btn_monitor')
async def monitor_press(callback: CallbackQuery):
    await callback.message.answer('Подождите идет парсинг данных...')
    scrape_enterKG(monitor)
    await callback.message.answer(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                parse_mode='HTML',
                                reply_markup=button_norex.as_markup())
    time.sleep(2) 
    del lst_prices[0], lst_urls[0], lst_names[0]
    
    
@router.callback_query(F.data == 'btn_computer_case')
async def comp_case_press(callback: CallbackQuery):
    await callback.message.answer('Подождите идет парсинг данных...')
    scrape_enterKG(computer_case)
    await callback.message.answer(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                parse_mode='HTML',
                                reply_markup=button_norex.as_markup())
    time.sleep(2) 
    del lst_prices[0], lst_urls[0], lst_names[0]


@router.callback_query(F.data == 'btn_procecor')
async def procecor_press(callback: CallbackQuery):
    await callback.message.answer('Подождите идет парсинг данных...')
    scrape_enterKG(procecor)
    await callback.message.answer(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                parse_mode='HTML',
                                reply_markup=button_norex.as_markup())
    time.sleep(2) 
    del lst_prices[0], lst_urls[0], lst_names[0]


@router.callback_query(F.data == 'btn_hdd_ccd_memory')
async def hdd_ccd_press(callback: CallbackQuery):
    await callback.message.answer('Подождите идет парсинг данных...')
    scrape_enterKG(hdd_ccd_memory)
    await callback.message.answer(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                parse_mode='HTML',
                                reply_markup=button_norex.as_markup())
    time.sleep(2) 
    del lst_prices[0], lst_urls[0], lst_names[0]



@router.callback_query(F.data == 'btn_power_block')
async def power_block_press(callback: CallbackQuery):
    await callback.message.answer('Подождите идет парсинг данных...')
    scrape_enterKG(power_block)
    await callback.message.answer(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                parse_mode='HTML',
                                reply_markup=button_norex.as_markup())
    time.sleep(2) 
    del lst_prices[0], lst_urls[0], lst_names[0]



@router.callback_query(F.data == 'btn_oper_memory')
async def oper_memory_press(callback: CallbackQuery):
    await callback.message.answer('Подождите идет парсинг данных...')
    scrape_enterKG(oper_memory)
    await callback.message.answer(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                parse_mode='HTML',
                                reply_markup=button_norex.as_markup())
    time.sleep(2) 
    del lst_prices[0], lst_urls[0], lst_names[0]


@router.callback_query(F.data == 'btn_motherboard')
async def motherboard_press(callback: CallbackQuery):
    await callback.message.answer('Подождите идет парсинг данных...')
    scrape_enterKG(motherboard)
    await callback.message.answer(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                parse_mode='HTML',
                                reply_markup=button_norex.as_markup())
    time.sleep(2) 
    del lst_prices[0], lst_urls[0], lst_names[0]


 
@router.callback_query(F.data == 'next_component')
async def next_press(callback: CallbackQuery):
    await callback.message.edit_text(text=f'<i>{lst_names[0]}</i>\n\n<b>Цена:</b> <i>{lst_prices[0]}</i> 🔥🔥🔥\n{lst_urls[0]}',
                                parse_mode='HTML',
                                reply_markup=button_norex.as_markup()
                                )
    time.sleep(2) 
    del lst_prices[0], lst_urls[0], lst_names[0]       
           
           
           
                







@router.callback_query(F.data == 'Ultra.KG_2')
async def back_press(callback: CallbackQuery):
    await callback.message.answer(text='С какого компонента вы предпочли бы начать свое погружение в мир сборки ПК?',
    reply_markup=button_select_components_2.as_markup())
    
    
    @router.callback_query(F.data == 'btn_videocard_2')
    async def videocard_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_UltraKG(videocard_2)
        await callback.message.answer(text=f'<i>{list_name[0]}</i>\n\n<b>Цена</b> <i>{list_price[0]}</i> 🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup())
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]

    @router.callback_query(F.data == 'btn_monitor_2')
    async def monitor_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_UltraKG(monitor_2)
        await callback.message.answer(text=f'<i>{list_name[0]}</i>\n\n<b>Цена</b> <i>{list_price[0]}</i> 🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup())
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]
        
        
    @router.callback_query(F.data == 'btn_computer_case_2')
    async def comp_case_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_UltraKG(computer_case_2)
        await callback.message.answer(text=f'<i>{list_name[0]}</i>\n\n<b>Цена</b> <i>{list_price[0]}</i> 🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup())
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]

    @router.callback_query(F.data == 'btn_procecor_2')
    async def procecor_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_UltraKG(procecor_2)
        await callback.message.answer(text=f'<i>{list_name[0]}</i>\n\n<b>Цена</b> <i>{list_price[0]}</i> 🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup())
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]


    @router.callback_query(F.data == 'btn_hdd_ccd_memory_2')
    async def hdd_ccd_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_UltraKG(hdd_ccd_memory_2)
        await callback.message.answer(text=f'<i>{list_name[0]}</i>\n\n<b>Цена</b> <i>{list_price[0]}</i> 🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup())
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]


    @router.callback_query(F.data == 'btn_power_block_2')
    async def power_block_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_UltraKG(power_block_2)
        await callback.message.answer(text=f'<i>{list_name[0]}</i>\n\n<b>Цена</b> <i>{list_price[0]}</i> 🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup())
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]



    @router.callback_query(F.data == 'btn_oper_memory_2')
    async def oper_memory_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_UltraKG(oper_memory_2)
        await callback.message.answer(text=f'<i>{list_name[0]}</i>\n\n<b>Цена</b> <i>{list_price[0]}</i> 🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup())
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]


    @router.callback_query(F.data == 'btn_motherboard_2')
    async def motherboard_press(callback: CallbackQuery):
        await callback.message.answer('Подождите идет парсинг данных...')
        scrape_UltraKG(motherboard_2)
        await callback.message.answer(text=f'<i>{list_name[0]}</i>\n\n<b>Цена</b> <i>{list_price[0]}</i> 🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup())
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]



    @router.callback_query(F.data == 'next_to_ultraKG')
    async def next_press(callback: CallbackQuery):
        await callback.message.edit_text(text=f'<i>{list_name[0]}</i>\n\n<b>Цена:</b> <i>{list_price[0]}</i> 🔥🔥🔥\n{list_url[0]}',
                                    parse_mode='HTML',
                                    reply_markup=next_to_ultraKG.as_markup()
                                    )
        time.sleep(2) 
        del list_price[0], list_url[0], list_name[0]     