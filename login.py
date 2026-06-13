from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

# Read and validate environment variables
SESSION_NAME = os.getenv("SESSION_NAME") or "session"
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

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    me = await client.get_me()

    print(f"Logged in as {getattr(me, 'first_name', 'Unknown')}")
    print(f"User ID: {getattr(me, 'id', 'Unknown')}")

with client:
    client.loop.run_until_complete(main())