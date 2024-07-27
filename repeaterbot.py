import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


CHANNEL_A_ID = YOURCHANNELID  # Name of Channel A
CHANNEL_B_ID = YOURCHANNELID  # Name of Channel B

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    print(f'Message from {message.author} in channel {message.channel.id}: {message.content}')
    if message.channel.id == CHANNEL_A_ID:
        channel_b = bot.get_channel(CHANNEL_B_ID)
        if channel_b:
            await channel_b.send(message.content)
            print(f'Message sent to Channel B: {message.content}')
        else:
            print('Channel B not found')

    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')
