import telethon.sync  # This automatically patches Telethon to work synchronously
from .telegram_client import client

# Start the client synchronously as soon as this is imported.
# It will use the configuration (API ID, Hash, Session) from telegram_client.py
client.start()
