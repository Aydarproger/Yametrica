from aiogram import F, Router
from aiogram.types import Message, PollAnswer
from aiogram.filters import Command, StateFilter
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.context import FSMContext

from . import localization as loc, keyboards as kb
from .states_menu import States
from utils import tools
from services.auth import AuthService
from services.users import UsersService
from data.config import YA_DATE_OF_BIRTH_ID, YA_EMAIL_ID, YA_FEEDBACK_ID, YA_PRIZES_ID, YA_RATING_ID, YA_START_ID, YA_USER_NAME_ID, YA_PHONE_ID


router = Router()
auth = AuthService()

#----------------------------- start handlers -----------------------------

@router.message(StateFilter(States.base_state), Command("start"))
async def start_command_authorized(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    username = message.from_user.username
    if username is None:
        username = f"user_{message.from_user.id}"
    data = await auth.auth(message.from_user.id, username)
    token = data.access_token
    await message.answer(text=loc.selecting_section(), reply_markup=kb.sections_keyboard(token, message.from_user.id))


@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    pre_start = message.text.split(' ')
    source = ''
    if len(pre_start) > 1:
        utm_source = pre_start[1]
        source = utm_source.split('-')[1]
    username = message.from_user.username
    if username is None:
        username = f"user_{message.from_user.id}"
    auth_response = await auth.auth(message.from_user.id, username, source)
    if auth_response.status:
        tools.ya_metric(counter=YA_START_ID, user_id=message.from_user.id)
    await message.answer(text=loc.start_message(), reply_markup=kb.proof_age_keyboard())
    await state.set_state(States.start)


@router.message(StateFilter(States.start), F.text == "Мне больше 18")
async def get_contact(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    await message.answer(text=loc.get_contact(), reply_markup=kb.get_contact_keyboard())
    await state.set_state(States.get_contact)


@router.message(StateFilter(States.start), F.text == "Мне меньше 18")
async def unacceptable_age(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    await message.answer(text=loc.unacceptable_age(), reply_markup=kb.proof_age_keyboard())
    await state.set_state(States.start)


@router.message(F.contact)
async def confirmation_contact_btn(message: Message, state: FSMContext, phone_number: str | None = None) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    if phone_number is None:
        phone_number = message.contact.phone_number
    username = message.from_user.username
    if username is None:
        username = f"user_{message.from_user.id}"
    auth_response = await auth.auth(message.from_user.id, username)
    if auth_response.status:
        await message.answer(text=loc.new_user(), reply_markup=kb.new_user_keyboard())
        await state.set_state(States.reg_user)
        await state.set_data({"access_token": auth_response.access_token})
        users = UsersService(auth_response.access_token)
        await users.update_field("phone", phone_number)
        return
    data = await auth.auth(message.from_user.id, username)
    token = data.access_token
    tools.ya_metric(counter=YA_PHONE_ID, user_id=message.from_user.id)
    await message.answer(text=loc.successful_registration())
    await message.answer(text=loc.selecting_section(), reply_markup=kb.sections_keyboard(token, message.from_user.id))
    await state.set_state(States.base_state)


@router.message(StateFilter(States.get_contact))
async def confirmation_contact_txt(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    phone_number = message.text
    is_correct = tools.phone_validation(phone_number)
    if not is_correct:
        await message.answer(text=loc.incorrect_phone(), reply_markup=kb.get_contact_keyboard())
        return
    tools.ya_metric(counter=YA_PHONE_ID, user_id=message.from_user.id)
    await confirmation_contact_btn(message, state, phone_number)

#----------------------------- registration handlers -----------------------------
    
@router.message(StateFilter(States.reg_user), F.text == "Зарегистрироваться")
async def reg_user(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    await message.answer(text=loc.get_fio(), reply_markup=kb.reg_keyboard())
    await state.set_state(States.get_fio)


@router.message(StateFilter(
    States.get_fio, 
    States.get_date_birth,
    States.get_email
    ), F.text == "Начать сначала")
async def start_over_reg_user(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    await get_contact(message, state)


@router.message(StateFilter(States.get_fio), F.text == "Назад")
async def get_fio_back(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    await get_contact(message, state)


@router.message(StateFilter(States.get_fio))
async def get_fio(message: Message, state: FSMContext, back: bool | None = None) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    if back is None:
        fio = message.text.split(' ')
        if len(fio) < 2:
            await message.answer(text=loc.incorrect_fio(), reply_markup=kb.reg_keyboard())
        last_name = fio[0]
        first_name = fio[1]
        data = await state.get_data()
        users = UsersService(data["access_token"])
        if len(fio) > 2:
            surname = fio[2]
            await users.update_field("surname", surname)
        await users.update_field("last_name", last_name)
        await users.update_field("first_name", first_name)
        tools.ya_metric(counter=YA_USER_NAME_ID, user_id=message.from_user.id)
    await message.answer(text=loc.get_date_birth(), reply_markup=kb.reg_keyboard())
    await state.set_state(States.get_date_birth)


@router.message(StateFilter(States.get_date_birth), F.text == "Назад")
async def get_date_birth_back(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    await reg_user(message, state)


@router.message(StateFilter(States.get_date_birth))
async def get_date_birth(message: Message, state: FSMContext, back: bool | None = None) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    if back is None:
        date_birth = message.text
        is_correct = tools.date_validation(date_birth)
        if not is_correct:
            await message.answer(text=loc.incorrect_date(), reply_markup=kb.reg_keyboard())
            return
        is_adult, age = tools.age_verification(date_birth)
        if not is_adult:
            await message.answer(text=loc.is_not_adult(), reply_markup=kb.reg_keyboard())
            return
        data = await state.get_data()
        users = UsersService(data["access_token"])
        await users.update_field("age", age)
        tools.ya_metric(counter=YA_DATE_OF_BIRTH_ID, user_id=message.from_user.id)
    await message.answer(text=loc.get_email(), reply_markup=kb.reg_keyboard())
    await state.set_state(States.get_email)


@router.message(StateFilter(States.get_email), F.text == "Назад")
async def get_email_back(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    await get_fio(message, state, True)


@router.message(StateFilter(States.get_email))
async def get_email(message: Message, state: FSMContext, back: bool | None = None) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    if back is None:
        email = message.text
    is_correct = tools.email_validation(email)
    if is_correct in (True, None):
        username = message.from_user.username
        if username is None:
            username = f"user_{message.from_user.id}"
        data = await auth.auth(message.from_user.id, username)
        token = data.access_token
        users = UsersService(token)
        await users.update_field("email", email)
        tools.ya_metric(counter=YA_EMAIL_ID, user_id=message.from_user.id)
        await message.answer(text=loc.successful_registration())
        await message.answer(text=loc.selecting_section(), reply_markup=kb.sections_keyboard(token, message.from_user.id))
        await state.set_state(States.base_state)
    else:
        await message.answer(text=loc.incorrect_email(), reply_markup=kb.reg_keyboard())
    
#----------------------------- reply sections handlers -----------------------------
    
@router.message(StateFilter(States.base_state), F.text == "Обратная связь")
async def feedback(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    username = message.from_user.username
    if username is None:
        username = f"user_{message.from_user.id}"
    data = await auth.auth(message.from_user.id, username)
    token = data.access_token
    tools.ya_metric(counter=YA_FEEDBACK_ID, user_id=message.from_user.id)
    await message.answer(text=loc.feedback(), reply_markup=kb.sections_keyboard(token, message.from_user.id))


@router.message(StateFilter(States.base_state), F.text == "Сокровища")
async def prizes(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    username = message.from_user.username
    if username is None:
        username = f"user_{message.from_user.id}"
    data = await auth.auth(message.from_user.id, username)
    token = data.access_token
    tools.ya_metric(counter=YA_PRIZES_ID, user_id=message.from_user.id)
    await message.answer_photo(photo=FSInputFile("data/files/prizes.png"), caption=loc.prizes(), reply_markup=kb.sections_keyboard(token, message.from_user.id))


@router.message(StateFilter(States.base_state), F.text == "Рейтинг")
async def rating(message: Message, state: FSMContext) -> None:
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    username = message.from_user.username
    if username is None:
        username = f"user_{message.from_user.id}"
    data = await auth.auth(message.from_user.id, username)
    token = data.access_token
    tools.ya_metric(counter=YA_RATING_ID, user_id=message.from_user.id)
    await message.answer(text=await loc.rating(token), reply_markup=kb.sections_keyboard(token, message.from_user.id))
    
#----------------------------- none state handlers -----------------------------

@router.message(StateFilter(States.base_state))
async def none_state_message(message: Message, state: FSMContext):
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    await start_command_authorized(message, state)


@router.message()
async def none_state_message(message: Message, state: FSMContext):
    if message.from_user.id in await tools.get_ban_ids():
        await message.answer(text=loc.banned_user())
        return
    await start_command(message, state)
    

@router.poll_answer()
async def poll_answer_handler(poll_answer: PollAnswer, state: FSMContext) -> None:
    if poll_answer.user.id in await tools.get_ban_ids():
        return
    question, options = tools.get_poll_data(poll_id=poll_answer.poll_id)
    auth_s = AuthService()
    data = await auth_s.auth(id=poll_answer.user.id, username=poll_answer.user.username)
    users = UsersService(token=data.access_token)
    try:
        answer = options[poll_answer.option_ids[0]]
    except:
        return
    await users.add_quiz_answer(
        question=question,
        answer=answer
    )