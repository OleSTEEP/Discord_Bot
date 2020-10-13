import wikipedia
import warnings
import discord

def embed_return(question):
    warnings.catch_warnings()
    warnings.simplefilter("ignore")

    wikipedia.set_lang("ru") # Русский язык
    question_clean = ' '.join(question) # Запрос в строку
    try:
        embed_obj = discord.Embed(title = f'Результат из Википедии по запросу {question_clean}', description = wikipedia.summary(question_clean)) #Создаём Discord Embed
        if len(wikipedia.summary(question_clean)) > 2048:
            embed_obj = discord.Embed(title = f'Результат из Википедии по запросу {question_clean}', description = 'К сожалению, статью не возможно отобразить из - за ограничения в Discord (2048 символов)...')
    except wikipedia.exceptions.PageError: # Страница не найдена
        embed_obj = discord.Embed(title = 'Википедия', description = f'По запросу {question_clean} ничего не найдено!')
    except wikipedia.exceptions.DisambiguationError as error: # Множество вариантов
        options = error.options
        options = ', '.join(options)
        embed_obj = discord.Embed(title = 'Википедия', description = f'Найдено множество вариантов! Пожалуйста выберите один из предложенных: {options}')
    except wikipedia.exceptions.WikipediaException: # Пустое использование
        embed_obj = discord.Embed(title = 'Википедия', description = 'Использование: %wiki [Запрос]')
    return embed_obj