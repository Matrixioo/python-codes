### General description
The telegram bot.

The main functioning of the bot is allowing you to parse a website. For my code I used https://aqiu384.github.io/megaten-fusion-tool/ as a website for parsing.
The code uses multiple libraries, such as asyncio, logging, aiogram, BeautifulSoup

---

### Short library description
- Asyncio library allows bot to compute multiple functions at the same time, therefore "synchronized". It's the most necessary library for any kind of bot, since it allows
him to keep his hard work even while dealing with thousands of users.
- Logging library is not much of a use in this code exactly (I just didn't use it). It allows you to log every error that has came up during the bot's work.
- Aiogram is the core library. It allows your code properly connect to the bot on telegram server side, send any data that is stored on the local PC to the bot and vice versa.
- BeautifulSoup is a library for parsing. It helps you to find a desirable element in website code.

---

### The algorithm
- Firstly, the code gets the token to which it should "connect". The token is a special key, an identificator of each bot, be it telegram bot, discord bot, etc. It works as
a password for getting access to any bot. In case of telegram, it is aquired through @BotFather. The name, tag, photo and description of the bot can be edited also
through @BotFather.
- The code consists of @Dispatcher.message functions and other basic functions, which will be described below. Dispatcher processes commands and "tells" the code what to
execute.
- All of the functions are written in form "async def". It is important for every function to start with async, so the function would be compiled with Asyncio library.
The result of that is bot that can function with multiple user's inputs at the same time.
- BeatifulSoup finds an element of your desire, be it by setting the 'class' of an element, arggs or any other parameters. Firstly, the code goes to the website, using
the name that the user sent us. Then, it finds a 'meta' object that has arguments name="description". For us, the 'meta' object with such arguments contains the information
we parse for. So, we extract the information that is contained in 'meta' object with such arguments and send it back to the code. Then, we make few simple changes to the text, so
it would look better. Finally, we have a result.
---

### P.S.
- I didn't add the token of the bot, since I don't want to anybody easily access my bot.
