from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest, DeleteMessagesRequest
from telethon.tl.types import InputPeerEmpty
import asyncio

api_id = int(input("🔐 Please enter your API ID: "))
api_hash = input("🔐 Please enter your API HASH: ")
phone = input("📱 Your phone number (with +1): ")

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone)
    print("✅ Login successful!")

    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            group = dialog
            print(f"🧹 Cleaning your messages in group: {group.name}")
            async for msg in client.iter_messages(group.id, from_user='me'):
                try:
                    await client.delete_messages(group.id, msg.id)
                    print(f"🗑 Message {msg.id} deleted")
                except Exception as e:
                    print(f"⚠️ Error deleting message {msg.id}: {e}")

    print("✅ Operation completed.")

with client:
    client.loop.run_until_complete(main())
