import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from bs4 import BeautifulSoup
import aiohttp

TOKEN = "token" #your token from @botfather

bot = Bot(token=TOKEN)
dp = Dispatcher()

help_list = """
/start - start
/help - list of commands
/recipe - type '/recipe {name} to get the desired persona recipe'
"""

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("hello! type /help in order to see list of all bot's capabilities")

@dp.message(Command('help'))
async def help(message: types.Message):
    await message.answer(help_list)

@dp.message(Command('recipe'))
async def fusion_recipe(message: types.Message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.answer('you need to write a persona name, in form of /recipe (persona name)')
        return
    persona = args[1].title()
    search_url = f"https://aqiu384.github.io/megaten-fusion-tool/p5r/personas/{persona}/fissions"
    headers = {"User-Agent": "Mozilla/5.0"}

    async with aiohttp.ClientSession() as session:
        #print(search_url)
        async with session.get(search_url, headers=headers) as response:
            if response.status != 200:
                await message.answer("data error, persona could have been not found")
                return

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            #print(soup)
            fusion_recipes = soup.find("meta", attrs={"name": "description"})

            if fusion_recipes and "content" in fusion_recipes.attrs:
                persona_names = fusion_recipes["content"]

                persona_names = persona_names.split(" = ", 1)[1]
                fusion_list = persona_names.split(", ")[:3]
                filtered_fusion_list = ", ".join(fusion_list)

                await message.answer(f"found recipe for {persona}: \n{filtered_fusion_list}")
            else:
                await message.answer(f"there's likely no available fusion recipes for {persona}")
                return

async def main():
    logging.basicConfig(level = logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
