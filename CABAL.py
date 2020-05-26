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
async def Новый_период(ctx):
    time = date.today()
    timenext = timedelta(days = 2)
    timenext = time + timenext
    time = time.strftime("%d/%m")
    timenext = timenext.strftime("%d/%m")
    cursor.execute(f"UPDATE Legates SET datenow = ('{time}'), datenext = ('{timenext}')")
    cursor.execute(f"UPDATE Legates SET time = Null, endtime = ('0:00')")
    conn.commit()

@cabal.command(pass_context= True)
async def Зашел(ctx, server, starttime):
    time1 = datetime.strptime(starttime,"%H:%M")
    time1 = time1.strftime("%H:%M")
    cursor.execute(f"UPDATE Legates SET starttime = ('{time1}') WHERE id = ('{ctx.author.id}')")
    conn.commit()
    await ctx.send(f"Запуск учёта времени на посту для {ctx.author.name}.")

@cabal.command(pass_context= True)
async def Вышел(ctx, server, endtime):
    cursor.execute(f"SELECT starttime, endtime FROM Legates WHERE id = ('{ctx.author.id}')  ")
    timeinserver = cursor.fetchall()
    time2 = datetime.strptime(endtime,"%H:%M")
    #time2 = time2.strftime("%H:%M")
    time3 = timeinserver[0][0]
    time4 = datetime.strptime(time3,"%H:%M")
    time5 = timeinserver[0][1]
    time6 = datetime.strptime(time5,"%H:%M")
    #time4 = time4.strftime("%H:%M")
    timeall = time2 - time4 + time6
    timeall = timeall.strftime("%H:%M")
    cursor.execute(f"UPDATE Legates SET time = ('{timeall}'), endtime = ('{timeall}') WHERE id = ('{ctx.author.id}')")
    conn.commit()
    await ctx.send(f"{ctx.author.name} общее время на посту: {timeall}")

@cabal.command(pass_context= True)
async def Дозапись(ctx, legat, endtime):
    cursor.execute(f"UPDATE Legates SET time = ('{endtime}'), endtime = ('{endtime}') WHERE name = ('{legat}')")
    conn.commit()
    await ctx.send(f"Дозапись Легату {legat} в размере {endtime} сделана.")
@cabal.command(pass_context= True)                          
async def Доклад(ctx):
    one = randint(0, 50)
    two = randint(50, 100)
    await ctx.send(f"Подготавливаю доклад...")
    time.sleep(1)
    await ctx.send(f"Чтение данных {one}%...")
    time.sleep(1)
    await ctx.send(f"Запрос личных данных {two}%...")
    time.sleep(1)
    await ctx.send(f"Готово.")
    cursor.execute("SELECT name, time, norma, datenow, datenext FROM Legates")
    results = cursor.fetchall()
    await ctx.send(f"***Период: {results[0][3]} - {results[0][4]}***")
    f = open ("test.txt", "w")
    for i in range (len(results)):
        if {results[i][2]} == {results[i][1]}:
            #await ctx.send(f"```{results[i][0]} - {results[i][1]} / {results[i][2]} (норма выполнена)```")
            f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} (норма выполнена) \n \n")
        else:
            #await ctx.send(f"```{results[i][0]} - {results[i][1]} / {results[i][2]}```")
            f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} \n \n")
    f.close()
    f = open ("test.txt", "r")
    await ctx.send(f"```{f.read()}```")


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
