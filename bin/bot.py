import discord
import asyncio
import configparser

client = discord.Client()

config = configparser.ConfigParser()
config.read("config.ini")

ownerid = (config['DISCORD']['owner'])

##Variablen##
minutes = 0
hours = 0
days = 0

players = {}

@client.event
async def on_ready():
    print ('')
    print ('UnknownBot ist gestartet')
    print ('')
    print ('?help - Für mehr Informationen')
    await client.change_presence(game=discord.Game(name="booting ..."))

@client.event
async def on_message(message):
    if message.content.lower().startswith("?help"):
        await  client.send_message(message.channel, ":beginner: UnknownBot :beginner: \n\n __Verfügbare Commands__ \n\n:arrow_forward: ?help\n\n:arrow_forward: ?info \n\n:arrow_forward: ?join / ?leave\n\n")

    if message.content.lower().startswith("?setgame") and message.author.id == ownerid:
        game = message.content[9:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Der Game-Status wurde auf `{0}` geändert.".format(game))

    if message.content.lower().startswith("?uptime"):
        await client.send_message(message.channel,"Ich bin schon **{0} Tag(e) {1} Stunde(n) {2} Minute(n)** im Internet unterwegs".format(days, hours, minutes))

    if message.content.lower().startswith("?info"):
        server = client.servers
        embed = discord.Embed(title="Support-Discord: mrunknownde.de", colour=discord.Colour(0x8800ff),
                              url="https://mrunknownde.de", description="\n\n\nIrgendwelche Informationen")
        embed.set_thumbnail(url="https://dl.mrunknownde.de/4KbNR")
        embed.set_author(name="UnknownBot Informationen", url="https://mrunknownde.de",
                         icon_url="https://dl.mrunknownde.de/4KbNR")
        embed.set_footer(text="{0}".format(config['VERSION']['version']), icon_url="https://slides.steveliedtke.de/git2/images/Git-Icon-small.png")
        embed.add_field(name="Benutzer", value="{0}", inline=True)
        embed.add_field(name="Servers", value="{0}".format(server), inline=True)
        embed.add_field(name="Letztes Update", value="12.04.2018 - 22:55 Uhr", inline=True)
        embed.add_field(name="Onlinezeit", value="{0} Tag(e) {1} Stunde(n) {2} Minute(n)".format(days, hours, minutes), inline=True)
        embed.add_field(name="Discord.py", value="{0}", inline=True)

        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith("?userinfo"):
        try:
            user = message.author
            usercreateat = str(user.created_at).split(".", 1)[0]
            userjoinat = str(user.joined_at).split(".", 1)[0]
            userstatus = user.game
            usericon = user.icon_url

            userembed = discord.Embed(colour=discord.Colour(0x8800ff))
            userembed.set_author(name="{0} #{1} Account Informationen".format(user.name, user.discriminator),
                             icon_url="https://dl.mrunknownde.de/Bilder/Rem_re_zero_render_by_ozkberg-daf287u.png")
            userembed.set_footer(text="{0}".format(config['VERSION']['version']),
                             icon_url="https://slides.steveliedtke.de/git2/images/Git-Icon-small.png")
            userembed.add_field(name="Account Erstellt", value="{0}".format(usercreateat), inline=True)
            userembed.add_field(name="Server beigetreten", value="{0}".format(userjoinat), inline=False)
            userembed.add_field(name="Status", value="{0}".format(userstatus), inline=False)

            await client.send_message(message.channel, "{0}".format(usericon))
            await client.send_message(message.channel, embed=userembed)

        except IndexError as error:
            await client.send_message(message.channel, "Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        except Exception as error:
            await client.send_message(message.channel, "Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        finally:
            pass
    if message.content.lower().startswith("?server"):
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

            await client.send_message(message.channel, embed=userembed)

        except IndexError as error:
            await client.send_message(message.channel, "Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        except Exception as error:
            await client.send_message(message.channel, "Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        finally:
            pass





### Music Commands ##

    if message.content.lower().startswith("?join"):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Du bist nicht mit ein Voice-Channel verbunden.")
        except Exception as error:
            await client.send_message(message.channel, "Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        finally:
            pass

    if message.content.lower().startswith("?leave"):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "Ich bin mit keinem Voice-Channel verbunden.")
        except Exception as error:
            await client.send_message(message.channel, "Fehler beim Verarbeiten \n\n ```{error}```\n Diesen Fehler dem Support melden.".format(error=error))
        finally:
            pass

## ENDE ##

## Player ##

    if message.content.lower().startswith("?play"):
        try:
            link = message.content[6:]
            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(link, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    await client.send_message(message.channel, "__Wird jetzt ausgeführt__\n\n :arrow_forward: {0}".format(link))
                    player.start()
                except Exception as error2:
                    await client.send_message(message.channel, "Error \n\n ```{erro}```".format(erro=error2))
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
                    await client.send_message(message.channel, "Error \n\n ```{erro}```".format(erro=error2))
                finally:
                    pass
        except Exception as error2:
            await client.send_message(message.channel, "Error \n\n ```{erro}```".format(erro=error2))
        finally:
            pass

    if message.content.lower().startswith("?pause"):
        try:
            players[message.server.id].pause()
        except Exception as error3:
            await client.send_message(message.channel, "Error \n\n ```{erro}```".format(erro=error3))
        finally:
            await client.send_message(message.channel, "**Player paussiert.**")

    if message.content.lower().startswith("?resume"):
        try:
            players[message.server.id].resume()
        except Exception as error4:
            await client.send_message(message.channel, "Error \n\n ```{erro}```".format(erro=error4))
        finally:
            await client.send_message(message.channel, "**Player wird fortgesetzt.**")

    if message.content.lower().startswith("?stop"):
        try:
            voice_client = client.voice_client_in(message.server)
            players[message.server.id].stop()
            await voice_client.disconnect()
        except Exception as error4:
            await client.send_message(message.channel, "Error \n\n ```{erro}```".format(erro=error4))
        finally:
            await client.send_message(message.channel, "**Player wurde gestoppt.**")






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
