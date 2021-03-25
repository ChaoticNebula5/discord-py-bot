import discord #import the discord libary
from discord.ext import commands 

client = commands.Bot(command_prefix = '.') #Define the bot and prefix

@client.event
async def on_ready(): #when the bot is in the 'ready' state
  print("Bot is ready!") #print to console that the bot is ready
 
 @client.command() #Creating a new command to which the bot will reply
async def ping(ctx): #Defining the function
  embed=discord.Embed(title='Pong 🏓', description=f'Ping is {round(client.latency * 1000)}ms') #Making the embed
  await ctx.send(embed=embed) #Sending the embed
 
client.run('your token here') #discord login (bot token) make one at https://discord.dev --> Applications --> Make New --> Bot
