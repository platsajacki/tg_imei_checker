from os import getenv

MAX_MESSAGE_LENGTH = 4096

BOT_TOKEN = getenv('BOT_TOKEN', '')
ADMIN_CONTACT = getenv('ADMIN_CONTACT', '')

WEB_IMEI_CHECKER_URL = getenv('WEB_IMEI_CHECKER_URL', '')
WEB_IMEI_CHECKER_TOKEN = getenv('WEB_IMEI_CHECKER_TOKEN', '')
WEB_IMEI_CHECKER_AUTH = {'Authorization': f'Api-Key {WEB_IMEI_CHECKER_TOKEN}'}

ACCESS_ERORR_MSG = f'Ошибка доступа. Обратитесь к администратору: @{ADMIN_CONTACT}'
SERVICE_ERORR_MSG = f'Ошибка получения данных. Попробуйте позже или обратитесь к администратору: @{ADMIN_CONTACT}'
