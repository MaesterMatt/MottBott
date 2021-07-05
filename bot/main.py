#!/usr/bin/env python3
import discord
import os
import time
import random
import asyncio
import logging
from welcome import *

#client = discord.Client()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

juwi_last = time.time()-60
@client.event
async def on_message(message):      
    if message.author == client.user:
        return

    #darren nauseous react
    if 'darren' in message.content.lower():
        emoji = '\U0001F922'#'\N{2764}'
        emoji2 = '\U00002764'
        darren = random.randint(0, 10)
        if str(message.author) == "$hwayjung#9949":
          await message.add_reaction(emoji if darren == 0 else emoji2)
        else:
          await message.add_reaction(emoji2 if darren == 0 else emoji)

    #For Julia Nuts emoji reaction
    global juwi_last
    if str(message.author) == "juwi#8008" and (time.time()-juwi_last > 60):
        emoji = '\U0001F1F3'
        await message.add_reaction(emoji)
        emoji = '\U0001F1FA'
        await message.add_reaction(emoji)
        emoji = '\U0001F1F9'
        await message.add_reaction(emoji)
        emoji = '\U0001F1F8'
        await message.add_reaction(emoji)
        juwi_last = time.time()

    #Hau sux
    if 'hau' in message.content.lower():
      hau = bool(random.getrandbits(1))
      await message.channel.send('sux' if hau else 'doesn\'t sux')

    mylist = ["jc...........", "JCJCJCJCJCJCJCJC", ".................JC!", "down >:)", "Oh sorry I'm busy", "Run without me :(", "I'm out right now", "How about in like an hour?"]
    if 'jc' in message.content.lower():
      rand_quote = mylist[random.randint(0, len(mylist)-1)]
      await message.channel.send(rand_quote)

#Public Welcome
@client.event
async def on_member_join(member):
    #welcome(member)
    #welcome(member)
    marc_welcome = "https://media.discordapp.net/attachments/495284966876512258/829984477727424512/ezgif.com-video-to-gif-2.gif"
    mylist = ["**Welcome to Spirit!** We're excited to see you ", "**Welcome to Spirit** BINCH... Enjoy your stay ", "**SSSUUUUUUUHHHHHHHHHHHHH** "]
    rand_quote = mylist[random.randint(0, len(mylist)-1)]
    newUserDMMessage = rand_quote + member.name + "!\n"
    self_add_roles = client.get_channel(717216767222480896)
    print(self_add_roles.name)
    newUserDMMessage2 = 'Please check out the roles in {0.mention}'.format(self_add_roles)
    
    print("Recognized that " + member.name + " joined")
  
    role = discord.utils.get(member.guild.roles, id=727473839268691968)
    await member.add_roles(role)
    time.sleep(1)
    await member.guild.system_channel.send(newUserDMMessage)
    await member.guild.system_channel.send(file=discord.File('marc.gif'))
    await member.guild.system_channel.send(newUserDMMessage2)


client.run(os.getenv('TOKEN'))
