import os
from dotenv import load_dotenv


load_dotenv()

AUTH_GRPC_URL = os.getenv('AUTH_GRPC_URL')
GAME_GRPC_URL = os.getenv('GAME_GRPC_URL')
USERS_GRPC_URL = os.getenv('USERS_GRPC_URL')

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')
YA_METRIC_TOKEN = os.getenv('YA_METRIC_TOKEN')

RISKS_URL = os.getenv('RISKS_URL')
USER_AGREEMENT_URL = os.getenv('USER_AGREEMENT_URL')
SITE_RULES_URL = os.getenv('SITE_RULES_URL')
INFORMATION_AGREEMENT_URL = os.getenv('INFORMATION_AGREEMENT_URL')
POLICY_URL = os.getenv('POLICY_URL')

GAME_URL = os.getenv('GAME_URL')
PRODUCTS_URL = os.getenv('PRODUCTS_URL')
JOURNAL_URL = os.getenv('JOURNAL_URL')
ABOUT_BRAND_URL = os.getenv('ABOUT_BRAND_URL')

YA_DATE_OF_BIRTH_ID = int(os.getenv('YA_DATE_OF_BIRTH_ID'))
YA_EMAIL_ID = int(os.getenv('YA_EMAIL_ID'))
YA_FEEDBACK_ID = int(os.getenv('YA_FEEDBACK_ID'))
YA_PRIZES_ID = int(os.getenv('YA_PRIZES_ID'))
YA_RATING_ID = int(os.getenv('YA_RATING_ID'))
YA_START_ID = int(os.getenv('YA_START_ID'))
YA_USER_NAME_ID = int(os.getenv('YA_USER_NAME_ID'))
YA_PHONE_ID = int(os.getenv('YA_PHONE_ID'))
YA_GAME_ID = int(os.getenv('YA_GAME_ID'))