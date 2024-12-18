import json
import datetime
import re
import requests
import csv
import os
from email_validator import validate_email, EmailNotValidError

from services.users import UsersService
from data.config import YA_METRIC_TOKEN


def get_admins() -> list:
    with open('data/json/admins.json', 'r') as admins_data:
        admins = json.load(admins_data)['admins']
    return admins

def phone_validation(phone: str) -> bool:
    return bool(re.match('(^8|7|\\+7)((\\d{10})|(\\s\\(\\d{3}\\)\\s\\d{3}\\s\\d{2}\\s\\d{2}))', phone))


def date_validation(date: str) -> bool:
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False
    

def age_verification(date: str) -> bool:
    today = datetime.date.today()
    year = datetime.datetime.strptime(date, '%d.%m.%Y').year
    month = datetime.datetime.strptime(date, '%d.%m.%Y').month
    day = datetime.datetime.strptime(date, '%d.%m.%Y').day
    birthdate = datetime.date(year, month, day)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age >= 18:
        return True, age
    else:
        return False, age


def email_validation(email: str) -> bool:
    try:
        validate_email(email)
        return True 
    except EmailNotValidError as err:
        return False
    

async def get_ban_ids() -> list:
    users = UsersService()
    ids = []
    async for user_id in users.get_ban_ids():
        ids.append(user_id.id)
    return ids


def get_admins() -> list:
    with open('data/json/admins.json', 'r') as admins_data:
        admins = json.load(admins_data)['admins']
    return admins


def get_game_status() -> bool:
    with open('data/json/game.json', 'r') as game_data:
        status = json.load(game_data)['status']
    if status == "True":
        return True
    return False


def set_game_status(status: bool) -> None:
    with open('data/json/game.json', 'w') as game_data:
        game_status = {
        'status': f'{status}'
        }
        game_data.write(json.dumps(game_status))
        

def get_poll_data(poll_id: int):
    with open('/root/CJ_Admin/scheduler/polls.json', 'r', encoding='utf-8') as polls_data:
        polls = json.load(polls_data)['polls']
    options = polls[poll_id].get("options")
    question = polls[poll_id].get("question")
    return question, options


def ya_metric(counter: int, user_id: int) -> None:
    date_time = datetime.datetime.now().timestamp()
    
    with open(f"data/files/csv_{user_id}_{counter}.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["UserId", "Target", "DateTime"])
        file_writer.writerow([user_id, "done", date_time])

    file = open(f"data/files/csv_{user_id}_{counter}.csv", "r").read()
    url = f"https://api-metrika.yandex.net/management/v1/counter/{counter}/offline_conversions/upload?client_id_type=USER_ID"
    headers = {
    "Authorization": f"OAuth {YA_METRIC_TOKEN}"
    }

    req = requests.post(url, headers=headers, files={"file":file})
    if req.status_code == 200:
        os.remove(f"data/files/csv_{user_id}_{counter}.csv")
        
        
def ya_metric_temp() -> None:
    for filename in os.listdir("data/files"):
        if filename.split(".")[-1] != "csv":
            continue
        file = open(filename, "r").read()
        counter = int(filename.split(".")[0].split("_")[-1])
        url = f"https://api-metrika.yandex.net/management/v1/counter/{counter}/offline_conversions/upload?client_id_type=USER_ID"
        headers = {
        "Authorization": f"OAuth {YA_METRIC_TOKEN}"
        }

        req = requests.post(url, headers=headers, files={"file":file})
        

