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

cabal = commands.Bot(command_prefix= "?")
@cabal.event                                
async def on_connect():                                       
    print("Module 2 status OK")
    #channelup = cabal.get_channel(695286021176426536)
    #await channelup.send("``Подключён``")
    await cabal.change_presence( status = discord.Status.online, activity = discord.CustomActivity ("123"))
    #activity = discord.Game ("C&C"))
conn = pymysql.connect(
    database = "heroku_37902c259aa0c69",
    user = "bfb248ab836452",
    password = "7ba0fd68",
    host = "eu-cdbr-west-03.cleardb.net",
    #port = "3306",
    charset = "utf8mb4",
)
cursor = conn.cursor()

@cabal.command(pass_context= True)
async def start(ctx):
    i = 0
    while i < 259250:
        time.sleep (1)
        await ctx.send(f"{i}")
        if i == 259200 :
            conn = pymysql.connect(
            database = "heroku_37902c259aa0c69",
            user = "bfb248ab836452",
            password = "7ba0fd68",
            host = "eu-cdbr-west-03.cleardb.net",
            #port = "3306",
            charset = "utf8mb4",
            )
            tim = date.today()
            timenext = timedelta(days = 2)
            timenext = tim + timenext
            tim = tim.strftime("%d/%m")
            timenext = timenext.strftime("%d/%m")
            cursor.execute(f"UPDATE Legates SET datenow = ('{tim}'), datenext = ('{timenext}')")
            cursor.execute(f"UPDATE Legates SET tim = ('00:00'), endtime = ('00:00')")
            cursor.execute("SELECT name, tim, norma, datenow, datenext FROM Legates")
            results = cursor.fetchall()
            await ctx.send(f"***Период: {results[0][3]} - {results[0][4]}***")
            f = open ("test.txt", "w")
            for i in range (len(results)):
                if str(results[i][2]) <= str(results[i][1]):
                    f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} (норма выполнена) \n \n")
                else:
                    f.write(f"{results[i][0]} - {results[i][1]} / {results[i][2]} \n \n")
            f.close()
            f = open ("test.txt", "r")
            await ctx.send(f"```{f.read()}```")
            i = 0
            cursor.close
        
token = os.environ.get("BOT_TOKEN")
cabal.run(str(token))
