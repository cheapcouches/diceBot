import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

#Print to console that everything is good to go
@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print ('--------')

#command itself
@bot.command(name='r')
async def rollDice(ctx, dice):
    total = 0 #total of all dice rolled - will be sent to discord

    # from the command, split the dice notation into two usable variables
    totalDice = dice.split('d')
    numOfDice = int(totalDice[0])
    sidesOfDice = int(totalDice[1])

    #roll dice
    for i in range(numOfDice):
        total += random.randint(1, sidesOfDice)
        print('Total so far is:', total)

    # send results to discord
    await ctx.send('You roll is: \n')
    await ctx.send(total)

bot.run('BOT_TOKEN')
