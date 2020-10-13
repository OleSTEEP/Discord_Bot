import words_base # База запрещённых слов
import requests
import discord
import random
import bs4

def yapCommand(question):
    reactions = ['*Стук*', '*knock* *knock*', 'FBI, OPEN UP!', 'Ага, попался!', 'Вы были пойманы за руку!'] 
    for word in question.split():
        no = word.lower() in words_base.words # Проверяем, есть ли в запросе запрещённое слово

        if no == True: 
            embed_obj = discord.Embed(title = 'Яндекс картинки', description = random.choice(reactions))
            return embed_obj

    url = f'https://yandex.ru/images/search?text={question}&isize=large'
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    img = soup.findAll('img') # Парсим все img
    try:
        url = [img[2].get('src'),
               img[3].get('src'),
               img[4].get('src'),
               img[5].get('src'),
               img[6].get('src'),
               img[7].get('src'),
               img[8].get('src'),
               img[9].get('src'),
               img[10].get('src'),
               img[11].get('src')]

        url = random.choice(url)
        embed_obj = discord.Embed(title = 'Яндекс картинки', description = f'Картинка по запросу {question}')
        embed_obj.set_image(url = f'http:{url}')
        return embed_obj
    except IndexError:
        embed_obj = discord.Embed(title = 'Яндекс картинки', description = 'По вашему запросу ничего не найдено!')
        return embed_obj