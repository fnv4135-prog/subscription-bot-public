import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ Бот для подписки работает! Используйте /проверьте для подтверждения подписки.")

@dp.message(Command("check"))
async def check(message: types.Message):
    await message.answer("🔍 Функция проверки подписки скоро появится здесь!")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())