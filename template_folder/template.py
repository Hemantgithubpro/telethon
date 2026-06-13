from .sync_client import client

# --- START CODING BELOW ---
# Everything is synchronous. You don't need `async def` or `await` anywhere!

# 1. Get your own user info
me = client.get_me()
print("Logged in as:", getattr(me, "first_name", "Unknown"))

folder_name = "job4fresherss"
count = 3

# 2. Iterate messages synchronously
print("\nRecent messages from '" + folder_name + "':")
for msg in client.iter_messages(folder_name, limit=count):
    print("\n\n\n--------------------\n", msg.text)

# Just write client.<method>() normally!
