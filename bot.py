#!/usr/bin/python36

import discord
import asyncio
import configparser
import re
import string
import random

config = configparser.ConfigParser()
config.read('settings.ini')

#Something Proto would say
client = discord.Client(activity=discord.Game(name='M-M-M-MUH'))

#Commands
@client.event
async def on_ready():
    print('Bot ready')

@client.event

async def on_message(message):

    #ignore self just in case
    if message.author.bot: return

    if message.content.startswith('!proto'):
        print('Random Proto Quote')
        with open('quotes.txt') as quotelist:
            quote = quotelist.read().splitlines()
        randomquote = random.choice(quote)
        await message.reply(f"{randomquote}")

    if message.content.startswith('!help'):
        print('Help Command Called')
        await message.reply('Use the command `!proto` to get your very own Proto Weewoojin Quote', mention_author=True)

    #I hate this joke but you can have it. I hope you guys can feel my disdain
    ihatethispattern = "^hi\si(\')?m$"
    ihatethisprog = re.compile(ihatethispattern)

    if ihatethisprog.match(message.content.lower()):
        print("Hi, I'm:")

        #... god.
        await message.reply("gay")

#Read config and run
client.run(config['discord']['token'])
