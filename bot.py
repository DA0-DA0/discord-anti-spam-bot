import disnake
import sys
from datetime import timedelta
from config import *

client = disnake.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    sys.stdout.flush()

@client.event
async def on_message(message):
    notify_channel = await client.fetch_channel(NOTIFY_CHANNEL_ID)

    content = message.content.lower()
    if "axvdex.org" in content or ("astrovault" in content and "airdrop" in content):
        print(f"Deleting message from {message.author.display_name}:")
        print("---------------------------------------")
        print(message.content)
        print("---------------------------------------")

        try:
            # delete message
            await message.delete()

            # time out user
            await message.author.timeout(duration=timedelta(days=27), reason="spam")

            # notify of timeout
            await notify_channel.send(f"{message.author.mention} timed out for spam")
        except Exception as e:
            print(f"Error: {e}")
            await notify_channel.send(f"Error deleting spam message or timing out user ({message.author.mention}):\n```{e}```")

client.run(TOKEN)
