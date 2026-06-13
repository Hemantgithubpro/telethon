from sync_client import client

# --- START CODING BELOW ---
# Everything is synchronous. You don't need `async def` or `await` anywhere!

# 1. Get your own user info
me = client.get_me()
print("Logged in as:", getattr(me, "first_name", "Unknown"))

# 2. Iterate messages synchronously
print("\nRecent messages from 'me' (Saved Messages):")
for msg in client.iter_messages("me", limit=3):
    print("-", msg.text)

# Just write client.<method>() normally!
