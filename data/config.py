from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = '#' #bot_token
bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(bot=bot)


admins = []#id admins