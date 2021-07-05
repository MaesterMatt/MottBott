#!/usr/bin/env python3
import discord
import os
import time
import random
import asyncio
import logging

#client = discord.Client()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
#welcome_channel = discord.Guild.system_channel.TextChannel
#print(welcome_channel)
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
      #msg = str("hau sux")
      hau = bool(random.getrandbits(1))
      
      await message.channel.send('sux' if hau else 'doesn\'t sux')

#Public Welcome
@client.event
async def on_member_join(member):
    print("Member Detected") #495284966876512258
    newUserDMMessage = "Welcome to Spirit, " + member.name + "!\nPlease check out the roles in #self-add-roles"
    print("Recognized that " + member.name + " joined")
    #member.add_roles("spies", )
    # role = discord.utils.get(member.guild.roles, name="spies")
    # await member.add_roles(role)
    role = discord.utils.get(member.guild.roles, id=727473839268691968)
    await member.add_roles(role)
    time.sleep(1)
    await member.guild.system_channel.send(newUserDMMessage)
    #await client.send_message(discord.Object(id='CHANNELID'), 'Welcome!')
    # print("Sent message to " + member.name)
    # print("Sent message about " + member.name + " to #CHANNEL")

client.run(os.getenv('TOKEN'))
