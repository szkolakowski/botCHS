import discord
import os
from stockfish import Stockfish

stockfish = Stockfish()
client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('!fen'):
		fen = str(message.content)[5:]
		print(fen)
		stockfish.set_fen_position(fen)
		bm = stockfish.get_best_move()
		stockfish.make_moves_from_current_position([bm])
		bv = stockfish.get_board_visual()
		print(bv)
		await message.channel.send(bm + '\n```bash\n' + bv + '```')
	if message.content.startswith('!pic'):
		cont = str(message.content).split(' ')
		if len(cont) != 3:
			await message.channel.send('Wrong arguments given for !pic function!')
			await message.channel.send('!pic <can white castle? (0 / 1)> <can black castle? (0 / 1)> <who moves now? (0 / 1)>')
			await message.channel.send('0 = false = black')
			await message.channel.send('1 = true = white')
			return
		try:
			string = message.attachments[0]
			await message.channel.send(string)
		except FileNotFoundError:
			return

client.run('OTIxNTI2MzU1NjEzNTg1NDE4.Yb0MTA.1I2896D1L-8_Co_q0I7p-mN_yaI') # add I