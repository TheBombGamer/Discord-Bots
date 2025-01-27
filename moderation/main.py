import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  
# Enable the members intent in the discord dev app so you can use this

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} for: {reason}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick members.")

bot.run('YOUR_BOT_TOKEN')
