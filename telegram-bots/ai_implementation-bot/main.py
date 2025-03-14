import requests
import asyncio
from aiogram import Dispatcher, types, Bot
from aiogram.types import Message
import logging

TOKEN = "TOKEN" #token here (obviously i won't put any of mines)

bot = Bot(token=TOKEN)
dp = Dispatcher()

url = "https://api.intelligence.io.solutions/api/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer TOKEN_HERE"
}

@dp.message()
async def response_from_ai(message: Message):

    user_input = message.text

    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "system",
                "content": "you are a chat bot in telegram named @BOT_TAG. (you can put here any description you want bot to be aware of"
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    fresponse = response.json()

    text = fresponse['choices'][0]['message']['content']
    ftext = text.split("</think>\n\n")[1]

    print(ftext)
    await message.answer(ftext)



async def main():
    logging.basicConfig(level = logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
