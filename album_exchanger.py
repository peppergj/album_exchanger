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

@tree.command(name="album", description="random-album!")
async def readfile(interaction: discord.Interaction):
    try:
        with open("albums.txt", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            choice = random.choice(lines)
        await interaction.response.send_message(choice)
    except FileNotFoundError:
        await interaction.response.send_message("File not found.")

@tree.command(name="draw-names", description="draw-names-randomly")
@app_commands.describe(names="Enter names separated by commas")
async def pair_names(interaction: discord.Interaction, names: str):
    name_list = [name.strip() for name in names.split(",") if name.strip()]
    if len(name_list) < 2:
        await interaction.response.send_message("Please provide at least 2 names for pairing.", ephemeral=True)
        return
    random.shuffle(name_list)
    pairs = []
    for i in range(0, len(name_list), 2):
        if i + 1 < len(name_list):
            pairs.append(f"{name_list[i]} and {name_list[i + 1]}")
        else:
            pairs.append(f"{name_list[i]} is lonely lol")
    await interaction.response.send_message("Here are the exchange pairs:\n" + "\n".join(pairs))

@client.event
async def on_ready():
    await tree.sync()
    print("Successfully Connected! 10% Off any album bought with Nitro!")

try:
    with open("token.txt", "r") as tokenfile: 
        token = tokenfile.readlines()[0]
    client.run(token)
except:
    print("Could not find token.txt, which must contain your discord bot token")
