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

        res = requests.post(
            "http://n8n:5678/webhook-test/c06245b1-90a9-4c97-be54-9efff048b38f",
            # "http://n8n:5678/webhook/c06245b1-90a9-4c97-be54-9efff048b38f",
            data={"message": message.content},
        )
        data = json.loads(res.content)
        await message.reply(data["content"])


intents = discord.Intents.none()
intents.messages = True
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ["DISCORD_BOT_TOKEN"])
