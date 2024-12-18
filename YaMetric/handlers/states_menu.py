from aiogram.filters.state import State, StatesGroup


class States(StatesGroup):
    base_state = State()
    start = State()
    get_contact = State()
    reg_user = State()
    get_fio = State()
    get_date_birth = State()
    get_email = State()