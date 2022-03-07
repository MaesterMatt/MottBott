#!/usr/bin/env python3
import discord
import os
import time
import random
import asyncio
import logging
import csv
from datetime import datetime, timedelta

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
    msg_lower = message.content.lower()
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        await message.channel.send('Hey Daddy ~')

    #darren nauseous react
    if 'darren' in msg_lower:
        emoji = '\U0001F922'#'\N{2764}'
        emoji2 = '\U00002764'
        darren = random.randint(0, 10)
        if message.author.id == 497640446328307713:
          await message.add_reaction(emoji if darren == 0 else emoji2)
        else:
          await message.add_reaction(emoji2 if darren == 0 else emoji)

    if 'fak u bot' in msg_lower and message.author.id == 134019734193700864:
      mylist = ["#botlivesmatter", "How dare you talk to BSFW like that!", "Stop it hoolian", "Julian is mean to bots confirmed", "fak u hooman", "meanie :(", "Issok BSFW I luv u", "bot luv", "botist", "It's 2021 no bot shaming", "You're ugly", "No booli", "stop being mean to BSFW", "fak u hoolian", "give bsfw a break, it's trying its best", "go back to BL5"]
      rand_quote = mylist[random.randint(0, len(mylist)-1)]
      await message.channel.send(rand_quote)

    #For Julia Nuts emoji reaction
    global juwi_last
    if message.author.id == 108011901136519168 and (time.time()-juwi_last > 120):
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
    if message.author == 575585308251521035 and (time.time()-lauren_last > 120):
        emoji = '\U0001F1ED'
        await message.add_reaction(emoji)
        emoji = '\U0001F1E7'
        await message.add_reaction(emoji)
        emoji = '\U0001F1E9'
        await message.add_reaction(emoji)
        lauren_last = time.time()

    #Hau sux
    # if 'hau' in msg_lower:
    #   hau = bool(random.getrandbits(1))
    #   await message.channel.send('sux' if hau else 'doesn\'t sux')

    mylist = ["JCJCJCJCJCJCJCJC", ".................JC!", "down >:)", "Oh sorry I'm busy", "just go w/o me idk wtf is wrong with this game", "I'm out right now", "How about in like an hour?", "Im going to dentist ...", "I WNA NAP", "I’m at hospital", "IM GETTING THE BEE OUT STILL", "It's too late for JC now, imma go to zak", "LMAO WTF IS THIS SHIT im going out ....", "LOL", "gimme like 15 mins me finishign dinner", "omg it says we are unable to connect to maplelegends"]
    if 'jc' in msg_lower:
      if 'no jc' in msg_lower:
        await message.channel.send(file=discord.File('nojc.png'))
      else:
        rand_quote = mylist[random.randint(0, len(mylist)-1)]
        await message.channel.send(rand_quote)

    #jiaoceng image
    if 'jiaoceng' in msg_lower:
      #bernie = "https://i.imgur.com/OAWkEbe.png"
      await message.channel.send(file=discord.File('Jiaoceng.png'))

    #eggjung
    if 'eggjung' in msg_lower:
      print(len(msg_lower[7:]))
      suwu = 'eggjung.gif'
      if len(msg_lower > 7):
        suwu = 'eggjung/eggjung' + str(msg_lower[7:]).strip(" \n") + '.jpg'
      else:
        eggjungImageCount = len(os.listdir('eggjung/'))
        sujung = random.randint(0, eggjungImageCount)
        if sujung < eggjungImageCount:
          suwu = 'eggjung/eggjung' + str(sujung) + '.jpg'
      await message.channel.send(file=discord.File(suwu))

    #mystery question
    if '?mystery' in msg_lower:
      with open('icebreakers.txt') as fr: 
        lines = fr.readlines() 
        icebreaker = random.choice(lines) if lines else None 
        channel = await message.author.create_dm()
        await channel.send("Your Mystery question is: \n*" + icebreaker.strip("\n") + "*\n")

    if '?birthdays' in msg_lower:
      MonthBdays = []
      Month = datetime.strftime(datetime.now(),'%-m')
      Day = datetime.strftime(datetime.now(), '%-d')
      with open('birthdays.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
          if Month == row[1][0:row[1].find('/')] and int(Day) <= int(row[1][row[1].find('/')+1:]):
            MonthBdays.append(row[0] + ' on ' + row[1])
        if len(MonthBdays) > 0:
          listToStr = '\n'.join([str(person) for person in MonthBdays])
          send = '**Birthdays left this month:** \n' + listToStr
          await message.channel.send(send)
        else:
          send = 'No other birthdays this month :('
          await message.channel.send(send)
          #print(f'\tIGN: {row[0]}\'s birthday is on {row[1]}, timezone is UTC + {row[2]}. Their Discord ID is: {row[3]}, and the quote assigned is: {row[4]}')

    if '?birthdaytest' in msg_lower:
      message_channel = client.get_channel(860799304134426625)
      Hour = datetime.strftime(datetime.now(),'%-H')
      Month = datetime.strftime(datetime.now(),'%-m')
      Day = datetime.strftime(datetime.now(), '%-d')
      Today = datetime.strftime(datetime.now(),'%-m/%-d')
      Tomorrow = datetime.strftime(datetime.now() + timedelta(days=1), '%-m/%-d')
      with open('birthdays.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
          if (int(row[2]) + int(Hour) == 24 and Tomorrow == row[1]) or (int(row[2]) + int(Hour) == 0 and Today == row[1]):
            bdaymsg = row[5]
            #Has a mention
            if bdaymsg.find('mention') and len(row[4]) > 0:
              bdayperson = client.get_user(int(row[4]))
              bdaymsg = bdaymsg.format(bdayperson)
            await message_channel.send(bdaymsg)

    #The unknown spirit messaged in the welcome channel
    if message.channel == client.get_channel(865854495760973834):
      ghost_role = discord.utils.get(message.author.guild.roles, id=868056296534999080)
      if message.author.top_role == ghost_role:
        intromsg = message.content
        if intromsg.find("Name") > 0 and intromsg.find("IGN") > 0:
          name = message.content[intromsg.find("Name")+5:intromsg.find("\n", intromsg.find("Name")+5)].strip(" \n")
          ign = message.content[intromsg.find("IGN")+4:intromsg.find("\n", intromsg.find("IGN")+4)].strip(" \n")

          if name.find(" ") > 0:
            name = name[:name.find(" ")]
          if name.find("/") > 0:
            name = name[:name.find("/")]
          if ign.find(" ") > 0:
            ign = ign[:ign.find(" ")]
          if ign.find("/") > 0:
            ign = ign[:ign.find("/")]
          if ign.find(",") > 0:
            ign = ign[:ign.find(",")]
          print("Name: " + name)
          print("IGN: " + ign)

 #         if len(name) and len(ign) and len(name) + len(ign) < 29:
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

#General: 495284966876512258
@client.event
async def time_check():
  await client.wait_until_ready()
  message_channel = client.get_channel(495284966876512258)
  send_time = datetime.strftime(datetime.now(),'%-m/%d-%H:%M')
  while True:
    Hour=datetime.strftime(datetime.now(),'%-H')
    Minute=datetime.strftime(datetime.now(),'%M')
    Month = datetime.strftime(datetime.now(),'%-m')
    Today = datetime.strftime(datetime.now(), '%-m/%-d')
    Tomorrow = datetime.strftime(datetime.now() + timedelta(days=1), '%-m/%-d')
    #print(now[:2]) - Hour
    if Minute == '00': #check csv
      with open('birthdays.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
          if (int(row[2]) + int(Hour) == 24 and Tomorrow == row[1]) or (int(row[2]) + int(Hour) == 0 and Today == row[1]):
            bdaymsg = row[5]
            #Has a mention
            if bdaymsg.find('mention') and len(row[4]) > 0:
              bdayperson = client.get_user(int(row[4]))
              bdaymsg = bdaymsg.format(bdayperson)
            await message_channel.send(bdaymsg)
      time = 3500
    else:
      time = 50
    await asyncio.sleep(time)

client.loop.create_task(time_check())

client.run(os.getenv('TOKEN'))
