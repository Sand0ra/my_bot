from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
# from handlers.config import TOKEN

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
TOKEN = '6731913392:AAEKKGoVCbVB7tKPuI__8G6oBE_Ks4deVSE'

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаем объекты инлайн-кнопок
url_button_1 = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',
    url='https://stepik.org/120924'
)
url_button_2 = InlineKeyboardButton(
    text='Процессор',
    url='https://ultra.kg/catalog/komplektuyushchie-dlya-kompyutera/protsessory-intel/protsessor-intel-core-i5-11400f-lga1200-2-60-4-40ghz-6xcores-8gt-s-12mb-cache-tray-no-vga-rocket-lak.html'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2]]
)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру c url-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "url"',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)