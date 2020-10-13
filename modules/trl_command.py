from googletrans import Translator
import discord

def embed_return(trans_text):
    translator = Translator() # Инициализируем переводчик
    try:
        pop = list(trans_text.split()).pop()
        crutch = trans_text.replace(pop, '') # Костыли~ (убираем параметр языка из фразы перевода)
        try:
            result = translator.translate(crutch, dest = pop.lower())
        except:
            embed_obj = discord.Embed(title = 'Google Translate', description = 'Язык не найден. Для получения информации о языках отправте %trl_help')
        embed_obj = discord.Embed(title = 'Google Translate', description = f'{result.origin} = {result.text}').set_footer(text = f'{result.src} → {result.dest}')
    except IndexError:
        embed_obj = discord.Embed(title = 'Google Translate', description = 'Использование: %trl [Текст] [Язык перевода].') 
    return embed_obj

def help_return():
    import googletrans
    lang = str(googletrans.LANGUAGES) # Получаем языки
    lang = lang.replace("'", '')
    lang = lang.replace('{', '')
    lang = lang.replace('}', '')
    embed_obj = discord.Embed(title = 'Google Translate', description = f'Языки для перевода - {lang}\n\nИспользование: %trl [Текст] [Язык перевода]')
    return embed_obj