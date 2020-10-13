from datetime import datetime
import requests
import discord
import bs4
import re 

def embed_return(euros):
    get = requests.get('https://finance.rambler.ru/currencies/')
    bs = bs4.BeautifulSoup(get.text, 'html.parser')
    euro = bs.select('.finance-exchange-rate__value')
    euro = euro[1].getText()
    euro = re.sub("\n", '', euro) # Убирем перенос строки
    change = bs.select('.finance-exchange-rate__link .finance-exchange-rate__difference')
    change = change[1].getText()
    change = re.sub("\n", '', change)
    try:
        euro_rub = float(euro) * float(euros[0])
        date = datetime.today().strftime('%d.%m.%Y')
        embed_obj = discord.Embed(title = 'Евро', description = f'{str(euros[0])} евро на {date} равняется {str(euro_rub)} рублей ({change})')
    except IndexError:
        embed_obj = discord.Embed(title = 'Евро', description = 'Использование: %euro [Количество]')
    return embed_obj