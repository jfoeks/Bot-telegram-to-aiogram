import os.path
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, F,types
from aiogram.filters import Command
from aiogram.types import Message
from data.config import admins,bot
from .user_button import ease_link_kb
from utils.sql_manager import *
router = Router()

class PhotoStates(StatesGroup):
    waiting_for_photo = State()

@router.message(Command(commands=['start']))
async def start_command1(message: Message):
    user_id = message.from_user.id
    USER.get_user_id(user_id=user_id)
    try:
        await message.answer_photo(photo=IMAGE.get_image_all()[0],reply_markup=ease_link_kb())
    except Exception as e:
        await message.answer('Приветственной фотографии пока нету')

@router.message(Command(commands=['id']))
async def userid(message:Message):
    user_id = message.from_user.id
    await message.answer(f'Ваш айди {user_id}')

@router.callback_query(lambda c: c.data == 'cazino')
async def cazino(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_dice(callback_query.from_user.id,emoji='🎰')




