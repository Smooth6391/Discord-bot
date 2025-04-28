import discord
from discord.ext import commands

# Setup bot with correct intents
intents = discord.Intents.default()
intents.message_content = True  # Allow the bot to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

# Event that triggers when bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")  # This will show the 'Logged in as' message in the terminal
    # Optionally, send a welcome message to a channel
    channel = bot.get_channel(1329803541417562244)  # Replace YOUR_CHANNEL_ID with the actual channel ID
    await channel.send(f"Hey everyone! I'm {bot.user}, your Nether Portal Calculator bot! 🚀")

# Nether portal calculator command
@bot.command()
async def portal(ctx, x: float, y: float, z: float, dimension: str):
    dimension = dimension.lower()

    if dimension == "overworld":
        # Overworld -> Nether
        nether_x = x / 8
        nether_z = z / 8
        await ctx.send(f"🌌 Nether coordinates:\nX: {nether_x:.2f}\nY: {y:.2f}\nZ: {nether_z:.2f}")
    elif dimension == "nether":
        # Nether -> Overworld
        overworld_x = x * 8
        overworld_z = z * 8
        await ctx.send(f"🌎 Overworld coordinates:\nX: {overworld_x:.2f}\nY: {y:.2f}\nZ: {overworld_z:.2f}")
    else:
        await ctx.send("❗ Please specify the dimension correctly: `overworld` or `nether`.")

# About command
@bot.command()
async def about(ctx):
    await ctx.send(
        "**🌀 Nether Portal Calculator Bot**\n"
        "This bot helps you calculate coordinates between the Overworld and Nether in Minecraft!\n\n"
        "Use the `!portal` command to convert coordinates easily:\n"
        "`!portal <x> <y> <z> <overworld/nether>`\n\n"
        "Example:\n"
        "`!portal 800 64 1200 overworld`\n"
        "→ It tells you the Nether coordinates for your portal!"
    )

# Run the bot (replace with your real token)
bot.run('MTM1NjI3ODQ0OTY3MjgxODgxMA.Gr8fih.eha0Mo31j-0NFRcmgmfnh1l6Cb7SKLg-WvHb18')
