import discord 
import math
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import MemberConverter
from discord.utils import get
from datetime import datetime, timedelta
from datetime import date
from time import sleep
import os
import requests
import io
import time
from random import randint
import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

key_words = ["CABAL", "cabal", "Cabal"]

cabal = commands.Bot(command_prefix= "!")

@cabal.event                                
async def on_connect():                                       
    print("Welcome back Commander")
    #channelup = cabal.get_channel(695286021176426536)
    #await channelup.send("``Подключён``")
    await cabal.change_presence( status = discord.Status.online, activity = discord.CustomActivity ("123"))
    #activity = discord.Game ("C&C")) 

@cabal.command(pass_context= True)  
async def пни(ctx, user: discord.User):
    author = ctx.message.author.id
    if author == 488038345151217719:
        await ctx.send(f"Доступ запрещён")
    else:
        await ctx.channel.purge(limit = 2)
        await ctx.send(f"{user.mention}")
    

@cabal.command(pass_context= True)                        
async def Время(ctx):
    await ctx.send(f"```Подключаю модуль времени...```")
    time = datetime.now()
    mtime = timedelta(hours=3)
    mtime = time + mtime
    mtime = mtime.strftime("%H:%M")
    await ctx.send(f" ```Текущее время МСК {mtime} ```")
    
@cabal.command(pass_context= True)
async def работать (ctx, user: discord.User):   
    if ctx.message.author.id == 370199534183120897:                                      
        await user.send(f"Ебошь блять!")
    else:
        await ctx.send(f"Доступ ограничен")
    

@cabal.command(pass_context= True)  
async def заеби(ctx, user: discord.User):
    #author = ctx.message.author.id
    if ctx.message.author.id == 370199534183120897:
        for i in range (100):
            await ctx.channel.purge(limit = 2)
            await ctx.send(f"{user.mention}")
    else:
        await ctx.send(f"Доступ ограничен")

@cabal.event
async def on_message (message):                                         
    await cabal.process_commands (message)
    mess = message.content.lower()
    if mess in key_words:
        #await message.delete()
        #time.sleep (3)
        await message.author.send(f" ```анализ упоминания...```")
        time.sleep (4)
        await message.author.send(f" ```{message.author.name} - здравствуйте легат, доступ разрешён .```")
    #await message.author.send({message.author.id})



token = os.environ.get("BOT_TOKEN")
cabal.run(str(token))
