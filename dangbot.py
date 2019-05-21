import discord
import asyncio

from humanfriendly import parse_timespan
from random import choice

TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
    # prevent bot from replying to itself
    if message.author == client.user:
        return
    
    # say hello to the user
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    # remind a user
    elif message.content.startswith('!remind'):
        msg = 'Hello {0.author.mention} I will remind you'.format(message)
        await client.send_message(message.channel, msg)

        m = message.content.split()

        try:
            await asyncio.sleep(parse_timespan(m[1]))
            msg = 'Reminder for {0.author.mention} '.format(message)
            await client.send_message(message.channel, msg + ' '.join(m[2:]))

        except Exception as error:
            msg = 'Sike something went wrong. {0.author.mention} Please input as\n'.format(message)
            msg += '!remind [time] [message]\n'
            msg += 'time as 5h or 5m or 5s'
            await client.send_message(message.channel, msg + ' ' + str(error))

    # coin flip
    elif message.content.startswith('!flipacoin'):
        coin = ['Heads', 'Tails']
        msg = choice(coin)
        await client.send_message(message.channel, msg)

    # roshambo
    elif message.content.startswith('!roshambo'):
        result = ['Scissors', 'Paper', 'Rock']
        computer = choice(result)

        m = message.content.split()

        input = m[1]

        if input == computer:
            msg = 'You: '
            msg += input
            msg += '\nComputer: '
            msg += computer
            msg += '\nDraw'
            await client.send_message(message.channel, msg)
        elif input == 'Rock' and computer == 'Scissors':
            msg = 'You: '
            msg += input
            msg += '\nComputer: '
            msg += computer
            msg += '\nYou win'
            await client.send_message(message.channel, msg)
        elif input == 'Rock' and computer == 'Paper':
            msg = 'You: '
            msg += input
            msg += '\nComputer: '
            msg += computer
            msg += '\nYou lose'
            await client.send_message(message.channel, msg)
        elif input == 'Paper' and computer == 'Rock':
            msg = 'You: '
            msg += input
            msg += '\nComputer: '
            msg += computer
            msg += '\nYou win'
            await client.send_message(message.channel, msg)
        elif input == 'Paper' and computer == 'Scissors':
            msg = 'You: '
            msg += input
            msg += '\nComputer: '
            msg += computer
            msg += '\nYou lose'
            await client.send_message(message.channel, msg)
        elif input == 'Scissors' and computer == 'Paper':
            msg = 'You: '
            msg += input
            msg += '\nComputer: '
            msg += computer
            msg += '\nYou win'
            await client.send_message(message.channel, msg)
        elif input == 'Scissors' and computer == 'Rock':
            msg = 'You: '
            msg += input
            msg += '\nComputer: '
            msg += computer
            msg += '\nYou lose'
            await client.send_message(message.channel, msg)
        else:
            msg = '!roshambo Scissors or Paper or Rock'
            await client.send_message(message.channel, msg)

    # randomiser
    elif message.content.startswith('!random'):
        m = message.content.split()

        m.remove('!random')

        try:
            msg = choice(m)
            await client.send_message(message.channel, msg)

        except Exception as error:
            msg = '!random choice1 choice2 etc'
            await client.send_message(message.channel, msg + ' ' + str(error))

    # plugs my soundcloud
    elif 'dang' in message.content:
        msg = 'Follow dang on soundcloud www.soundcloud.com/dang000'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)