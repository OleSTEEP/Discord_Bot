from datetime import datetime
import requests
import discord
import bs4
import re

def embed_return(dollars):
    get = requests.get('https://finance.rambler.ru/currencies/')
    soup = bs4.BeautifulSoup(get.text, 'html.parser')
    dollar = soup.select('.finance-exchange-rate__value')
    dollar = dollar[0].getText()
    dollar = re.sub("\n", '', dollar) # Удаление переноса строки
    change = soup.select('.finance-exchange-rate__link .finance-exchange-rate__difference')
    change = change[0].getText()
    change = re.sub("\n", '', change)
    try:
        dollar_rub = float(dollar) * float(dollars[0])
        date = datetime.today().strftime('%d.%m.%Y')
        embed_obj = discord.Embed(title = 'Доллар', description = f'{str(dollars[0])} долларов на {date} равняется {str(dollar_rub)} рублей ({change})')
    except IndexError:
        embed_obj = discord.Embed(title = 'Доллар', description = 'Использование: %euro [Количество]')
    return embed_obj