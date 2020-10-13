import discord
import random

def embed_return(statement):
    embed_obj = discord.Embed(title = statement.lower().capitalize(), description = f'Это правда на {random.randint(0, 100)}%')
    if statement == None:
        embed_obj = discord.Embed(title = 'Правда', description = 'Использование: %true [Высказывание]') 
    return embed_obj