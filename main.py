import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print ('--------')

@bot.command(name='r')
async def rollDice(ctx, dice):
    total = 0
    totalDice = dice.split('d')
    numOfDice = int(totalDice[0])
    sidesOfDice = int(totalDice[1])
    for i in range(numOfDice):
        total += random.randint(1, sidesOfDice)
        print('Total so far is:', total)
    await ctx.send('You roll is: \n')
    await ctx.send(total)

bot.run('OTkwMzAwMTczODE1MTI4MTM1.G1fFBY.Y1TJFPBKAkRLh3FHlr1mUqkhj2id7Fhx9KIVAE')
