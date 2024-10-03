from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from data.config import bot
from handlers.users import startcommands
from handlers.admins import admin_commands
from utils.notify_admins import start

# Инициализация бота и диспетчера
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


routers = [admin_commands.router,startcommands.router]
for router in routers:
    dp.include_router(router)

async def main():
    await start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
