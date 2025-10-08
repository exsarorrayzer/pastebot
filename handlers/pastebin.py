import json
import requests
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

# Config yükleme
with open('config.json', 'r') as f:
    config = json.load(f)

PASTEBIN_API_KEY = config['PASTEBIN_API_KEY']

async def paste_to_pastebin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = {
        "api_dev_key": PASTEBIN_API_KEY,
        "api_option": "paste",
        "api_paste_code": context.user_data['content'],
        "api_paste_private": 1,
        "api_paste_expire_date": context.user_data.get('expire', 'N'),
        "api_paste_name": context.user_data.get('title', ''),
        "api_paste_format": context.user_data.get('format', 'text')
    }
    try:
        r = requests.post("https://pastebin.com/api/api_post.php", data=data)
        await update.message.reply_text(f"✅ Paylaşıldı:\n{r.text}")
    except Exception as e:
        await update.message.reply_text(f"❌ Hata:\n{e}")
    return ConversationHandler.END