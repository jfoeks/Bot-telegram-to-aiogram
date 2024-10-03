from aiogram import Router,F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from handlers.admins.admin_filters import AdminFilter
from .admin_button import *
from ..users.startcommands import PhotoStates
from utils.sql_manager import *
from handlers.users.user_button import *

router = Router()
@router.message(Command(commands=['start']),AdminFilter())
async def start_admin(message: Message):
    await message.answer('/user_start',reply_markup=admin_key())

@router.message(Command(commands=['user_start']),AdminFilter())
async def start_admin(message: Message):
    try:
        await message.answer_photo(photo=IMAGE.get_image_all()[0],reply_markup=ease_link_kb())
    except Exception as e:
        await message.answer('Добавьте фотографию',reply_markup=admin_key())

@router.message(lambda message: message.text == "Изменить начальную фотографию", AdminFilter())
async def process_post_callback(message: Message, state: FSMContext):
    await message.answer("Отправьте мне фотографию.")
    await state.set_state(PhotoStates.waiting_for_photo)

@router.message(F.photo, PhotoStates.waiting_for_photo, AdminFilter())
async def photo_handler(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    IMAGE.create_image(photo_id)
    await message.answer('Фотография обновлена')
    await state.clear()