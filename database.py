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


# Функция для добавления пользователя в бд (если его еще нет)
async def save_user(telegram_id, username):
    # Проверяем, существует ли пользователь
    if not await user_exists(telegram_id):
        async with connect("users.db") as db:
            await db.execute("INSERT INTO users (telegram_id, username, status) VALUES (?, ?, 'pending')", (telegram_id, username))
            await db.commit()

# Функция для получения статуса пользователя
async def get_user_status(telegram_id):
    async with connect("users.db") as db:
        cursor = await db.execute("SELECT status FROM users WHERE telegram_id = ?", (telegram_id,))
        row = await cursor.fetchone()
        if row:
            return row[0]  # Возвращаем статус пользователя (например, 'registered')
        return None  # Если пользователя нет в базе, возвращаем None

# Функция для обновления статуса пользователя
async def update_user_status(telegram_id, status):
    async with connect("users.db") as db:
        await db.execute("UPDATE users SET status = ? WHERE telegram_id = ?", (status, telegram_id))
        await db.commit()

# Функция для удаления пользователя из базы данных
async def delete_user(telegram_id):
    async with connect("users.db") as db:
        await db.execute("DELETE FROM users WHERE telegram_id = ?", (telegram_id,))
        await db.commit()