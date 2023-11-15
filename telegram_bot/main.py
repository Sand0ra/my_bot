import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


from handlers import router
from config import TOKEN
import sys



logging.basicConfig(level=logging.INFO)










# Запуск процесса поллинга новых апдейтов
async def main():
    
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)
    




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')