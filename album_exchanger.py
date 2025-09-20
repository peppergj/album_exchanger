import discord
import random
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="test", description="test-album")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("https://open.spotify.com/album/6hPkbAV3ZXpGZBGUvL6jVM?si=NSetYITLRyCFkQ6BVLIkKA")

@tree.command(name="draw-names", description="draw-names-randomly")
async def world(interaction:discord.Interaction):
        with open("name_list.txt", "r") as f:
            content = f.read()
        await interaction.response.send_message(content)

@client.event
async def on_ready():
    await tree.sync()
    print("oh ok hi")

with open("token.txt", "r") as tokenfile: 
    token = tokenfile.readlines()[0]
client.run(token)
