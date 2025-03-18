import requests
import asyncio
from aiogram import Dispatcher, types, Bot
from aiogram.types import Message
import logging
from ai_memory import db_create, get_last_message, save_message

TOKEN = "TOKEN" #your BOT_TOKEN from @BotFather here

bot = Bot(token=TOKEN)
dp = Dispatcher()

url = "https://api.intelligence.io.solutions/api/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer API_KEY" #your API key for an AI instead of API_KEY
}

@dp.message()
async def response_from_ai(message: Message):
    user_id = message.from_user.id
    user_input = message.text

    await save_message(user_id, "user", message.text)

    message_history = await get_last_message(user_id)

    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "system",
                "content": """
                bot installations description goes here"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ] + message_history
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        fresponse = response.json()

        if "choices" in fresponse and fresponse["choices"]:
            text = fresponse['choices'][0]['message']['content']
            ftext = text.split("</think>\n\n")[1]

            await save_message(user_id, "assistant", ftext)

            await message.answer(ftext)
            print(ftext)
        else:
            await message.answer("An error has occurred")
            return "An AI has returnd an incorrect answer"

    except Exception as e:
        return f"An error has occurred: {e}"


async def main():
    logging.basicConfig(level = logging.INFO)
    await db_create()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
