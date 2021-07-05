#welcome script

def welcome(member)
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