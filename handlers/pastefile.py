import json
from telegram.ext import ContextTypes
from telegram import Update, Document
from handlers.pastebin import paste_to_pastebin

# Config yükleme
with open('config.json', 'r') as f:
    config = json.load(f)

OWNER_ID = config['OWNER_ID']

# Conversation states
ASK_FILE_CUSTOM, WAIT_FILE, FILE_ASK_TITLE, FILE_ASK_FORMAT, FILE_ASK_EXPIRE = range(10, 15)

async def pastefile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID: return
    await update.message.reply_text("Özelleştirmek ister misin? (y/n)")
    return ASK_FILE_CUSTOM

async def ask_file_custom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    yanit = update.message.text.lower().strip()
    context.user_data['custom'] = (yanit == 'y')
    await update.message.reply_text("Dosyanı gönder (.txt, .py)")
    return WAIT_FILE

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc: Document = update.message.document
    if not doc: return
    file = await doc.get_file()
    content = await file.download_as_bytearray()
    context.user_data['content'] = content.decode()

    if context.user_data.get('custom'):
        await update.message.reply_text("Başlık gir:")
        return FILE_ASK_TITLE
    else:
        return await paste_to_pastebin(update, context)

async def file_ask_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['title'] = update.message.text
    await update.message.reply_text("Dil formatı gir (.py .txt vb.):")
    return FILE_ASK_FORMAT

async def file_ask_format(update: Update, context: ContextTypes.DEFAULT_TYPE):
    format_map = {
        ".py": "python",
        ".txt": "text",
        ".html": "html5",
        ".js": "javascript"
    }
    uzanti = update.message.text.strip()
    context.user_data['format'] = format_map.get(uzanti, "text")
    await update.message.reply_text("Süre gir (10M, 1H, 1D, 1W, N):")
    return FILE_ASK_EXPIRE

async def file_ask_expire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['expire'] = update.message.text.upper().strip()
    return await paste_to_pastebin(update, context)