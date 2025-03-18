import aiosqlite as sq

db = None

async def db_create(): #creates a new database
    global db
    db = await sq.connect('messages.db')

    await db.execute("""
        CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_id INTEGER, 
        role TEXT, 
        content TEXT)""")

    await db.commit()

async def get_last_message(user_id): #gets last 5 messages from the user and the bot
    if db is None:
        await db_create()

    cursor = await db.execute(
        "SELECT role, content FROM messages WHERE user_id = ? ORDER BY id DESC LIMIT 5", (user_id,)
    )
    messages = await cursor.fetchall()
    await cursor.close()

    return [{"role": role, "content": content} for role, content in reversed(messages)]

async def save_message(user_id, role, content): #saves last 5 messages from the bot and the user
    if db is None:
        await db_create()

    await db.execute("INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)", (user_id, role, content))
    await db.commit()

    await db.execute("DELETE FROM messages WHERE user_id = ? AND id NOT IN (SELECT id FROM messages WHERE user_id = ? ORDER BY id DESC LIMIT 10)", (user_id, user_id))


# async def close_db(): #stops database func
#     if db is not None:
#         await db.close()
