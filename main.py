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

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

juwi_last = time.time()-60
lauren_last = time.time()-60
@client.event
async def on_message(message):      
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        await message.channel.send('Hey Daddy ~')

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

    global lauren_last
    if str(message.author) == "Lauren#2084" and (time.time()-lauren_last > 60):
        emoji = '\U0001F1ED'
        await message.add_reaction(emoji)
        emoji = '\U0001F1E7'
        await message.add_reaction(emoji)
        emoji = '\U0001F1E9'
        await message.add_reaction(emoji)
        lauren_last = time.time()

    #Hau sux
    if 'hau' in message.content.lower():
      hau = bool(random.getrandbits(1))
      await message.channel.send('sux' if hau else 'doesn\'t sux')

    mylist = ["JCJCJCJCJCJCJCJC", ".................JC!", "down >:)", "Oh sorry I'm busy", "just go w/o me idk wtf is wrong with this game", "I'm out right now", "How about in like an hour?", "Im going to dentist ...", "I WNA NAP", "I’m at hospital", "IM GETTING THE BEE OUT STILL", "It's too late for JC now, imma go to zak", "LMAO WTF IS THIS SHIT im going out ....", "LOL", "gimme like 15 mins me finishign dinner", "omg it says we are unable to connect to maplelegends"]
    if 'jc' in message.content.lower():
      if 'no jc' in message.content.lower():
        await message.channel.send(file=discord.File('nojc.png'))
      else:
        rand_quote = mylist[random.randint(0, len(mylist)-1)]
        await message.channel.send(rand_quote)

    if 'jiaoceng' in message.content.lower():
      #bernie = "https://i.imgur.com/OAWkEbe.png"
      await message.channel.send(file=discord.File('Jiaoceng.png'))

    if 'eggjung' in message.content.lower():
      eggjungImageCount = len(os.listdir('eggjung/'))
      sujung = random.randint(0, eggjungImageCount-1)
      suwu = 'eggjung/eggjung' + str(sujung) + '.jpg'
      await message.channel.send(file=discord.File(suwu))

    if '?mystery' in message.content.lower():
      with open('icebreakers.txt') as fr: 
        lines = fr.readlines() 
        icebreaker = random.choice(lines) if lines else None 
        channel = await message.author.create_dm()
        await channel.send("Your Mystery question is: \n*" + icebreaker.strip("\n") + "*\n")

    #The unknown spirit messaged in the welcome channel
    if message.channel == client.get_channel(865854495760973834):
      ghost_role = discord.utils.get(message.author.guild.roles, id=868056296534999080)
      if message.author.top_role == ghost_role:
        intromsg = message.content
        if intromsg.find("Name") > 0 and intromsg.find("IGN") > 0 and intromsg.find("Birthday") > 0 and intromsg.find("Mystery") > 0:
          name = message.content[intromsg.find("Name")+5:intromsg.find("\n", intromsg.find("Name")+5)].strip(" \n")
          print("Name: " + name)
          ign = message.content[intromsg.find("IGN")+4:intromsg.find("\n", intromsg.find("IGN")+4)].strip(" \n")
          print("IGN: " + ign)

          if len(name) and len(ign) and len(name) + len(ign) < 29:
            nickname = name + " | " + ign
            await message.author.edit(nick=nickname)

            await message.author.remove_roles(ghost_role)
            general = client.get_channel(495284966876512258)
            spies_role = discord.utils.get(message.author.guild.roles, id=727473839268691968)
            await message.author.add_roles(spies_role)
            mylist = ["**Welcome to Spirit!** We're excited to see you ", "**Welcome to Spirit** BINCH... Enjoy your stay ", "**SSSUUUUUUUHHHHHHHHHHHHH** ", "SHEEEEEEEEEEEEEEEEEEEEEEEEEESH ", "Welcome to spirit! I'm ugly "]
            rand_quote = mylist[random.randint(0, len(mylist)-1)]
            self_add_roles = client.get_channel(717216767222480896)
            newUserDMMessage = rand_quote + "{0.mention}!\nPlease check out the roles in {1.mention}".format(message.author, self_add_roles)
          
            #newUserDMMessage2 = 'Please check out the roles in {1.mention}'.format()
            await general.send(file=discord.File('marc.gif'))
            await general.send(newUserDMMessage)
          else:
            errorDM = "Hi, please give us your name and IGN(In Game Name)\n*Must be fewer than 28 characters total*\n"
            await message.delete()
            channel = await message.author.create_dm()
            await channel.send(errorDM)
        else:
          errorDM = "Hi, it seems like you need to copy the following template exactly:\n"
          errorDM2 = "-------------------------\nName: \nIGN: \nBirthday: \nMystery:\n-------------------------"
          await message.delete()
          channel = await message.author.create_dm()
          await channel.send(errorDM)
          await channel.send(errorDM2)

#Public Welcome
@client.event
async def on_member_join(member):
    introduce_self = client.get_channel(865854495760973834)
    icebreaker = ""
    with open('icebreakers.txt') as fr: 
        lines = fr.readlines() 
        icebreaker = random.choice(lines) if lines else None 
    Text2Send = '**Hello and Welcome to Spirit!**\nBefore letting you into the bathhouse, please copy and fill out this template below and post it in {0.mention}\n'.format(introduce_self)
    copytext = "-------------------------\nName: \nIGN: \nBirthday: \nMystery:\n-------------------------\n"
    icebreaker_string = "*For the Mystery, please answer this question:\n*{0}*".format(icebreaker.strip("\n"))
    channel = await member.create_dm()
    await channel.send(Text2Send)
    await channel.send(copytext)
    await channel.send(icebreaker_string)
  
    role = discord.utils.get(member.guild.roles, id=868056296534999080)
    await member.add_roles(role)

client.run(os.getenv('TOKEN'))
