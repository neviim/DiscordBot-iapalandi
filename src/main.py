import discord
from discord.ext import commands
from discord import app_commands

DISCORD_TOKEN=''

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logado como {self.user}!')

    async def on_message(self, message):
        #print(f'Mensagem de {message.author}: {message.content}')
        if message.author == self.user:
            return
        
        if message.content.startswith('ola'):
            await message.channel.send(f'Oi {message.author}')

    # reagio a uma mensagem com um emojin
    async def on_reaction_add(self, reaction, use):
        await reaction.message.channel.send('Você reagio !!!, :heart_eyes: ameri ...')




# =================================
#
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(DISCORD_TOKEN)

