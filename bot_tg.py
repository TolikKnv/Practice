import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8699905883:AAEhza-Vr7RBrVZny5rdWfnSX8O7M1_euE0"

API_URL = "https://api.pro-talk.ru/api/v1.0/ask"
BOT_ID = 61531

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    chat_id = str(update.message.chat_id)

    response = requests.post(API_URL, json={
        "bot_id": BOT_ID,
        "chat_id": chat_id,
        "message": user_text
    })

    data = response.json()
    answer = data.get("response", "Ошибка")

    await update.message.reply_text(answer)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()