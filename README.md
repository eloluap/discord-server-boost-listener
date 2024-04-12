# discord-server-boost-listener
Discord Bot which listens for role changes to log (in german) in a discord channel who started or stopped boosting your Server and automatically removes a reaction on a reaction roles message from someone who stopped boosting your server.

Requires a .env file with:
- BOT_TOKEN=\<Your Bot Token\>
- WATCH_ROLE_NAME=Server Booster
- LOG_CHANNEL_ID=\<Channel ID of the discord channel the bot should log in\>
- REACTION_CHANNEL_ID=\<Channel ID of the discord channel which contains the reaction roles message\>
- REACTION_MESSAGE_ID=\<Message ID of the reaction roles message\>