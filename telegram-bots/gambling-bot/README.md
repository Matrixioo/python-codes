### General description
The telegram bot.

The main functioning of the bot is allowing you to gamble. Without using the real money, of course.
The code uses multiple vital libraries, such as asyncio, logging, aiogram, random.

---

### Short library description
- Asyncio library allows bot to compute multiple functions at the same time, therefore "synchronized". It's the most necessary library for any kind of bot, since it allows
him to keep his hard work even while dealing with thousands of users.
- Logging library is not much of a use in this code exactly (I just didn't use it). It allows you to log every error that has came up during the bot's work.
- Aiogram is the core library. It allows your code properly connect to the bot on telegram server side, send any data that is stored on the local PC to the bot and vice versa.
- Random library is initially built in python's basic libraries list. Simple enough, it is used to randomly choose slots from the list with each request for slot machine.

---

### The algorithm
- Firstly, the code gets the token to which it should "connect". The token is a special key, an identificator of each bot, be it telegram bot, discord bot, etc. It works as
a password for getting access to any bot. In case of telegram, it is aquired through @BotFather. The name, tag, photo and description of the bot can be edited also
through @BotFather.
- The code consists of @Dispatcher.message functions and other basic functions, which will be described below. Dispatcher processes commands and "tells" the code what to
execute.
- All of the functions are written in form "async def". It is important for every function to start with async, so the function would be compiled with Asyncio library.
The result of that is bot that can function with multiple user's inputs at the same time.
- The code has pre-written set of slots variations, such as 7️⃣, 🍒, 🍋, 🍈, 🍐, ⭐️. Then, it uses random library, to randomly choose set of three random variations.
If user is lucky enough and random library has chosen three 7️⃣, for instance, the user will be granted +300 "coins" on their balance.
- The balance system works through using the SQL language and aiosqlite library for SQL functions to be executed in async mode. The balance of each user is stored in 
"money.db" file, which consists of two columns, first is for the user's id, second is for the amount of money on the user's "account". A new row is created for every user.

---

### P.S.
- I didn't add the token of the bot, since I don't want anybody to easily access my bot. The same goes for the money.db file, I edited first columns as "id1", "id2" respectivly, so as to not share with everyone my telegram id. However, you can input your token and clear/delete "money.db" file, everything will work.
