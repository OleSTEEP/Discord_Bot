#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#GitHub release

#---------------------------------------------------------------
# Options
bot_name = 'bot'
token = 'NzA3OTgxMzEyMzE2NjcwMDMy.XrQs-g.sRn3OdWg5A9ZiZqCFR8eQaBh7xM'
prefix = '%'
#---------------------------------------------------------------

print("[Launch]Initialization...")

import logging
import discord
import asyncio
from datetime import datetime
from discord.ext import commands

# Создание логгера
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename = 'logs/{}_log_{}_{}.log'.format(bot_name, datetime.today().strftime('%d.%m.%Y'), str(datetime.now().strftime("%H.%M"))), encoding = 'utf-8', mode = 'w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

print("[Launch]Login...")

# Создание клиента бота
client = commands.Bot(command_prefix = prefix, help_command = None)

@client.event
# Готов к работе
async def on_ready():
    print('[{} {}] '.format(datetime.today().strftime('%d.%m.%Y'), str(datetime.now().strftime("%H:%M:%S"))) + 'Login in {0.user}'.format(client))

@client.command()
async def time(ctx):
    from modules import time_command
    await ctx.send(time_command.string)

@client.command()
async def dollar(ctx, *dollars):
    from modules import dollar_command
    await ctx.send(embed = dollar_command.embed_return(dollars))

@client.command()
async def euro(ctx, *euros):
    from modules import euro_command

    await ctx.send(embed = euro_command.embed_return(euros))

@client.command()
async def weather(ctx, *, city):
    from modules import weather_command
    await ctx.send(embed = weather_command.embed_return(city))

@client.command()
async def true(ctx, *, statement):
    from modules import true_command
    await ctx.send(embed = true_command.embed_return(statement))

@client.command()
async def rand(ctx, *number):
    from modules import rand_command
    await ctx.send(embed = rand_command.embed_return(number))

@client.command()
async def wiki(ctx, *question):
    from modules import wiki_command
    await ctx.send(embed = wiki_command.embed_return(question))

@client.command()
async def calc(ctx, *calc_int):
    from modules import calc_command
    await ctx.send(embed = calc_command.embed_return(calc_int))

@client.command()
async def info(ctx):
    from modules import info_command
    await ctx.send(embed = info_command.embed_return(client))

@client.command()
async def trl(ctx, *, trans_text):
    from modules import trl_command
    await ctx.send(embed = trl_command.embed_return(trans_text))

@client.command()
async def trl_help(ctx):
    from modules import trl_command
    await ctx.send(embed = trl_command.help_return())

@client.command()
async def news(ctx):
    from modules import news_command
    await ctx.send(embed = news_command.embed_return())

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    from modules import ban_command
    success, string = ban_command.string_return(member, reason)
    if success == True:
        await member.ban(reason = reason)
    await ctx.send(string)

@client.command()
async def yap(ctx, *, question):
    from modules import yap_command
    await ctx.send(embed = yap_command.yapCommand(question))

@client.command()
async def end(ctx):
    await ctx.send('Пожалуйста, подождите...') 
    from modules import end_command
    await ctx.send(embed = end_command.embed_return())

@client.command()
async def help(ctx):
    embed_obj = discord.Embed(title = 'Помощь', description =
    f'''Я - {bot_name} и вот что я могу:
    - news          (Новости)
    - time          (Время по МСК)
    - true          (Вероятность правдивости)
    - wiki          (Википедия) (Использование: %wiki [Запрос])
    - ban           (Бан!) (Использование: %ban [Участник] [Причина])
    - rand          (Генератор чисел) (Использование: %rand [От] [До])
    - euro          (Курс евро рублями) (Использование: %euro [Количество])
    - end           (Подскажет, через сколько закончится обучение (До 31 мая))
    - dollar        (Курс доллара рублями) (Использование: %dollar [Количество])
    - trl           (Google Translate) (Использование: %trl [Текст] [Язык перевода])
    - weather       (Погода в населённом пункте) (Использование: %wthr [Населённый пункт])
    - yap           (Яндекс картинки (Отправляет в чат рандомную найденную картинку по запросу)) (Использование: %yap [Запрос])
    - calc          (Калькулятор) (Использование: %calc [Число] [Знак] [Число]. Использование sqrt: %calc sqrt [Число])
    ''')
    await ctx.send(embed = embed_obj)

# Разделитель
print("___________________________________________________")

client.run(token)


#Шаблон команды
'''
@client.command()
async def test(ctx):
    await ctx.send()
'''
