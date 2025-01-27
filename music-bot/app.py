import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel.")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I am not in a voice channel.")

@bot.command()
async def play(ctx, url):
    voice_client = ctx.voice_client
    if not voice_client:
        await ctx.send("I need to be in a voice channel to play music.")
        return
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'type': 'audio/ffmpeg',
            'options': '-vn',
        }],
        'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    }
  
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(url))
bot.run('YOUR_BOT_TOKEN')
