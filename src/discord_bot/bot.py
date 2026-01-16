import discord
import os
import requests
import json


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        res = requests.post(os.environ["N8N_WEBHOOK_URL"], data={"message": message.content})
        await message.reply(res.content.decode("utf-8"))
        


intents = discord.Intents.none()
intents.messages = True
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ["DISCORD_BOT_TOKEN"])
