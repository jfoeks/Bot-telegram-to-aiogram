from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButton
def admin_key():
    kb = [
        [KeyboardButton(text="Изменить начальную фотографию",)],
    ]
    return ReplyKeyboardMarkup(keyboard=kb)
