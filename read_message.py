import asyncio
from template_folder.telegram_client import client, ensure_started

channel_username = "job4fresherss"  # Replace with the actual channel username

async def main():
    await ensure_started()
    async for msg in client.iter_messages(
        channel_username,
        limit=10
    ):
        print(msg.text)



if __name__ == "__main__":
    asyncio.run(main())