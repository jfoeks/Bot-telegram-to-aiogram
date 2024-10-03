from data.config import admins,bot

async def start():
    for admin in admins:
        await bot.send_message(chat_id=admin,text='Бот запущен, /start')


