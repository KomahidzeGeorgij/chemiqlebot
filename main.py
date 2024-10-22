import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import config
from database import create_users_table, get_user_status, update_user_status, save_user, delete_user

# Создаем экземпляр бота и диспетчера
bot = Bot(token=config.TOKEN)
dp = Dispatcher()
veb = config.VEBINAR
share = config.GROUPSHARE

# Обработка команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    # Добавляем пользователя в бд при первом запуске
    await save_user(message.from_user.id, message.from_user.username)

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Регистрация")],
            [types.KeyboardButton(text="Справка")]
        ],
        resize_keyboard=True
    )

    await message.answer("Привет! Нажми 'Регистрация', чтобы зарегистрироваться на вебинар.", reply_markup=keyboard)


# Обработка кнопки "Справка"
@dp.message(lambda message: message.text == "Справка")
async def help_command(message: Message):
    await message.answer("Этот бот помогает зарегистрироваться на вебинар. Для начала нажмите 'Регистрация'.")


# Обработка кнопки "Регистрация"
@dp.message(lambda message: message.text == "Регистрация")
async def register(message: Message):
    # Проверяем, есть ли пользователь в бд и его статус
    user_status = await get_user_status(message.from_user.id)

    try:
        # Проверяем, состоит ли пользователь в группе
        member = await bot.get_chat_member(config.GROUP_CHAT_ID, message.from_user.id)

        if member.status in ["member", "administrator", "creator"]:
            # Если пользователь в группе и статус зарегистрирован, отправляем ссылку
            if user_status == "registered":
                await message.answer(
                    "Вы уже зарегистрированы! Вот ваша ссылка на вебинар: https://www.youtube.com/watch?v=d3ql-gGtDmk")
            else:
                # Если пользователь не зарегистрирован, обновляем статус и отправляем ссылку
                await update_user_status(message.from_user.id, "registered")
                await message.answer(
                    "Регистрация успешна! Вот ваша ссылка на вебинар: https://www.youtube.com/watch?v=d3ql-gGtDmk")
        else:
            # пользователя нет в бд
            await delete_user(message.from_user.id)
            await message.answer(
                "Вы не состоите в группе! Пожалуйста, вступите в группу, чтобы зарегистрироваться: https://t.me/+fxtsvv4TQ0lkYTgy")

    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}") #задолбали ошибки, бд не гуд


# Запуск бота
async def main():
    await create_users_table()  # Создаем таблицу перед началом работы бота
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())