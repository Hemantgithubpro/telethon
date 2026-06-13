import asyncio
from telegram_client import client, ensure_started


async def main():
    await ensure_started()
    me = await client.get_me()
    # print(f"Logged in as {getattr(me, 'first_name', 'Unknown')} (id={getattr(me, 'id', 'Unknown')})")
    print(me.id) # type: ignore
    print(me.first_name)
    print(me.username)



if __name__ == "__main__":
    asyncio.run(main())
