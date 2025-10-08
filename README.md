PasteBin Telegram Bot

This bot allows you to share text and files to PasteBin directly from Telegram. It can only be used by the bot owner.

🚀 Features

• Text Sharing: Share text using the /paste command

• File Sharing: Share files using the /pastefile command

• Customization: Title, format, and expiration settings

• Security: Only the bot owner can use it

📦 Installation

1. Requirements

• Python 3.7+

• Telegram Bot Token

• PasteBin API Key

2. Required Packages

```bash
pip install -r requirements.txt
```

3. Configuration

Edit the config.json file:

```json
{
    "TELEGRAM_TOKEN": "YOUR_BOT_TOKEN_HERE",
    "PASTEBIN_API_KEY": "YOUR_PASTEBIN_API_KEY_HERE",
    "OWNER_ID": YOUR_TELEGRAMID_HERE
}
```

4. Starting the Bot

```bash
python main.py
```

🛠 Commands

/start

Starts the bot and shows a welcome message.

/help

Shows all commands and their usage.

/paste

Starts text sharing. Customization options:

• Title: Paste title

• Format: Programming language format (.py, .txt, .js, .html)

• Expiration: Paste expiration time (10M, 1H, 1D, 1W, N)

/pastefile

Starts file sharing. Supported formats:

• .txt - Text files

• .py - Python files

• .js - JavaScript files

• .html - HTML files

📁 Project Structure

```
pastebot/
├── config.json
├── main.py
├── requirements.txt
├── README.md
├── handlers/
│   ├── __init__.py
│   ├── start.py
│   ├── paste.py
│   └── pastefile.py
└── utils/
    ├── __init__.py
    └── pastebin.py
```

🔧 Development

Adding New Commands

• Create a new file in the handlers/ directory

• Import it in main.py

• Add the handler to the application

Adding Config Variables

• Add new variable to config.json

• Import it in relevant files

🌐 API References

• Telegram Bot API

• PasteBin API

⚠️ Security Notes

• The bot can only be used by the user specified in OWNER_ID

• Keep your API keys secure

• Do not share config file in public repositories

🐛 Troubleshooting

• If the bot doesn't work, check your token

• If you get PasteBin errors, check your API key

• If you get file upload errors, check the file size

📄 License

This project is for private use.

👨‍💻 Developer

Developed by Rayzer.

---

Note: Don't forget to fill out the config.json file before using the bot!