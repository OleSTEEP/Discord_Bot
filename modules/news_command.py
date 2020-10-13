import requests
import discord
import bs4

def embed_return():
    try:
        get = requests.get('https://yandex.ru/')
        soup = bs4.BeautifulSoup(get.text, 'html.parser')
        news = soup.select('.news__item-content')

        embed_obj = discord.Embed(
        title = 'Сейчас в СМИ',
        description = f'''1). {news[0].getText()}
                          2). {news[1].getText()}
                          3). {news[2].getText()}
                          4). {news[3].getText()}
                          5). {news[4].getText()}
                          6). {news[5].getText()}
                          7). {news[6].getText()}
                          8). {news[7].getText()}
                          9). {news[8].getText()}
                         10). {news[9].getText()}''')

    except IndexError:
        embed_obj = discord.Embed(title = 'Новости', description = 'Сервис временно недоступен, попробуйте позже')
    return embed_obj