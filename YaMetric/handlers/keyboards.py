from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

from utils.tools import get_admins, get_game_status
from data.config import GAME_URL, ABOUT_BRAND_URL, PRODUCTS_URL, JOURNAL_URL, YA_GAME_ID


def proof_age_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text='Мне больше 18')],
        [KeyboardButton(text='Мне меньше 18')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard


def get_contact_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text='Поделиться номером', request_contact=True)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard


def confirmation_contact_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text='Отправить код повторно')],
        [KeyboardButton(text='Начать сначала')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard


def new_user_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text='Зарегистрироваться')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard


def reg_keyboard(skipping_step: bool | None = None) -> ReplyKeyboardMarkup:
    if skipping_step:
        buttons = [
            [KeyboardButton(text='Пропустить шаг')],
            [KeyboardButton(text='Назад')],
            [KeyboardButton(text='Начать сначала')]
        ]
    else:
        buttons = [
            [KeyboardButton(text='Назад')],
            [KeyboardButton(text='Начать сначала')]
        ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard


def sections_keyboard(token: str, user_id: int) -> ReplyKeyboardMarkup:
    buttons = [
        [
            KeyboardButton(text='О бренде', web_app=WebAppInfo(url=ABOUT_BRAND_URL)),
            KeyboardButton(text='Журнал', web_app=WebAppInfo(url=JOURNAL_URL))
        ],
        [
            KeyboardButton(text='Продукция', web_app=WebAppInfo(url=PRODUCTS_URL)),
            KeyboardButton(text='Обратная связь')
        ],
        [
            KeyboardButton(text='Сокровища'),
            KeyboardButton(text='Pейтинг')
        ]
    ]
    if get_game_status():
        buttons.append([KeyboardButton(text='На абордаж!', web_app=WebAppInfo(url=GAME_URL + token + '&tg_user_id=' + user_id + '&ym_counter_id=' + YA_GAME_ID))])
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard




