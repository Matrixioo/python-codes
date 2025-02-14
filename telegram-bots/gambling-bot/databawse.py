import aiosqlite as sq

db = None

async def db_start() -> None: #creates a new database
    global db
    db = await sq.connect('money.db')

    await db.execute(
        "CREATE TABLE IF NOT EXISTS profile (user_id TEXT PRIMARY KEY, balance INTEGER)"
    )
    await db.commit()

async def create_profile(user_id) -> None: #creates a profile if it doesn't exist
    if db is None:
        await db_start()

    await db.execute("INSERT OR IGNORE INTO profile (user_id, balance) VALUES (?, ?)", (user_id, 0))
    await db.commit()

async def get_balance(user_id) -> tuple:
    if db is None:
        await db_start()

    cursor = await db.execute("SELECT balance FROM profile WHERE user_id = ?", (user_id,))
    result = await cursor.fetchone()
    await cursor.close()

    if result:
        return result[0]
    else:
        await create_profile(user_id)
        return 0

async def edit_profile(user_id, new_balance) -> None: #edits a profile, such as the balance state of a user
    if db is None:
        await db_start()

    await db.execute("UPDATE profile SET balance = ? WHERE user_id = ?", (new_balance, user_id))
    await db.commit()

async def close_db() -> None: #stops database func
    if db is not None:
        await db.close()