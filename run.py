import logging
import discord
import configparser
import sys
config = configparser.ConfigParser()
config.read('bin/config.ini')



# //Logging - Müll
class discord(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('[LOG] Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('{0}help'.format(config['DISCORD']['PREFIX'])):
            await message.channel.send('MOIN MEISTA')

client = discord()
client.run(config["DISCORD"]["TOKEN"])
