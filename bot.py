import json
import logging
import os
import random
from pathlib import Path

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

DATA_FILE = Path(__file__).with_name("word_list.json")


def load_units():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    units = data.get("units", [])
    if not units:
        raise ValueError("word_list.json ichida units topilmadi")
    return units


def all_words(units):
    return [word for unit in units for word in unit.get("words", [])]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Inglizcha so'zlarni o'rganamiz.\n\n"
        "/random — tasodifiy so'z\n"
        "/unit 1 — unit bo'yicha so'zlar\n"
        "/help — yordam"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


async def random_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        word = random.choice(all_words(load_units()))
    except (OSError, ValueError, json.JSONDecodeError, IndexError) as error:
        logging.exception("So'zlar yuklanmadi: %s", error)
        await update.message.reply_text("So'zlar faylini o'qishda xatolik yuz berdi.")
        return

    await update.message.reply_text(f"📚 {word['word']}\n🇺🇿 {word['meaning']}")


async def unit_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Iltimos, unit raqamini yozing. Masalan: /unit 1")
        return

    unit_number = int(context.args[0])
    try:
        unit = next(unit for unit in load_units() if unit.get("unit") == unit_number)
    except (OSError, ValueError, json.JSONDecodeError, StopIteration) as error:
        logging.exception("Unit yuklanmadi: %s", error)
        await update.message.reply_text(f"Unit {unit_number} topilmadi.")
        return

    words = unit.get("words", [])
    text = f"📖 Unit {unit_number}\n\n" + "\n".join(
        f"• {word['word']} — {word['meaning']}" for word in words
    )
    await update.message.reply_text(text)


def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN environment variable o'rnatilmagan")

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("random", random_word))
    application.add_handler(CommandHandler("unit", unit_words))
    application.run_polling()


if __name__ == "__main__":
    main()
