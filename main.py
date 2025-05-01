from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Перейти в магазин", url="https://t.me/BLACKWHITE_VAPE")],
        [InlineKeyboardButton("Связаться с менеджером", url="https://t.me/blackwhitevape")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Добро пожаловать в наш магазин, где мы предлагаем широкий ассортимент жидкостей для вейпа и снюса! Здесь вы найдете только качественные продукты, которые подарят вам незабываемые вкусовые ощущения.\n\nМы готовы помочь вам выбрать идеальный вкус и ответить на все ваши вопросы. Не стесняйтесь обращаться — наш дружелюбный бот всегда на связи! Наслаждайтесь покупками и оставайтесь с нами для получения актуальных новинок и акций!",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
