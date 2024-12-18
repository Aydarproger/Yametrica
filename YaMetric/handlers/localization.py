from services.game import GameService
from data import config


def start_message() -> str:
    return ('Пожалуйста, подтвердите, '
            'что Вам исполнилось 18 лет, '
            'Вы являетесь потребителем табака '
            'и постоянно проживаете на территории РФ.\n\n'
            f'<a href="{config.RISKS_URL}">Риски, связанные со здоровьем</a>')
    
    
def get_contact() -> str:
    return ('Осталась всего пара вопросов для регистрации, и ты сможешь окунуться в мир Captain Jack.\n\n'
            'Введите Ваш номер телефона или поделитесь им, кликнув '
            '«Поделиться номером». Так как Вы даете свое согласие '
            'на обработку персональных данных и подтверждаете, что '
            f'ознакомились и согласны с нашим <a href="{config.USER_AGREEMENT_URL}">Пользовательским соглашением</a> '
            f'и с <a href="{config.SITE_RULES_URL}">Правилами сайта</a>.')
    
    
def test_contact(phone_number: str) -> str:
    return f'Ваш номер {phone_number}'


def confirmation_contact() -> str:
    return 'Для подтверждения номера телефона, пожалуйста, введите код из SMS сообщения'


def resending_sms_code() -> str:
    return 'Код отправлен повторно'


def unacceptable_age() -> str:
    return 'По законам РФ, взаимодействовать с нашим сервисом могут только пользователи старше 18 лет'


def new_user() -> str:
    return ('Похоже, Вы еще не зарегистрированы.\n\n'
            'Зарегистрируйтесь, чтобы получить полный доступ '
            'к бренду Captain Jack.\n\n'
            f'Регистрируясь, Вы принимаете условия <a href="{config.INFORMATION_AGREEMENT_URL}">Соглашения о предоставлении информации</a> '
            'и даете согласие на обработку персональных данных в соответствии с '
            f'<a href="{config.POLICY_URL}">Политикой в отошении обработки персональных данных</a>.')
    
    
def get_surname() -> str:
    return 'Введите, пожалуйста, Вашу фамилию.'


def get_name() -> str:
    return 'Введите, пожалуйста, Ваше имя.'


def get_patronymic() -> str:
    return 'Введите, пожалуйста, Ваше отчество.'


def get_date_birth() -> str:
    return ('Для подтверждения возраста укажите, пожалуйста, Вашу дату рождения.\n\n'
            'Введите дату в формате ДД.ММ.ГГГГ')
    
    
def get_email() -> str:
    return ('Осталась пара шагов до завершения регистрации.\n\n'
            'Укажите, пожалуйста, свой email.')


def get_passport() -> str:
    return ('Последний шаг — подтвердите свой возраст.\n\n'
            'Приложите, пожалуйста, фото паспорта или водительского удостоверения.')
    
    
def successful_registration() -> str:
    return ('Спасибо, Вы успешно зарегистрированы!\n\n'
            'Теперь вы можете окунуться в мир Captain Jack.')
    
    
def selecting_section() -> str:
    return 'Выберите один из интересующих Вас разделов ниже'


def passport_not_document() -> str:
    return 'Пожалуйста, приложите Ваш паспорт документом'


def feedback() -> str:
    return ('Вы можете поделиться с нами предложениями и пожеланиями, написав нам на почту:\n\n'
            'brand@i-tob.ru')


def incorrect_date() -> str:
    return 'Пожалуйста, введите дату в верном формате'


def is_not_adult() -> str:
    return 'Похоже, что Вы не достигли 18 лет'


def incorrect_email() -> str:
    return 'Пожалуйста, введите верный email'


def incorrect_phone() -> str:
    return 'Пожалуйста, введите верный номер'


def prizes() -> str:
    return ('<b>Топ-30</b> игроков с наибольшим количеством баллов получают следующие призы:\n\n'
            '<b>1-10 место</b> — подписка Amediateka на 3 месяца.\n\n'
            '<b>11-30 место</b> — сертификат Ozon на 500 рублей.')
    
    
async def rating(token: str) -> str:
    game = GameService(token)
    text = '<b>Топ-10 лучших в игре «Сокровища Капитана Джека»:</b>\n\n'
    i = 1
    async for user in game.get_rating(10):
        text += f'{i}. {user.username} — {user.score}\n'
        i += 1
    text += '\nВойдите в <b>Топ-30</b> и выигрывайте призы!'
    return text


def banned_user() -> str:
    return 'Вы забанены администрацией бота'


def game_off() -> str:
    return 'Игра отключена'


def game_on() -> str:
    return 'Игра включена'


def game_season_off() -> str:
    return 'Сезон игры закончился!'


def game_season_on() -> str:
    return 'Сезон игры начался!'


def get_fio() -> str:
    return 'Введите ФИО в формате "Фамилия Имя Отчество", где Отчество указывается по желанию'
    

