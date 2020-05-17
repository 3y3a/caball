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
async def on_connect():                                       #Ok
    print("Welcome back Commander")
    #channelup = cabal.get_channel(695286021176426536)
    #await channelup.send("``Подключён``")
    await cabal.change_presence( status = discord.Status.online, activity = discord.CustomActivity ("123"))
    #activity = discord.Game ("C&C")) 

@cabal.command(pass_context= True)  
async def пнул(ctx, user: discord.User):
    await ctx.channel.purge(limit = 2)
    await ctx.send(f"{user.mention}")

@cabal.command(pass_context= True)           
async def Справка(ctx):
    author = ctx.message.author
    await ctx.send(f" {author.mention} Приветствую, я #дополнить# ")

@cabal.command(pass_context= True)                          #Ok
async def Время(ctx):
    await ctx.send(f"```Подключаю модуль времени...```")
    time = datetime.now()
    mtime = timedelta(hours=3)
    mtime = time + mtime
    mtime = mtime.strftime("%H:%M")
    await ctx.send(f" ```Текущее время МСК {mtime} ```")
    
@cabal.command(pass_context= True)
async def Новый_период(ctx):
    time = date.today()
    timenext = timedelta(days = 2)
    timenext = time + timenext
    time = time.strftime("%d/%m")
    timenext = timenext.strftime("%d/%m")
    cursor.execute(f"UPDATE Legates SET datenow = ('{time}'), datenext = ('{timenext}')")
    conn.commit()

cursor.execute("SELECT datenow, datenext FROM Legates")
datedoklad = cursor.fetchall()
datenow = datedoklad[0][0]
datenext = datedoklad[0][1] 

@cabal.command(pass_context= True)                          
async def Очистка(ctx, amount = 18):
    await ctx.channel.purge(limit = amount)

@cabal.command(pass_context= True)                          
async def Доклад(ctx):
    one = randint(0, 50)
    two = randint(50, 100)
    await ctx.send(f"Подготавливаю доклад...")
    time.sleep(2)
    await ctx.send(f"Чтение данных {one}%...")
    time.sleep(2)
    await ctx.send(f"Запрос личных данных {two}%...")
    time.sleep(2)
    await ctx.send(f"Готово.")
    cursor.execute("SELECT name, time, norma FROM Legates")
    results = cursor.fetchall()
    await ctx.send(f"***Период: {datenow} - {datenext}***")
    for i in range (len(results)):
        if {results[i][2]} == {results[i][1]}:
            await ctx.send(f"```{results[i][0]} - {results[i][1]} / {results[i][2]} (норма выполнена)```")
        else:
            await ctx.send(f"```{results[i][0]} - {results[i][1]} / {results[i][2]}```")

@cabal.command(pass_context= True)                          #ok
async def Запись(ctx, tim):
    cursor.execute(f"UPDATE Legates SET time = ('{tim}') WHERE id = ('{ctx.author.id}')")
    conn.commit()
    time.sleep(2)
    await ctx.send(f"```Запись сделана```")

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
