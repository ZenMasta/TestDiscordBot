import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

## CHANNEL_A_ID = 880432552404467733  # Trading-Floor
CHANNEL_A_ID = 1062230790026580028  #  Market News
CHANNEL_B_ID = 879427114338779136  # Stax-Chat

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.channel.id == CHANNEL_A_ID:
        channel_b = bot.get_channel(CHANNEL_B_ID)
        if channel_b:
            await channel_b.send(message.content)

    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')
