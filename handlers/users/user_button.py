from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Мой github", url='https://github.com/jfoeks')],
        [InlineKeyboardButton(text="Казино", callback_data='cazino')],
        [InlineKeyboardButton(text="Мой тг", url='#')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)