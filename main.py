#Est's child
import discord
import asyncio
import random

client = discord.Client()
lovecommand = ['Your eyes sparkle today.','I dont know about it, <@{}>', 'I already stole your heart :)']

@client.event
async def on_message(message):
    channel = message.channel
    if message.content == 'I love you!':
        await channel.send(random.choice(lovecommand).format(message.author.id))

client.run('NzA2NTQ4OTE5Nzg5NjgyNzYx.Xq78Sw.YJqhIIJp3W85NrOYsZaWYXfgl3A')
