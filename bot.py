# File: bot.py
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

# Import configuration and handlers
import config
from handlers import schedule_router

async def main() -> None:
    # Initialize Bot instance with default parse mode which will be passed to all API calls
    bot = Bot(config.BOT_TOKEN)

    # Initialize Dispatcher
    dp = Dispatcher()

    # Include routers
    dp.include_router(schedule_router)

    # Start polling
    # Remove webhook updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped manually")
    except ValueError as e:
        print(f"Configuration Error: {e}")

