from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_TOKEN, API_ID, API_HASH, BOT_USERNAME
import logging

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Bot
app = Client(
    "VJ_File_Store",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)


@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    args = message.text.split(None, 1)
    if len(args) == 2 and args[1].startswith("watch_"):
        file_id = args[1].split("_", 1)[1]
        try:
            await client.send_cached_media(chat_id=message.chat.id, media=file_id)
        except Exception as e:
            await message.reply_text(f"❌ Failed to send file.\n\nError: `{e}`")
    else:
        await message.reply_text(
            "👋 Welcome to the Stream Bot!\n\n"
            "Send me any Telegram video or document, and I will give you a streaming link."
        )


@app.on_message(filters.private & (filters.video | filters.document))
async def media_handler(client, message: Message):
    media = message.video or message.document
    file_id = media.file_id
    file_name = media.file_name or "Telegram_File"

    stream_link = f"https://t.me/{BOT_USERNAME}?start=watch_{file_id}"

    await message.reply_text(
        f"📁 **File Name:** `{file_name}`\n\n"
        f"▶️ **Stream Link:** [Click to Stream]({stream_link})",
        disable_web_page_preview=True
    )


if __name__ == "__main__":
    logger.info("Bot is running...")
    app.run()
