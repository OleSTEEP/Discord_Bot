import discord
import random

def embed_return(number):
    try:
        embed_obj = discord.Embed(title = 'Генератор чисел', description = f'Сгенерированное число - {random.randint(int(number[0]), int(number[1]))}')
    except IndexError:
        embed_obj = discord.Embed(title = 'Генератор чисел', description = 'Использование: %random [От] [До]' )
    return embed_obj