from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing from .env file!")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def receive_message(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    text = message.text
    print(f"Message from telegram: {user_id} - @{username}: {text}")


async def main():
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
