import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import random
from databawse import db_start, create_profile, get_balance, edit_profile
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "token" #token here (obviously i won't put any of mines)

bot = Bot(token=TOKEN)
dp = Dispatcher()

#a keyboard which has two options of /balance command and gambling commands
#so you won't need to print them each time again
def gamble_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text = "/balance")
    kb.button(text = "🦞")
    return kb.as_markup(resize_keyboard=True)

gamble_slots = [("🍋"), ("7️⃣"), ("🍒"), ("🍈"), ("🍐"), ("⭐️")]

help_command = """
/help - get the full list of commands
/start - start chatting with the bot
/balance - your balance value
🦞 - gambling (slot machine)
"""

#short desc
@dp.message(Command("start"))
async def start(message: types.Message) -> None:
    keyboard = gamble_keyboard()
    await message.answer("hi! can do whatever you ask from /help", reply_markup=keyboard)
    await message.delete()

    await create_profile(user_id = message.from_user.id)

#get some help
@dp.message(Command("help"))
async def help(message: types.Message) -> None:
    await message.answer(help_command)

@dp.message(Command("balance"))
async def ask_for_balance(message: types.Message) -> None:
    balance = await get_balance(message.from_user.id)
    await message.answer(f"your balance: {balance}")

#GAMBLING
@dp.message()
async def gamble(message: types.Message) -> None:
    balance = await get_balance(message.from_user.id)

    slot1 = random.choice(gamble_slots)
    slot2 = random.choice(gamble_slots)
    slot3 = random.choice(gamble_slots)

    if message.text == "🦞":
        await message.answer(slot1 + slot2 + slot3)
        await message.answer(f"you got {await check_slots(slot1, slot2, slot3, balance, message.from_user.id)}")

#this function checks which slots do you have and gives you money respectivly (not real money xd)
async def check_slots(slot1, slot2, slot3, balance, user_id) -> int:
    #jackpot
    if slot1 == "7️⃣" and slot2 == "7️⃣" and slot3 == "7️⃣":
        new_balance = balance + 300
        await edit_profile(user_id, new_balance)
        return 300
    #40
    elif slot1 == "🍋" and slot2 == "🍋" and slot3 == "🍋":
        new_balance = balance + 40
        await edit_profile(user_id, new_balance)
        return 40
    #30
    elif slot1 == "🍒" and slot2 == "🍒" and slot3 == "🍒":
        new_balance = balance + 30
        await edit_profile(user_id, new_balance)
        return 30
    #50
    elif slot1 == "🍈" and slot2 == "🍈" and slot3 == "🍈":
        new_balance = balance + 50
        await edit_profile(user_id, new_balance)
        return 50
    #25
    elif slot1 == "🍐" and slot2 == "🍐" and slot3 == "🍐":
        new_balance = balance + 25
        await edit_profile(user_id, new_balance)
        return 25
    #100
    elif slot1 == "⭐️" and slot2 == "⭐️" and slot3 == "⭐️":
        new_balance = balance + 100
        await edit_profile(user_id, new_balance)
        return 100
    #any other combination
    else:
        new_balance = balance - 10
        await edit_profile(user_id, new_balance)
        return -10

async def main():
    logging.basicConfig(level = logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
