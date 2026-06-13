from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

SESSION_NAME = os.getenv("SESSION_NAME", "session")
API_ID_STR = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

if API_ID_STR is None:
    raise RuntimeError("API_ID environment variable is not set")
try:
    API_ID = int(API_ID_STR)
except ValueError:
    raise RuntimeError("API_ID environment variable must be an integer")

if API_HASH is None:
    raise RuntimeError("API_HASH environment variable is not set")

# Shared TelegramClient instance for the application
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def ensure_started():
    """Start the client if it's not already running and return it."""
    # `start()` is safe to call multiple times; it will connect/sign-in as needed.
    await client.start() # type: ignore
    return client

__all__ = ["client", "ensure_started"]
