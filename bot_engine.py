import discord
import os

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	else:
		await message.channel.send('alfa')

client.run('OTIxNTI2MzU1NjEzNTg1NDE4.Yb0MTA.1I2896D1L-8_Co_q0I7p-mN_ya') # add I