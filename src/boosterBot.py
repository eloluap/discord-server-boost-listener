import discord
""" from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time """
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix = "!!")
tree = app_commands.CommandTree(client)


@tree.command(
    name="help",
    description="Lists the help page of this bot",
    guild=discord.Object(id=269566282494377984)
)
async def help_command(interaction):
    await interaction.response.send_message("""```
Help:
/help              Lists the help page of this bot
/ping (@...)       Pings yourself or someone if you mentioned him```""")
    
@tree.command(
    name="ping",
    description="Pings yourself or someone if you mentioned him",
    guild=discord.Object(id=269566282494377984)
)
async def ping_command(interaction, text: str):
    await interaction.response.send_message(f"text: {text}")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=269566282494377984))
    print(f"Bot is ready! Logged in as: {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "cookie":
        await message.channel.send(":cookie:")
    if message.content.upper().startswith("!!HELP"):
        await message.channel.send("""```
Help:
!!help              Shows this page
!!ping (@...)       Pings yourself or someone if you mentioned him```""")
# !!clear (HowMany)   Clears the last ... chat messages
    if message.content.upper().startswith("!!PING"):
        if len(message.content) > 6: # change if prefix length changes
            split = message.content.split(" ")
            await message.channel.send("{} Pong!".format(split[1]))
        else:
            userID = message.author.id
            await message.channel.send("<@{}> Pong!".format(userID))
    """ if message.content.upper().startswith("!CLEAR"):
        if "Admin" in [role.name for role in message.author.roles]:
            if len(message.content) > 6:
                split = message.content.split(" ")
                number = split[1]
                mgs = [] #Empty list to put all the messages in the
                number = int(number) #Converting the amount of messages to delete to an integer
                number += 1
                async for x in bot.logs_from(message.channel, limit = number):
                    mgs.append(x)
                await bot.delete_messages(mgs)
        else:
            await bot.send_message(message.channel, "Du hast nicht die nötigen Berechtigungen!") """

client.run("")