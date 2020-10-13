import discord
import math

def embed_return(calc_int):
    try:
        if(calc_int[1].lower() == "+"):
            result = float(calc_int[0]) + float(calc_int[2])

        if(calc_int[1].lower() == "-"):
            result = float(calc_int[0]) - float(calc_int[2])

        try:
            if(calc_int[1].lower() == "/"):
                result = float(calc_int[0]) / float(calc_int[2])
        except ZeroDivisionError: # При делении на ноль
            embed_obj = discord.Embed(title = 'PyCalc 2.2', description = 'На ноль делить нельзя!')
            return embed_obj

        if(calc_int[1].lower() == "*"):
            result = float(calc_int[0]) * float(calc_int[2])

        if(calc_int[1].lower() == "^"):
            result = float(calc_int[0]) ** float(calc_int[2])

        if(calc_int[0].lower() == "sqrt"):
            result = math.sqrt(float(calc_int[1]))
            embed_obj = discord.Embed(title = 'PyCalc 2.2', description = f'{calc_int[0]} {calc_int[1]} = {result}')
        else:
            embed_obj = discord.Embed(title = 'PyCalc 2.2', description = f'{calc_int[0]} {calc_int[1]} {calc_int[2]} = {result}')
    except IndexError:
        embed_obj = discord.Embed(title = 'PyCalc 2.2', description = 'Использование: %calc [Число] [Знак] [Число]\nP.S. Использование sqrt: %calc sqrt [Число]') 
    return embed_obj