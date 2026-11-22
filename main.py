import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = "https://sozaevvv.github.io/UzParking/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "Привет! 👋 Добро пожаловать в UzParking!\n\n"
        "Умный поиск, AI-прогноз загруженности и бронирование парковок в Ташкенте прямо в Telegram.\n\n"
        "Жми кнопку ниже, чтобы открыть интерактивную карту! 🚀"
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🚗 Открыть UzParking", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])

    await message.answer(text, reply_markup=keyboard)

async def main():
    print("Бот запущен и ждет команду /start...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
