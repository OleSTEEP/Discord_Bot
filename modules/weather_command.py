import requests
import discord
import bs4
import re

def embed_return(city):
    try:
        site = 'https://sinoptik.com.ru/погода-{}'.format('-'.join(city.split()))
        get = requests.get(site.lower())
        bsoup = bs4.BeautifulSoup(get.text, 'html.parser')
        now = bsoup.select('.weather__article_main_right-table .current .table__temp')
        current_temp = now[0].getText()
        sens = bsoup.select('.weather__article_main_right-table .current .table__felt')
        sens = sens[0].getText()
        pressure = bsoup.select('.weather__article_main_right-table .current .table__pressure')
        pressure = pressure[0].getText()
        humidity = bsoup.select('.weather__article_main_right-table .current .table__humidity')
        humidity = humidity[0].getText()
        wind = bsoup.select('.current .table__wind label.show-tooltip')
        wind = wind[0].getText()
        wind = re.sub("\n", '', wind)
        description = bsoup.select('.weather__article_description-text')
        description = description[0].getText()
        embed_obj = discord.Embed(title = 'Погода в насел. пункте: {}'.format(city.capitalize()), description =

        f'''Погода сейчас:
        -Температура: {current_temp} (Ощущается как: {sens})
        -Давление: {pressure} мм
        -Влажность: {humidity}%
        -Ветер: {wind}

        Описание: {description.strip()}''')
        embed_obj.set_footer(text = '--> Данные предоставлены сервисами Рамблер и SINOPTIK')

    except IndexError:
        embed_obj = discord.Embed(title = 'Погода', description = 'Населённый пункт не найден!\n\nИспользование: %weather [Город]')
    return embed_obj 