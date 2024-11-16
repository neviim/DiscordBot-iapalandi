import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class Client(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)

    async def on_ready(self):
        print(f'Logado como {self.user}!')

        try:
            guild = discord.Object(id=1305001407472078869)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands para guild {guild.id}')

        except Exception as e:
            print(f'Error syscing commands {e}')

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
# intents = discord.Intents.default()
# intents.message_content = True
# client = Client(command_prefix="!", intents=intents)

client  = Client()
GUILD_ID = discord.Object(id=1305001407472078869)

# comando oieee
@client.tree.command(name='oieee', description="Oieee, tudo bem?", guild=GUILD_ID)
async def sayoieee(interaction: discord.Interaction):
    await interaction.response.send_message("Oiee, como esta?")

# comando printer
@client.tree.command(name='escreva', description="Eu vou escrever tudo o que você me der!", guild=GUILD_ID)
async def escreva(interaction: discord.Interaction, escreva: str):
    await interaction.response.send_message(escreva)

client.run(TOKEN)

