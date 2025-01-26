# Telegram Bot IMEI Checker
Этот бот интегрируется с веб-сервисом [Web IMEI Checker](https://github.com/platsajacki/web_imei_checker), который позволяет проверять информацию об устройстве по его IMEI-коду.

## Функционал бота
1. Ограничение доступа с использованием белого списка пользователей.
2. Проверка информации по IMEI-коду через API веб-сервиса.
3. Ответы в удобном формате (текстовые сообщения, JSON-данные).

## Запуск проекта
1. Создаейте файл `.env` по примеру `env.example`.
2. Соберите и запустите контейнер командами:
```bash
docker build -t tg_imei_checher .
```

```bash
docker run -d --env-file .env --name tg_imei_checker tg_imei_checher
```