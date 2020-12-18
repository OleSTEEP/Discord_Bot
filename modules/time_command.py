# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import discord
import re

def embed_return(city):

    site = 'https://time100.ru/{}'.format('+'.join(city))
    
    get = requests.get(site.lower())
    get.encoding = 'utf8'
    soup = BeautifulSoup(get.text, 'html.parser')
    time = soup.select('.display-time.text-monospace.text-center.maintime .time')
    time = time[0].getText()
    time_city = soup.select('.container .row .col-12.text-center.page-header')
    time_city = time_city[0].getText()
    try:
        city_location = soup.select('.container .row .col-12.text-right.page-header')
        city_location = city_location[0].getText()
    except IndexError:
        text = f'{time_city} - {time}'
        text = re.sub("\n", '', text)
        embed_obj = discord.Embed(title = 'Время', description = text)
        embed_obj.set_footer(text = '--> Данные предоставлены сервисом time100.ru')
        return embed_obj

    text = f'{time_city} {city_location} - {time}'
    text = re.sub("\n", '', text)
    embed_obj = discord.Embed(title = 'Время', description = text)
    embed_obj.set_footer(text = '--> Данные предоставлены сервисом time100.ru')
    return embed_obj
