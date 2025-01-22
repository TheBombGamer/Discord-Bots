import discord
from discord.ext import commands
import json
import os

TOKEN = 'YOUR_BOT_TOKEN'
INVITE_FILE = 'invites.json'

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

def load_invites():
    if os.path.exists(INVITE_FILE):
        with open(INVITE_FILE, 'r') as f:
            return json.load(f)
    return {}
def save_invites(invites):
    with open(INVITE_FILE, 'w') as f:
        json.dump(invites, f)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')
@bot.event
async def on_member_join(member):
    invites = load_invites()
    guild = member.guild
    current_invites = await guild.invites()
    for invite in current_invites:
        if invite.uses > invites.get(str(invite.code), 0):
            inviter = invite.inviter
            await member.send(f'Welcome to the server, {member.name}! You were invited by {inviter.name}.')
            invites[str(invite.code)] = invite.uses 
            break
    save_invites(invites)
@bot.command()
async def invites(ctx):
    invites = load_invites()
    invite_list = "\n".join([f"Invite Code: {code}, Uses: {uses}" for code, uses in invites.items()])
    await ctx.send(f"Current invites:\n{invite_list}")

bot.run(TOKEN)