from aiosqlite3 import connect

# Создаем таблицу users, если она не существует
async def create_users_table():
    async with connect("users.db") as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE,
                username TEXT,
                status TEXT
            )
        ''')
        await db.commit()

# Функция для проверки наличия пользователя в базе данных
async def user_exists(telegram_id):
    async with connect("users.db") as db:
        cursor = await db.execute("SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,))
        row = await cursor.fetchone()
        return row is not None