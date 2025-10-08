import json

with open('config.json', 'r') as f:
    config = json.load(f)

OWNER_ID = config['OWNER_ID']

async def start(update, context):
    if update.effective_user.id != OWNER_ID: return
    await update.message.reply_text("🌟 Pastebin Uploader Bot\n/help for details.")

async def help_command(update, context):
    if update.effective_user.id != OWNER_ID: return
    await update.message.reply_text("""
🌟 Commands:
/paste → uploads <text> To pastebin
/pastefile → uploads <file> To pastebin
""")