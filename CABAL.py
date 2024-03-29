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
#import sqlite3
import pymysql

key_words = ["CABAL", "cabal", "Cabal"]

cabal = commands.Bot(command_prefix= "!")

@cabal.event                                
async def on_connect():                                       
    print("Module 1 status OK")
    #channelup = cabal.get_channel(695286021176426536)
    #await channelup.send("``Подключён``")
    await cabal.change_presence( status = discord.Status.online, activity = discord.CustomActivity ("123"))
    #activity = discord.Game ("C&C"))
    

@cabal.command(pass_context= True)  
async def пни(ctx, user: discord.User):
    await ctx.channel.purge(limit = 1)
    await ctx.send(f"{user.mention}")

@cabal.command(pass_context= True)
async def скарманил(ctx, user: discord.User, channel: discord.TextChannel):
    await ctx.message.delete()
    user2 = ctx.message.author
    await channel.send(f"{user2} скарманил {user.mention}")

@cabal.command(pass_context= True)                        
async def Время(ctx):
   time = datetime.now()
   mtime = timedelta(hours=3)
   mtime = time + mtime
   mtime = mtime.strftime("%H:%M")
   await ctx.send(f" ```Текущее время МСК {mtime} ```")
    
@cabal.command(pass_context= True)
async def Новый_период(ctx):
    conn = pymysql.connect(
    database = "heroku_37902c259aa0c69",
    user = "bfb248ab836452",
    password = "7ba0fd68",
    host = "eu-cdbr-west-03.cleardb.net",
    #port = "3306",
    charset = "utf8mb4",
)
    cursor = conn.cursor()
    await ctx.message.delete()
    time = date.today()
    timenext = timedelta(days = 6)
    timenext = time + timenext
    time = time.strftime("%d/%m")
    timenext = timenext.strftime("%d/%m")
    cursor.execute(f"UPDATE Legates SET datenow = ('{time}'), datenext = ('{timenext}')")
    cursor.execute(f"UPDATE Legates SET tim = ('00:00'), endtime = ('00:00'), event = ('0')")
    await ctx.send(f"Начало нового периода {time} - {timenext}")
    conn.commit()
    cursor.close

@cabal.command(pass_context= True)
async def Ивент(ctx, event_new):
    conn = pymysql.connect(
    database = "heroku_37902c259aa0c69",
    user = "bfb248ab836452",
    password = "7ba0fd68",
    host = "eu-cdbr-west-03.cleardb.net",
    #port = "3306",
    charset = "utf8mb4",
)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE Legates SET event = ('{event_new}') WHERE id = ('{ctx.author.id}')")
    conn.commit()
    cursor.close
    await ctx.send(f"Количество ивентов за данную сессию учтено")
    cursor.execute("SELECT name, tim, norma, datenow, datenext, event, events_all FROM Legates")
    results = cursor.fetchall()
    f = open ("test.txt", "w")
    for i in range (len(results)):
        if str(results[i][2]) <= str(results[i][1]):
            f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} (норма выполнена) / ивенты ")
        else:
            f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} / ивенты ")
        if str(results[i][6]) <= str(results[i][5]):
            f.write(f"{results[i][5]} / {results[i][6]} (норма выполнена) \n \n")
        else:
            f.write(f"{results[i][5]} / {results[i][6]} \n \n")
    f.close()
    f = open ("test.txt", "r")
    await channel.send(f"```{f.read()}```")
    conn.commit()
        
@cabal.command(pass_context= True)
async def Зашел(ctx, server, starttime):
    conn = pymysql.connect(
    database = "heroku_37902c259aa0c69",
    user = "bfb248ab836452",
    password = "7ba0fd68",
    host = "eu-cdbr-west-03.cleardb.net",
    #port = "3306",
    charset = "utf8mb4",
)
    if ctx.author.id == 345253518376173570:       #zuza
        cursor = conn.cursor()
        time1 = datetime.strptime(starttime,"%H:%M")
        time1 = time1.strftime("%H:%M")
        cursor.execute(f"UPDATE Legates SET starttime = ('{time1}') WHERE id = ('{ctx.author.id}')")
        conn.commit()
        cursor.close
        await ctx.send(f"С возвращением, Создатель. Постараюсь не разрушать код реальности раньше времени. Учёт времени запущен.")
    elif ctx.author.id == 364491118005714966:          #deriator  
        cursor = conn.cursor()
        time1 = datetime.strptime(starttime,"%H:%M")
        time1 = time1.strftime("%H:%M")
        cursor.execute(f"UPDATE Legates SET starttime = ('{time1}') WHERE id = ('{ctx.author.id}')")
        conn.commit()
        cursor.close
        await ctx.send(f"С возвращением лейтенант, удачно провести время. Учёт запущен.")
    elif ctx.author.id == 370199534183120897:          #fanta  
        cursor = conn.cursor()
        time1 = datetime.strptime(starttime,"%H:%M")
        time1 = time1.strftime("%H:%M")
        cursor.execute(f"UPDATE Legates SET starttime = ('{time1}') WHERE id = ('{ctx.author.id}')")
        conn.commit()
        cursor.close
        await ctx.send(f"Рад вашему возвращению, нечасто я вас вижу. Учёт запущен.")
    elif ctx.author.id == 488038345151217719:   #pmm
        await ctx.send(f"Отказ услуги. Рапорт об наказании N213")
    else:
        cursor = conn.cursor()
        time1 = datetime.strptime(starttime,"%H:%M")
        time1 = time1.strftime("%H:%M")
        cursor.execute(f"UPDATE Legates SET starttime = ('{time1}') WHERE id = ('{ctx.author.id}')")
        conn.commit()
        cursor.close
        await ctx.send(f"Запуск учёта времени на посту для {ctx.author.name}.")

@cabal.command(pass_context= True)
async def Вышел(ctx, server, endtime):
    conn = pymysql.connect(
    database = "heroku_37902c259aa0c69",
    user = "bfb248ab836452",
    password = "7ba0fd68",
    host = "eu-cdbr-west-03.cleardb.net",
    #port = "3306",
    charset = "utf8mb4",
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT starttime, endtime FROM Legates WHERE id = ('{ctx.author.id}')  ")
    timeinserver = cursor.fetchall()
    time2 = datetime.strptime(endtime,"%H:%M")
    time3 = timeinserver[0][0]
    time4 = datetime.strptime(time3,"%H:%M")
    time5 = timeinserver[0][1]
    time6 = datetime.strptime(time5,"%H:%M")
    timeall = time2 - time4 + time6
    timeall = timeall.strftime("%H:%M")
    cursor.execute(f"UPDATE Legates SET tim = ('{timeall}'), endtime = ('{timeall}') WHERE id = ('{ctx.author.id}')")
    if ctx.author.id == 345253518376173570:             #zuza
        await ctx.send(f"Досвидания. Общее время пребывания в реальности №{server} - {timeall}.")
    elif ctx.author.id == 364491118005714966:          #deriator
        await ctx.send(f"Жду вас вновь, лейтенант. Общее время на посту {timeall}.")
    elif ctx.author.id == 370199534183120897:          #fanta
        await ctx.send(f"Жду вас вновь, командир. Общее время на посту {timeall}.")
    else:
        await ctx.send(f"{ctx.author.name} общее время на посту: {timeall}")

    channel = discord.utils.get(ctx.guild.channels, id=801607997229891584)
    await channel.purge(limit = 1)
    
    cursor.execute("SELECT name, tim, norma, datenow, datenext, event, events_all FROM Legates")
    results = cursor.fetchall()
    f = open ("test.txt", "w")
    for i in range (len(results)):
        if str(results[i][2]) <= str(results[i][1]):
            f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} (норма выполнена) / ивенты ")
        else:
            f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} / ивенты ")
        if str(results[i][6]) <= str(results[i][5]):
            f.write(f"{results[i][5]} / {results[i][6]} (норма выполнена) \n \n")
        else:
            f.write(f"{results[i][5]} / {results[i][6]} \n \n")
    f.close()
    f = open ("test.txt", "r")
    await channel.send(f"```{f.read()}```")
    conn.commit()

@cabal.command(pass_context= True)
async def Перезапись(ctx, legat, endtime):
    conn = pymysql.connect(
    database = "heroku_37902c259aa0c69",
    user = "bfb248ab836452",
    password = "7ba0fd68",
    host = "eu-cdbr-west-03.cleardb.net",
    #port = "3306",
    charset = "utf8mb4",
)
    if ctx.author.id == 345253518376173570:#zuza
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Legates SET tim = ('{endtime}'), endtime = ('{endtime}') WHERE id = ('{legat}')")
        conn.commit()
        cursor.close
        await ctx.send(f"Изменения времени для {legat} в размере {endtime} учтены.")
    elif ctx.author.id == 445588020230356993:          #latikoma
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Legates SET tim = ('{endtime}'), endtime = ('{endtime}') WHERE id = ('{legat}')")
        conn.commit()
        cursor.close
        await ctx.send(f"Изменения времени для {legat} в размере {endtime} учтены.")
    elif ctx.author.id == 370199534183120897:          #fanta
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Legates SET tim = ('{endtime}'), endtime = ('{endtime}') WHERE id = ('{legat}')")
        conn.commit()
        cursor.close
        await ctx.send(f"Изменения времени для {legat} в размере {endtime} учтены.")
    else:
        await ctx.send(f"Отказ. Рапорт об несанкционированном доступе сформирован и отправлен, ждите.")

@cabal.command(pass_context= True)
async def Смена_снаряжения(ctx, time, legat):
    conn = pymysql.connect(
    database = "heroku_37902c259aa0c69",
    user = "bfb248ab836452",
    password = "7ba0fd68",
    host = "eu-cdbr-west-03.cleardb.net",
    #port = "3306",
    charset = "utf8mb4",
)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE Legates SET norma = ('{time}') WHERE id = ('{legat}')")
    conn.commit()
    await ctx.send(f"Норма времени для {legat} изменена.")

@cabal.command(pass_context= True)                          
async def Доклад(ctx):
    await ctx.message.delete()
    conn = pymysql.connect(
    database = "heroku_37902c259aa0c69",
    user = "bfb248ab836452",
    password = "7ba0fd68",
    host = "eu-cdbr-west-03.cleardb.net",
    #port = "3306",
    charset = "utf8mb4",
)
    cursor = conn.cursor()
    #one = randint(0, 50)
    #two = randint(50, 100)
    #await ctx.send(f"Подготавливаю доклад...")
    #time.sleep(1)
    #await ctx.send(f"Чтение данных {one}%...")
    #time.sleep(1)
    #await ctx.send(f"Запрос личных данных {two}%...")
    #time.sleep(1)
    #await ctx.send(f"Готово.")
    cursor.execute("SELECT name, tim, norma, datenow, datenext, event, events_all FROM Legates")
    results = cursor.fetchall()
    await ctx.send(f"***Период: {results[0][3]} - {results[0][4]}***")
    f = open ("test.txt", "w")
    for i in range (len(results)):
        if str(results[i][2]) <= str(results[i][1]):
            f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} (норма выполнена) / ивенты ")
        else:
            f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} / ивенты ")
        if str(results[i][6]) <= str(results[i][5]):
            f.write(f"{results[i][5]} / {results[i][6]} (норма выполнена) \n \n")
        else:
            f.write(f"{results[i][5]} / {results[i][6]} \n \n")
    f.close()
    f = open ("test.txt", "r")
    await ctx.send(f"```{f.read()}```")
    #await ctx.send(f"{results[i][1]}")
    cursor.close
    
@cabal.command(pass_context= True)
async def Выдача_снаряжения(ctx, type, rank):
    conn = pymysql.connect(
    database = "heroku_37902c259aa0c69",
    user = "bfb248ab836452",
    password = "7ba0fd68",
    host = "eu-cdbr-west-03.cleardb.net",
    #port = "3306",
    charset = "utf8mb4",
)
    cursor = conn.cursor()
    id = ctx.author.id
    name = ctx.author.name
    a = 0
    b = 0
    cursor.execute(f"SELECT id, norma FROM Legates")
    results = cursor.fetchall()
    for i in range(len(results)):
        if id == results[a][0]:
            await ctx.send(f"{ctx.author.name} вы уже получили снаряжение. Приступайте к выполнению поставленных задач.")
            b = 2
            break
        a=a+1
    if b == 2:
        return
    if int(rank) == 1:
        cursor.execute(f"INSERT INTO Legates VALUES ({id}, '{name}', '04:00', '00:00', {4}, {5}, '00:00', '00:00', '0', '8')")
        conn.commit()
        await ctx.send(f"{ctx.author.name} снаряжение выдано. Удачи на поле боя.")
                
                ##cursor.execute(f"UPDATE Legates SET norma = ('04:00') WHERE id = ('{ctx.author.id}')")
    if int(rank) == 2:
        cursor.execute(f"INSERT INTO Legates VALUES ({id}, '{name}', '05:00', '00:00', {4}, {5}, '00:00', '00:00', '0', '9'))")
        conn.commit()
        await ctx.send(f"{ctx.author.name} снаряжение выдано. Удачи на поле боя.")
                
                ##cursor.execute(f"UPDATE Legates SET norma = ('05:00') WHERE id = ('{ctx.author.id}')")
    if int(rank) == 3:
        cursor.execute(f"INSERT INTO Legates VALUES ({id}, '{name}', '06:00', '00:00', {4}, {5}, '00:00', '00:00', '0', '10'))")
        conn.commit()
        await ctx.send(f"{ctx.author.name} снаряжение выдано. Удачи на поле боя.")
                
                ##cursor.execute(f"UPDATE Legates SET norma = ('06:00') WHERE id = ('{ctx.author.id}')")
    conn.commit
    
@cabal.command(pass_context= True)
async def работать (ctx, user: discord.User):   
    if ctx.message.author.id == 370199534183120897:                                      
        await user.send(f"Ебошь блять!")
    else:
        await ctx.send(f"Доступ ограничен")
    
@cabal.command(pass_context= True)
async def маска(ctx, member: discord.Member):
    await member.edit(nick=(f"{member} в маске"))
    await ctx.send(f"{member.mention} одел маску!")

@cabal.command(pass_context= True)  
async def заеби(ctx, user: discord.User):
    if ctx.message.author.id == 370199534183120897:
        for i in range (100):
            await ctx.channel.purge(limit = 2)
            await ctx.send(f"{user.mention}")
    else:
        await ctx.send(f"Доступ ограничен")


@cabal.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def say(ctx, channel : discord.TextChannel, *args):
    await ctx.message.delete()
    if ctx.message.author.id == 370199534183120897:
        text = ''
        for item in args:
            text = text + item + ' '
        await channel.send(text)
    elif ctx.message.author.id == 345253518376173570:
        text = ''
        for item in args:
            text = text + item + ' '
        await channel.send(text)
    else:
        await ctx.send(f"Доступ запрещён")


token = os.environ.get("BOT_TOKEN")
cabal.run(str(token))
