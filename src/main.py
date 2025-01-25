import asyncio
import json
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from constants import BOT_TOKEN, MAX_MESSAGE_LENGTH
from middlewares import TelegramUserValidationMiddleware
from utils import check_imei

dp = Dispatcher()
dp.message.middleware(TelegramUserValidationMiddleware())


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer('Привет! Можно отправить IMEI, я проверю!')


@dp.message()
async def imei_handler(message: Message) -> None:
    if not message.text:
        return
    response = await check_imei(message.text)
    if isinstance(response, dict):
        response = json.dumps(response, indent=4)
    while len(response) > MAX_MESSAGE_LENGTH:
        await message.answer(response[:MAX_MESSAGE_LENGTH])
        response = response[MAX_MESSAGE_LENGTH:]


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
