import discord
from discord.ext import commands

# Setup bot with correct intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# REMOVE the default help command
bot.remove_command('help')

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Nether Portal Calculator"))
    channel = bot.get_channel(1329803541417562244)  # Replace with your actual channel ID
    if channel:
        await channel.send(f"Hey everyone! I'm {bot.user}, your Nether Portal Calculator bot! 🚀")
    else:
        print("⚠️ Channel not found. Check your channel ID.")

# Command to calculate Nether/Overworld coordinates
@bot.command()
async def portal(ctx, x: float, y: float, z: float, dimension: str):
    dimension = dimension.lower()

    if dimension == "overworld":
        nether_x = x / 8
        nether_z = z / 8
        await ctx.send(f"🌌 Nether coordinates:\nX: {nether_x:.2f}\nY: {y:.2f}\nZ: {nether_z:.2f}")
    elif dimension == "nether":
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
        "**Usage:**\n"
        "`!portal <x> <y> <z> <overworld/nether>`\n\n"
        "**Example:**\n"
        "`!portal 800 64 1200 overworld`\n"
        "→ It tells you the Nether coordinates for your portal!"
    )

# Custom Help command
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="🛠 Help Menu",
        description="Here are the available commands:",
        color=discord.Color.green()
    )
    embed.add_field(
        name="!portal <x> <y> <z> <overworld/nether>",
        value="🔹 Converts coordinates between Overworld and Nether.\nExample: `!portal 800 64 1200 overworld`",
        inline=False
    )
    embed.add_field(
        name="!about",
        value="🔹 Shows information about the bot.",
        inline=False
    )
    await ctx.send(embed=embed)

# Start the bot
bot.run('')  # Replace with your token
