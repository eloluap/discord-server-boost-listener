import os
from dotenv import load_dotenv
import disnake
from disnake.ext import commands

load_dotenv()

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!!"), intents=intents, test_guilds=[269566282494377984])


@bot.slash_command(description="Lists the help page of this bot")
async def help(inter):
    await inter.response.send_message("""```
/help               Lists the help page of this bot
/ping (@...)        Pings yourself or someone if you mentioned him```""") # TODO: Create Embedding later
    
@bot.slash_command(description="Pings yourself or someone if you mentioned him")
async def ping(inter, user: disnake.User = None):
    if user is None:
        await inter.response.send_message(f"<@{inter.user.id}> Pong!")
    else: 
        await inter.response.send_message(f"<@{user.id}> Pong!")


@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as: {bot.user} (ID: {bot.user.id})")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "cookie":
        await message.channel.send(":cookie:")
    

if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))