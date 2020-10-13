from memory_profiler import memory_usage
import discord

def embed_return(client):
    ram = memory_usage()
    ram = round(ram[0])
    ping = round(client.latency * 1000)
    embed_obj = discord.Embed(title = 'Информация', description = f'Работаю... Использовано оперативной памяти: {ram} Мб, пинг: {ping} мс')
    return embed_obj