import json
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
from handlers.start import start, help_command
from handlers.paste import (
    paste, ask_custom, get_content, ask_title, ask_format, ask_expire,
    ASK_CUSTOM, GET_CONTENT, ASK_TITLE, ASK_FORMAT, ASK_EXPIRE
)
from handlers.pastefile import (
    pastefile, ask_file_custom, handle_file, file_ask_title, file_ask_format, file_ask_expire,
    ASK_FILE_CUSTOM, WAIT_FILE, FILE_ASK_TITLE, FILE_ASK_FORMAT, FILE_ASK_EXPIRE
)

with open('config.json', 'r') as f:
    config = json.load(f)

TELEGRAM_TOKEN = config['TELEGRAM_TOKEN']

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # /paste akışı
    paste_conv = ConversationHandler(
        entry_points=[CommandHandler("paste", paste)],
        states={
            ASK_CUSTOM: [MessageHandler(filters.TEXT, ask_custom)],
            GET_CONTENT: [MessageHandler(filters.TEXT, get_content)],
            ASK_TITLE: [MessageHandler(filters.TEXT, ask_title)],
            ASK_FORMAT: [MessageHandler(filters.TEXT, ask_format)],
            ASK_EXPIRE: [MessageHandler(filters.TEXT, ask_expire)],
        },
        fallbacks=[]
    )

    # /pastefile akışı
    file_conv = ConversationHandler(
        entry_points=[CommandHandler("pastefile", pastefile)],
        states={
            ASK_FILE_CUSTOM: [MessageHandler(filters.TEXT, ask_file_custom)],
            WAIT_FILE: [MessageHandler(filters.Document.ALL, handle_file)],
            FILE_ASK_TITLE: [MessageHandler(filters.TEXT, file_ask_title)],
            FILE_ASK_FORMAT: [MessageHandler(filters.TEXT, file_ask_format)],
            FILE_ASK_EXPIRE: [MessageHandler(filters.TEXT, file_ask_expire)],
        },
        fallbacks=[]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(paste_conv)
    app.add_handler(file_conv)

    print("✅ Bot Online")  # By Rayzer
    app.run_polling()

if __name__ == "__main__":
    main()