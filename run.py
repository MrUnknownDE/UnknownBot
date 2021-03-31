# pip install discord.py discord.py[voice] configparser sentry-sdk youtube_dl requests ffmpeg
import logging
import discord
import configparser
import sys
import sentry_sdk
from youtube_dl import YoutubeDL
from requests import get
sentry_sdk.init(
    "https://d012b451482f428ab43ef4cbb3766931@sentry.syslul.de/5",
    traces_sample_rate=1.0
)
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
    async def join(ctx, voice):
        channel = ctx.author.voice.channel

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect() 

    async def play(ctx, *, query):
        #Solves a problem I'll explain later
        FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        video, source = search(query)
        voice = get(bot.voice_clients, guild=ctx.guild)

        await join(ctx, voice)
        await ctx.send(f'Now playing {info['title']}.')

        voice.play(FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print('done', e))
        voice.is_playing()
    def search(query):
        with YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
            try: requests.get(arg)
            except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            else: info = ydl.extract_info(arg, download=False)
        return (info, info['formats'][0]['url'])

client = discord()
client.run(config["DISCORD"]["TOKEN"])
