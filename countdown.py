import discord 
import asyncio
import os
from discord.ext import commands

prefix = '%'

token = 'NzQ0NjQ3MjE1NjM2Njc2Njk5.XzmQzA.nGs2jHztmpjIy53Vx1OdIrEOB2M'
os.system('clear')

bot = commands.Bot(command_prefix=prefix) 
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'ON. Use {prefix}countdown to start.')


@bot.command(pass_context=True)
async def countdown(ctx):
  await ctx.delete()
  a = await ctx.send('10')
  await asyncio.sleep(1)
  await a.edit(content="9") 
  await asyncio.sleep(1)
  await a.edit(content="8")
  await asyncio.sleep(1)
  await a.edit(content="7")
  await asyncio.sleep(1)
  await a.edit(content="6")        
  await asyncio.sleep(1)
  await a.edit(content="5")
  await asyncio.sleep(1)
  await a.edit(content="4")
  await asyncio.sleep(1)
  await a.edit(content="3")
  await asyncio.sleep(1)
  await a.edit(content="2")
  await asyncio.sleep(1)
  await a.edit(content="1")
  await asyncio.sleep(1)
  await a.edit(content="0")
  await asyncio.sleep(1)
  await a.edit(content="Time's Up!")
  await print("Made by Cryptos1337 and Cuet1337")

bot.run(token, bot=False)
