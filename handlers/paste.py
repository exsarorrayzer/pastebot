import json
from telegram.ext import ContextTypes
from telegram import Update
from handlers.pastebin import paste_to_pastebin

with open('config.json', 'r') as f:
    config = json.load(f)

OWNER_ID = config['OWNER_ID']

# Conversation states
ASK_CUSTOM, GET_CONTENT, ASK_TITLE, ASK_FORMAT, ASK_EXPIRE = range(5)

async def paste(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID: return
    await update.message.reply_text("Customization? (y/n)")
    return ASK_CUSTOM

async def ask_custom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    yanit = update.message.text.lower().strip()
    context.user_data['custom'] = (yanit == 'y')
    await update.message.reply_text("Send Text:")
    return GET_CONTENT

async def get_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['content'] = update.message.text
    if context.user_data.get('custom'):
        await update.message.reply_text("Enter Title:")
        return ASK_TITLE
    else:
        return await paste_to_pastebin(update, context)

async def ask_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['title'] = update.message.text
    await update.message.reply_text("Dil formatı gir (.py .txt vb.):")
    return ASK_FORMAT

async def ask_format(update: Update, context: ContextTypes.DEFAULT_TYPE):
    format_map = {
        ".py": "python",
        ".txt": "text",
        ".html": "html5",
        ".js": "javascript"
    }
    uzanti = update.message.text.strip()
    context.user_data['format'] = format_map.get(uzanti, "text")
    await update.message.reply_text("Enter Expire Duration (10M, 1H, 1D, 1W, N):")
    return ASK_EXPIRE

async def ask_expire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['expire'] = update.message.text.upper().strip()
    return await paste_to_pastebin(update, context)