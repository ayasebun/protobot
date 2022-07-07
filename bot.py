#!/usr/bin/python3.10

import discord
import asyncio
import configparser
import re
import string
import random
from random import randint
from quotes import *

config = configparser.ConfigParser()
config.read('settings.ini')

#Something Proto would say
bot = discord.Client(activity=discord.Game(name='M-M-M-MUH'))

#Commands
@bot.event
async def on_ready():
    print('Bot ready')

@bot.event
async def on_message(message):

    #ignore self just in case
    if message.author.bot: return

    #I hate this joke but you can have it. I hope you guys can feel my disdain.
    #Only matching explicitly "hi im" or "hi i'm" or else it's going to get annoying
    ihatethispattern = "^hi\si(\')?m$"
    ihatethisprog = re.compile(ihatethispattern)

    if ihatethisprog.match(message.content.lower()):
        print("Hi, I'm:")

        await message.reply("gay")

    # Proto responds based on quote
    if message.content.startswith("proto "):

        naiahprog = "(\s)na(i|y)a(h+)?"
        naiahpattern = re.compile(naiahprog)
        crimprog = "(\s)c(r|w)im"
        crimpattern = re.compile(crimprog)
        sashaprog = "(\s)s(a|e+)sh(a+|u(h)+)"
        sashapattern = re.compile(sashaprog)
        marvinprog = "(\s)ma(rv|vr)in"
        marvinpattern = re.compile(marvinprog)

        if naiahpattern.search(message.content.lower()):
            quote = random.choice(naiah)
            print("Naiah\n")
        elif crimpattern.search(message.content.lower()):
            quote = random.choice(crim)
            print("Crim\n")
        elif sashapattern.search(message.content.lower()):
            quote = random.choice(sasha)
            print("Sasha\n")
        elif marvinpattern.search(message.content.lower()):
            quote = random.choice(marvin)
            print("Marvin\n")
        elif message.content.endswith("?"):
            quote = random.choice(questions)
            print("Question\n")
        else:
            quote = random.choice(quotes)
            print("Default")
        await message.reply(quote)

#Read config and run
bot.run(config['discord']['token'])
