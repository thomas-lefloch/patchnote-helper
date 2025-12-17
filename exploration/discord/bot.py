import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if (message.author == self.user):
            return 

        await message.add_reaction("🤩")
        await message.reply("No.")


intents = discord.Intents.none()
intents.messages = True
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ["DISCORD_BOT_TOKEN"])