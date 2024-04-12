# discord-server-boost-listener
Discord Bot which listens for role changes to log who started or stopped boosting your Server and automatically removes a reaction on an reaction role message.

Requires a .env file with:
- BOT_TOKEN=\<Your Bot Token\>
- WATCH_ROLE_NAME=Server Booster
- LOG_CHANNEL_ID=\<Channel ID of the channel in which the Bot should do the logging\>
- REACTION_CHANNEL_ID=\<Channel ID of the channel in which the message with the reaction roles is\>
- REACTION_MESSAGE_ID=\<Message ID of the reaction role message\>