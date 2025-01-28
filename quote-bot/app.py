import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def quote(ctx):
    # Fetch a quote from the API learn more on the api wiki page
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        await ctx.send(f'"{quote}" - {author}')
    else:
        await ctx.send("Sorry, I couldn't fetch a quote at the moment.")

bot.run('YOUR_BOT_TOKEN')
