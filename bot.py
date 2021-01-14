import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=';')


@bot.event
async def on_ready():
    print(">>Bot is online<<")


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')


bot.run('Nzk5MTg2MjgyNDgyNzYxNzc5.X__6OQ.tYjzSsupwn2AtFU-xCjfhhOfXYE')
