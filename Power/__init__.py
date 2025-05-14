from telethon import TelegramClient

from Config import config


# Initialize the Telegram client
api_id = config.ID # Replace with your actual API ID
api_hash = config.HASH  # Replace with your actual API Hash
bot_token = config.BOT_TOKEN  # Replace with your actual bot token
# Initialize the bot client
bot = TelegramClient(api_id, api_hash)

class client:
    def __init__(self):
        self.client = bot

    async def start(self):
        await self.client.start(bot_token=bot_token)
        print("Bot is running...")

    async def stop(self):
        await self.client.stop(bot_token=bot_token)
        print("Bot stopped.")


