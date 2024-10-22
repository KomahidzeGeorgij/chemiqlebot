# chemiqle_bot

## Описание

Этот Telegram-бот предназначен для управления регистрацией пользователей на вебинары. Он позволяет пользователям зарегистрироваться, проверить свои данные и получить ссылку на мероприятие после вступления в группу.

## Функциональность

- Регистрация пользователей на вебинар.
- Проверка подписки на группу в Telegram.
- Отправка ссылки на вебинар после успешной регистрации.

## Установка

### Требования

- Python 3.7 или выше
- Установленные библиотеки:
  - `aiogram`
  - `sqlalchemy`
  - `aiosqlite3`

### Установка зависимостей

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/KomahidzeGeorgij/chemiqlebot.git
   cd chemiqlebot
   
2. Установите необходимые библиотеки:
   ```bash
   pip install -r requirements.txt

## Настройка бота

1. Откройте файл `config.py` и внесите следующие изменения:
   ```python
   TOKEN = 'Ваш токен бота'
   GROUP_CHAT_ID = 'ID вашей группы'
### ИЛИ
Используйте *@chemiqle_bot* в телеграмме.

## Запуск и Использование бота

### Запуск бота

1. Для запуска бота выполните следующую команду:
    ```bash
    python main.py

### Использование бота

Запустите бота в Telegram, найдите его по имени и нажмите "Старт".
Выберите опцию "Регистрация" для регистрации на вебинар.
Подпишитесь на группу, чтобы получить доступ к ссылке на мероприятие.
После успешной регистрации бот отправит вам ссылку на вебинар.
