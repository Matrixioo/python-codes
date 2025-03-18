# Telegram Slot Machine Bot

This Telegram bot implements a simple gambling game (slot machine). It allows users to check their balance and play the slot machine, modifying the balance depending on the symbols rolled. Thi was created to practice working with databases and asynchronous programming in Python using the Aiogram library.

## Features
- Checks user's balance
- Play a gambling game (slot machine) with balance updates
- Store user data in an SQLite database

## Technologies Used
- **Asyncio**: Python library for writing asynchronous code, used to handle multiple tasks without blocking the bot.
- **Aiogram**: Asynchronous Telegram bot framework, used for handling user interactions and commands.
- **SQLite (Aiosqlite)**: Lightweight database for storing user data asynchronously.
- **Random**: Python module for generating random slot machine results.

## File Descriptions
### `main.py`
This file contains the bot logic. It handles commands, generates random slot values, and updates user balances.

### `databawse.py`
This file manages interactions with the SQLite database.

## Bot Commands
| Command  | Description |
|----------|-------------|
| `/start` | Start the bot and create a profile |
| `/help`  | Display the list of commands |
| `/balance` | Check your current balance |
| Slot machine symbol | Play the slot machine |

## Slot Machine Logic
The bot randomly selects three symbols from the list:
```python
gamble_slots = ["Lemon", "7", "Cherry", "Melon", "Pear", "Star"]
```

Winning conditions:
- `777` → +300
- `Lemon Lemon Lemon` → +40
- `Cherry Cherry Cherry` → +30
- `Melon Melon Melon` → +50
- `Pear Pear Pear` → +25
- `Star Star Star` → +100
- Any other combination → -10

## TO DO
- Switch to PostgreSQL.
- Betting for higher rewards. Maybe (?).
- Would be nice to add other betting games as well.
