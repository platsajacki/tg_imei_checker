from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from constants import ACCESS_ERORR_MSG
from utils import check_telegram_user


class TelegramUserValidationMiddleware(BaseMiddleware):
    """Middleware для проверки доступности пользователя в системе перед обработкой его сообщений."""

    async def __call__(
        self, handler: Callable[[Message, dict[str, Any]], Awaitable[Any]], event: TelegramObject, data: dict[str, Any]
    ) -> Any:
        """Проверяет доступ пользователя перед обработкой сообщения."""
        if not isinstance(event, Message) or not event.from_user:
            return
        telegram_id = event.from_user.id
        is_allowed = await check_telegram_user(telegram_id)
        if not is_allowed:
            await event.answer(ACCESS_ERORR_MSG)
            return
        return await handler(event, data)
