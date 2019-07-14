import discord
import asyncio
import configparser

client = discord.Client()

config = configparser.ConfigParser()
config.read("config.ini")

ownerid = (config['DISCORD']['owner'])
game = discord.Game(config['DISCORD']['game'])

##Variablen##
minutes = 0
hours = 0
days = 0

players = {}

@client.event
async def on_ready():
    print ('')
    print ('UnknownBot ist gestartet')
    print ('Verion: {0}'.format(config['VERSION']['version']))
    print ('')
    print ('?help - Für mehr Informationen')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('?help'):
        await  message.channel.send(":beginner: UnknownBot :beginner: \n\n __Verfügbare Commands__ \n\n:arrow_forward: ?help\n\n:arrow_forward: ?info \n\n:arrow_forward: ?join / ?leave\n\n")

    if message.content.startswith("?setgame") and message.author.id == ownerid:
        game = message.content[9:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Der Game-Status wurde auf `{0}` geändert.".format(game))

    if message.content.startswith("?uptime"):
        await  message.channel.send("Ich bin schon **{0} Tag(e) {1} Stunde(n) {2} Minute(n)** im Internet unterwegs".format(days, hours, minutes))

    if message.content.startswith("?info"):
        server = client.guilds
        embed = discord.Embed(title="Support-Discord: mrunknownde.de", colour=discord.Colour(0x8800ff),
                              url="https://gidf.de", description="\n\n\nIrgendwelche Informationen")
        embed.set_thumbnail(url="https://i.syslul.de/0b6e2/5d2b420c8fd39.jpg/raw")
        embed.set_author(name="UnknownBot Informationen", url="https://gidf.de",
                         icon_url="https://i.syslul.de/0b6e2/5d2b420c8fd39.jpg/raw")
        embed.set_footer(text="{0}".format(config['VERSION']['version']), icon_url="https://slides.steveliedtke.de/git2/images/Git-Icon-small.png")
        ### MEHR DOCS LESEN !!!!
        embed.add_field(name="Benutzer", value="-1 (aktuell in Arbeit)", inline=True)
        ### Datenschutz ist aktuell nicht geben :D
        embed.add_field(name="Servers", value="{0}".format(server), inline=True)
        embed.add_field(name="Letztes Update", value="{0}".format(config['VERSION']['last_change']), inline=True)
        embed.add_field(name="Onlinezeit", value="{0} Tag(e) {1} Stunde(n) {2} Minute(n)".format(days, hours, minutes), inline=True)
        ### Finde gerade nix gute um es umzusetzten :D
        embed.add_field(name="Discord.py", value="1.2.3v (aktuell in Arbeit)", inline=True)

        await message.channel.send(embed=embed)

    if message.content.startswith("?userinfo"):
        try:
            user = client.author
            usercreateat = str(user.created_at).split(".", 1)[0]
            userjoinat = str(user.joined_at).split(".", 1)[0]
            userstatus = user.game
            usericon = user.icon_url

            userembed = discord.Embed(colour=discord.Colour(0x8800ff))
            userembed.set_author(name="{0} #{1} Account Informationen".format(user.name, user.discriminator),
                             icon_url="https://i.syslul.de/0b6e2/5d2b420c8fd39.jpg/raw")
            userembed.set_footer(text="{0}".format(config['VERSION']['version']),
                             icon_url="https://slides.steveliedtke.de/git2/images/Git-Icon-small.png")
            userembed.add_field(name="Account Erstellt", value="{0}".format(usercreateat), inline=True)
            userembed.add_field(name="Server beigetreten", value="{0}".format(userjoinat), inline=False)
            userembed.add_field(name="Status", value="{0}".format(userstatus), inline=False)

            await  message.channel.send("{0}".format(usericon))
            await  message.channel.send(embed=userembed)

        except IndexError as error:
            await message.channel.send("Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        except Exception as error:
            await message.channel.send("Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        finally:
            pass
    if message.content.startswith("?server"):
        try:
            servers = message.server
            serverrcreateat = str(servers.created_at).split(".", 1)[0]
            serverowner = servers.owner
            servericon = servers.icon
            serverid = servers.id

            userembed = discord.Embed(colour=discord.Colour(0x8800ff))
            userembed.set_author(name="{0} - Informationen".format(servers.name), icon_url="https://cdn.discordapp.com/icons/{0}/{1}.jpg".format(serverid, servericon))
            userembed.set_footer(text="{0}".format(config['VERSION']['version']), icon_url="https://slides.steveliedtke.de/git2/images/Git-Icon-small.png")
            userembed.set_thumbnail(url="https://cdn.discordapp.com/icons/{0}/{1}.jpg".format(serverid, servericon))
            userembed.add_field(name="Server Erstellt", value="{0}".format(serverrcreateat), inline=True)
            userembed.add_field(name="Server Owner", value="{0}".format(serverowner), inline=False)
            userembed.add_field(name="Mitglieder", value="-Buggy-")

            await  message.channel.send(embed=userembed)

        except IndexError as error:
            await  message.channel.send("Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        except Exception as error:
            await  message.channel.send("Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        finally:
            pass





### Music Commands ##

    if message.content.startswith("?join"):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await  message.channel.send("Du bist nicht mit ein Voice-Channel verbunden.")
        except Exception as error:
            await  message.channel.send("Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        finally:
            pass

    if message.content.startswith("?leave"):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await  message.channel.send("Ich bin mit keinem Voice-Channel verbunden.")
        except Exception as error:
            await  message.channel.send("Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        finally:
            pass

## ENDE ##

## Player ##

    if message.content.startswith("?play"):
        try:
            link = message.content[6:]
            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(link, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    await  message.channel.send("__Wird jetzt ausgeführt__\n\n :arrow_forward: {0}".format(link))
                    player.start()
                except Exception as error2:
                    await  message.channel.send("Error \n\n ```{erro}```".format(erro=error2))
                finally:
                    pass
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player(link, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    player.start()
                except Exception as error2:
                    await  message.channel.send("Error \n\n ```{erro}```".format(erro=error2))
                finally:
                    pass
        except Exception as error2:
            await  message.channel.send("Error \n\n ```{erro}```".format(erro=error2))
        finally:
            pass

    if message.content.startswith("?pause"):
        try:
            players[message.server.id].pause()
        except Exception as error3:
            await  message.channel.send("Error \n\n ```{erro}```".format(erro=error3))
        finally:
            await  message.channel.send("**Player paussiert.**")

    if message.content.startswith("?resume"):
        try:
            players[message.server.id].resume()
        except Exception as error4:
            await  message.channel.send("Error \n\n ```{erro}```".format(erro=error4))
        finally:
            await  message.channel.send("**Player wird fortgesetzt.**")

    if message.content.startswith("?stop"):
        try:
            voice_client = client.voice_client_in(message.server)
            players[message.server.id].stop()
            await voice_client.disconnect()
        except Exception as error4:
            await  message.channel.send("Error \n\n ```{erro}```".format(erro=error4))
        finally:
            await  message.channel.send("**Player wurde gestoppt.**")


### Python Test CMDs
    if message.content.startswith("?author"):
        await message.channel.send("{0}".format(client.abc.user.name))






async def uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hours
    hours = 0
    global days
    days = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
            if hours == 24:
                minutes = 0
                hours = 0
                days += 1


client.loop.create_task(uptime())
client.run(config['DISCORD']['bot-token'])
