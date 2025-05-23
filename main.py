from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

ADMIN_ID = 1612476345

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام عزیز! پیام ناشناس‌تو بفرست 😉")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message_text = update.message.text
    username = user.username or "نداره"
    user_id = user.id

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"پیام ناشناس جدید:\n\n{message_text}\n\n👤 از: @{username} (ID: {user_id})"
    )

    await update.message.reply_text("مرسی! پیامت فرستاده شد ✅")

app = ApplicationBuilder().token("8050518543:AAFUWYzmWkMIIsi5YnwbKYUVO_gLTVkTrhs").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
