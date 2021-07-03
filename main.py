#!/usr/bin/env python3
import discord
import os
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

juwi_last = time.time()-60
"$TOKEN"
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #darren nauseous react
    if 'darren' in message.content.lower() or message.author == "misterjuicy#8092":
        emoji = '\U0001F922'#'\N{NAUSEATED FACE}'
        await message.add_reaction(emoji)

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


client.run(os.getenv('TOKEN'))
