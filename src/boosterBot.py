import os
from dotenv import load_dotenv
import disnake
from disnake.ext import commands

load_dotenv()

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.InteractionBot(intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as: {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_member_update(before, after):
    if len(before.roles) is not len(after.roles):
        rolename = os.getenv("WATCH_ROLE_NAME")
        logChannelID = int(os.getenv("LOG_CHANNEL_ID"))
        logChannel = bot.get_channel(logChannelID)
        reactionChannelID = int(os.getenv("REACTION_CHANNEL_ID"))
        reactionMessageID = int(os.getenv("REACTION_MESSAGE_ID"))
        reactionMessage = await bot.get_channel(reactionChannelID).fetch_message(reactionMessageID)
        if (rolename in str(after.roles)) and not (rolename in str(before.roles)):
            print(f"User {after.name} gained role {rolename}")
            await logChannel.send(f"<@{after.id}> hat angefangen den Server zu boosten.")
        if (rolename in str(before.roles)) and not (rolename in str(after.roles)):
            print(f"User {after.name} lost role {rolename}")
            await logChannel.send(f"<@{after.id}> hat aufgehört den Server zu boosten.")
            for reaction in reactionMessage.reactions:
                users = await reaction.users().flatten()
                if after in users:
                    await reaction.remove(after)

if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))