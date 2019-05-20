import discord
import asyncio

from humanfriendly import parse_timespan

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

    # plugs my soundcloud
    elif 'dang' in message.content:
        msg = 'Follow dang on soundcloud www.soundcloud.com/dang000'
        await client.send_message(message.channel, msg)

# login message
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)