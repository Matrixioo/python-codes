# Telegram AI Chatbot

This Telegram bot is written in Python using **aiogram**. It interacts with an AI API to process user messages and provide intelligent responses.

## Libraries Used

- **requests** — Used for making HTTP requests to the AI API, sending user input, and receiving responses.
- **asyncio** — Enables asynchronous execution, allowing the bot to handle multiple messages concurrently without blocking.
- **aiogram** — A modern and efficient framework for building Telegram bots in Python, simplifying interaction with Telegram's API.
- **logging** — Provides logging functionality to track errors and events, making debugging easier.

## How the Bot Works

1. **Receiving a message:**
   - The bot listens for incoming messages using the `@dp.message()` handler from `aiogram`.
   - When a user sends a message, it triggers the corresponding function.

2. **Processing the message:**
   - The bot extracts the text message from the user.
   - A JSON request is formatted with the message and sent to the AI API.

3. **Communicating with the AI API:**
   - The request is sent to `https://api.intelligence.io.solutions/api/v1/chat/completions`.
   - The request contains:
     - The AI model being used (`deepseek-ai/DeepSeek-R1`).
     - The system's instructions defining the bot’s personality.
     - The user's message.

4. **Receiving and extracting AI response:**
   - The API responds with a JSON object containing AI-generated text.
   - The relevant content is extracted from the response.
   - Some formatting is done to remove unnecessary text.

5. **Sending the AI response back to Telegram:**
   - The bot sends the AI's response back to the user in Telegram.
   - The process repeats for each new user message.

## How to Run the Bot

1. **Install dependencies**
   ```sh
   pip install aiogram requests
   ```
2. **Create a Telegram bot**
   - Open Telegram and search for `@BotFather`.
   - Use the `/newbot` command to create a new bot.
   - Follow the instructions to obtain a bot token.

3. **Add your API key**
   - Replace `YOUR_API_KEY` in the script with your actual AI API key.
   - Replace `YOUR_BOT_TOKEN` with the token obtained from BotFather.

4. **Run the bot**

# TO DO
## Done
- **Error handling.** Implement error handling to manage API failures and invalid responses.
- **Memory.** So that the bot could remember past messages from the user, so the conversation would be more natural.
## To be done
- **Improve memory.** Apparently, memory sometimes functions poorly. The bot may perceive the installations as a message, which should not occur. It would be wise to change the memory library.
- **Optimization.** Supposedly not possible since the performance speed is mainly depends on the API answering speed. The best possible solution is to switch to a paid API.
