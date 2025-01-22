import discord
import asyncio
import socket

TOKEN = 'YOUR_BOT_TOKEN'
SERVER_IP = '51.222.151.221'
SERVER_PORT = 2175
USER_ID = 123456789012345678  # Replace with the actual user ID of person you want to @

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def check_server_status():
    channel = None
    while True:
        try:
            # Attempt to "ping" the Minecraft server
            with socket.create_connection((SERVER_IP, SERVER_PORT), timeout=5):
                print("Server is up!")
        except (socket.timeout, ConnectionRefusedError, OSError):
            print("Server is down!")
            if channel is None:
                channel = discord.utils.get(client.get_all_channels(), name='general')
            user = await client.fetch_user(USER_ID)
            await channel.send(f"{user.mention}, the Minecraft server is down!")
        
# Wait for 10 minutes before checking again as a form of rate limiting :3
        await asyncio.sleep(600)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(check_server_status())

client.run(TOKEN)
