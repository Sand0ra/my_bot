from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from links import *

btn_next_config_1 = InlineKeyboardButton(
    text='Дальше',
    callback_data='next_setup_1'
)
btn_next_config_2 = InlineKeyboardButton(
    text='Дальше',
    callback_data='next_setup_2'
)
btn_next_config_3 = InlineKeyboardButton(
    text='Дальше',
    callback_data='next_setup_3'
)

btn_back_config = InlineKeyboardButton(
    text='Назад',
    callback_data='back_to_configuration'
)

btn_next_componet = InlineKeyboardButton(
    text='Дальше',
    callback_data='next_component'
)


btn_laptop = InlineKeyboardButton(
    text='Ноутбук',
    callback_data='laptop_data'
)

btn_PC = InlineKeyboardButton(
    text='ПК',
    callback_data='PC_data'
)
select_type = InlineKeyboardBuilder()
select_type.row(btn_laptop, btn_PC, width=1)


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

btn_back = InlineKeyboardButton(
    text='Назад',
    callback_data='Back_data'
)
btn_next = InlineKeyboardButton(
    text='Дальше',
    callback_data='next'
)
btn_next_ultraKG = InlineKeyboardButton(
    text='Дальше',
    callback_data='next_to_ultraKG'
)

next_or_back = InlineKeyboardBuilder()
next_or_back.row(btn_back,btn_next,width=2)

next_to_ultraKG = InlineKeyboardBuilder()
next_to_ultraKG.row(btn_back, btn_next_ultraKG, width=2)


select_shop = InlineKeyboardBuilder()
select_shop.row(btn_UltraKG,btn_EnterKG,btn_back,width=2)


btn_Full_pc = InlineKeyboardButton(
    text='Готовый ПК',
    callback_data='Full_data'
)

btn_components = InlineKeyboardButton(
    text='Комплектующие',
    callback_data='components_data'
)

select_configuration = InlineKeyboardBuilder()
select_configuration.row(btn_Full_pc,btn_components,btn_back,width=2)



btn_EnterKG_2 = InlineKeyboardButton(
    text='Enter.KG',
    callback_data='Enter.KG_2'
)

btn_UltraKG_2 = InlineKeyboardButton(
    text='Ultra.KG',
    callback_data='Ultra.KG_2'
    
)
select_shop_2 = InlineKeyboardBuilder()
select_shop_2.row(btn_UltraKG_2,btn_EnterKG_2,btn_back_config,width=2)

button_norex = InlineKeyboardBuilder()
button_norex.row(btn_back_config,btn_next_componet,width=2)


btn_monitor = InlineKeyboardButton(
    text='Монитор',
    callback_data='btn_monitor'
)
btn_computer_case = InlineKeyboardButton(
    text='Корпус',
    callback_data='btn_computer_case'
)
btn_procecor = InlineKeyboardButton(
    text='Процессор',
    callback_data='btn_procecor'
)
btn_hdd_ccd_memory = InlineKeyboardButton(
    text='Жесткий диск',
    callback_data='btn_hdd_ccd_memory'
)
btn_power_block = InlineKeyboardButton(
    text='Блок питания',
    callback_data='btn_power_block'
)
btn_motherboard = InlineKeyboardButton(
    text='Материнская плата',
    callback_data='btn_motherboard'
)
btn_oper_memory = InlineKeyboardButton(
    text='Оперативная память',
    callback_data='btn_oper_memory'
)
btn_videocard = InlineKeyboardButton(
    text='Видео карта',
    callback_data='btn_videocard'
)


button_select_components = InlineKeyboardBuilder()
button_select_components.row(btn_videocard,btn_oper_memory,btn_monitor,btn_computer_case,
                             btn_procecor,btn_hdd_ccd_memory,btn_power_block,btn_motherboard,btn_back_config,width=2)




btn_monitor_2 = InlineKeyboardButton(
    text='Монитор',
    callback_data='btn_monitor_2'
)
btn_computer_case_2 = InlineKeyboardButton(
    text='Корпус',
    callback_data='btn_computer_case_2'
)
btn_procecor_2 = InlineKeyboardButton(
    text='Процессор',
    callback_data='btn_procecor_2'
)
btn_hdd_ccd_memory_2 = InlineKeyboardButton(
    text='Жесткий диск',
    callback_data='btn_hdd_ccd_memory_2'
)
btn_power_block_2 = InlineKeyboardButton(
    text='Блок питания',
    callback_data='btn_power_block_2'
)
btn_motherboard_2 = InlineKeyboardButton(
    text='Материнская плата',
    callback_data='btn_motherboard_2'
)
btn_oper_memory_2 = InlineKeyboardButton(
    text='Оперативная память',
    callback_data='btn_oper_memory_2'
)
btn_videocard_2 = InlineKeyboardButton(
    text='Видео карта',
    callback_data='btn_videocard_2'
)


btn_next_component = InlineKeyboardButton(
    text='Дальше',
    callback_data='next_component_2'
)
button_select_components_2 = InlineKeyboardBuilder()
button_select_components_2.row(btn_videocard_2,btn_oper_memory_2,btn_monitor_2,btn_computer_case_2,
                             btn_procecor_2,btn_hdd_ccd_memory_2,btn_power_block_2,btn_motherboard_2,btn_back_config,width=2)




# ниже тупо ссылки на пырвый полный сетап
monitor_button = InlineKeyboardButton(
    text='Монитор',
    url='https://enter.kg/monitory_bishkek/6a226d380a86312a0d5edf98ccfff697-detail'
)
case_button = InlineKeyboardButton(
    text='Корпус',
    url='https://enter.kg/korpusa_bishkek/903ea63a7042e4fddbb7f4d20160f7e3-detail'
)
procecor_button = InlineKeyboardButton(
    text='Процессор',
    url='https://enter.kg/processory_bishkek/intel-pentium-dual-core_bishkek/2d79fef89f5ae9736331a78d97f6c9f6-detail'
)
oper_memory_button = InlineKeyboardButton(
    text='Оперативная память',
    url='https://enter.kg/operativnaya-pamyat_bishkek/ddr-4_bishkek/f545d3a532cb48a95b140847b04891c9-detail'
)
videocard_button = InlineKeyboardButton(
    text='Видео карта',
    url='https://enter.kg/videokarty_bishkek/f5667fe598922bea58cb079eb2be2d4f-detail'
)
hdd_ccd_memory_button = InlineKeyboardButton(
    text='Жесткий диск',
    url='https://enter.kg/vnutrennie-zhestkie-diski_bishkek/b1efa8ac458c110ec108e4632ebe1351-detail'
)
culler_button = InlineKeyboardButton(
    text='Кулер',
    url='https://enter.kg/sistemy-ohlazhdeniya_bishkek/2f2d2e78226ace2e2d73c8f4bcaea8e9-detail'
)
power_block_button = InlineKeyboardButton(
    text='Блок питания',
    url='https://enter.kg/bloki-pitaniya-dlya-pk_bishkek/p30307_power-unit-delux-dlp-21d_bishkek-detail'
)
motherboard_button = InlineKeyboardButton(
    text='Материнская плата',
    url='https://enter.kg/nenuzhnoe_bishkek/f6596aa9c514c1a05e8ebab9f6e4862d-detail'
)

first_fullBlock = InlineKeyboardBuilder()
first_fullBlock.row(procecor_button,motherboard_button, videocard_button,monitor_button,case_button,oper_memory_button,
                    hdd_ccd_memory_button, culler_button, power_block_button, btn_back_config,btn_next_config_2, width=3)


# теперь ФУЛЛ сетап номер 2


monitor_button_2 = InlineKeyboardButton(
    text='Монитор',
    url=f_2monitor
)
case_button_2 = InlineKeyboardButton(
    text='Корпус',
    url=f_2computer_case
)
procecor_button_2 = InlineKeyboardButton(
    text='Процессор',
    url=f_2procecor
)
oper_memory_button_2 = InlineKeyboardButton(
    text='Оперативная память',
    url=f_2oper_memory
)
videocard_button_2 = InlineKeyboardButton(
    text='Видео карта',
    url=f_2videocard
)
hdd_ccd_memory_button_2 = InlineKeyboardButton(
    text='Жесткий диск',
    url=f_2hdd_ccd_memory
)
culler_button_2 = InlineKeyboardButton(
    text='Кулер',
    url=f_2culler
)
power_block_button_2 = InlineKeyboardButton(
    text='Блок питания',
    url=f_2power_block
)
motherboard_button_2 = InlineKeyboardButton(
    text='Материнская плата',
    url=f_2motherboard
)

second_fullBlock = InlineKeyboardBuilder()
second_fullBlock.row(procecor_button_2,motherboard_button_2, videocard_button_2,monitor_button_2,case_button_2,oper_memory_button_2,
                    hdd_ccd_memory_button_2, culler_button_2, power_block_button_2, btn_back_config,btn_next_config_3, width=3)



# Ниже фулблок номер 3

monitor_button_3 = InlineKeyboardButton(
    text='Монитор',
    url=f_3monitor
)
case_button_3 = InlineKeyboardButton(
    text='Корпус',
    url=f_3computer_case
)
procecor_button_3 = InlineKeyboardButton(
    text='Процессор',
    url=f_3procecor
)
oper_memory_button_3 = InlineKeyboardButton(
    text='Оперативная память',
    url=f_3oper_memory
)
videocard_button_3 = InlineKeyboardButton(
    text='Видео карта',
    url=f_3videocard
)
hdd_ccd_memory_button_3 = InlineKeyboardButton(
    text='Жесткий диск',
    url=f_3hdd_ccd_memory
)
culler_button_3 = InlineKeyboardButton(
    text='Кулер',
    url=f_3culler
)
power_block_button_3 = InlineKeyboardButton(
    text='Блок питания',
    url=f_3power_block
)
motherboard_button_3 = InlineKeyboardButton(
    text='Материнская плата',
    url=f_3motherboard
)

third_fullBlock = InlineKeyboardBuilder()
third_fullBlock.row(procecor_button_3,motherboard_button_3, videocard_button_3,monitor_button_3,case_button_3,oper_memory_button_3,
                    hdd_ccd_memory_button_3, culler_button_3, power_block_button_3, btn_back_config, width=3)



