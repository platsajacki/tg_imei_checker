from http import HTTPStatus

from aiohttp import ClientSession

from constants import SERVICE_ERORR_MSG, WEB_IMEI_CHECKER_AUTH, WEB_IMEI_CHECKER_URL


async def check_telegram_user(telegram_id: int) -> bool:
    """Метод для запроса к внешнему API и проверки доступа пользователя."""
    url = f'{WEB_IMEI_CHECKER_URL}telegram-users/{telegram_id}/'
    async with ClientSession() as session:
        async with session.get(url, headers=WEB_IMEI_CHECKER_AUTH) as response:
            if response.status == HTTPStatus.OK:
                data = await response.json()
                return data.get('is_allowed', False)
    return False


async def check_imei(device_id: str) -> str | dict:
    """Проверяет IMEI устройства через внешний API."""
    url = f'{WEB_IMEI_CHECKER_URL}check-imei/'
    async with ClientSession() as session:
        async with session.post(url, headers=WEB_IMEI_CHECKER_AUTH, data={'device_id': device_id}) as response:
            data = await response.json()
            match response.status:
                case HTTPStatus.OK:
                    return data['data']
                case HTTPStatus.BAD_REQUEST:
                    return data['device_id'][0]
            return SERVICE_ERORR_MSG
