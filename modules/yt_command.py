from selenium import webdriver
import discord

def createHeadlessFirefoxBrowser():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless') # Добавляем опцию - работать скрытно
    return webdriver.Firefox(options=options)

def remove():
    try:
        import os
        os.remove('downloads/youtube_temp')
    except:
        pass

def embed_return(ctx, link, voice):
    try:
        if link[0] == 'stop':
            remove()
            return
    except:
        embed_obj = discord.Embed(title = 'YouTube', description = 'Использование: %yt [Ссылка на воспроизводимое видео]')
        return embed_obj

    from pytube import YouTube
    
    yt = YouTube(link[0])
    
    stream = yt.streams.first()
    
    remove()
    
    stream.download('downloads')
    import re
    title_clear = re.sub(r'[^\w\s]', '', yt.title)
    import os
    os.rename(f'downloads/{title_clear}.mp4', 'downloads/youtube_temp')
    try:
    	import ffmpeg
        voice.play(discord.FFmpegPCMAudio(source = "downloads/youtube_temp"), after=lambda e: remove())
    except UnboundLocalError:
        embed_obj = discord.Embed(title = 'YouTube', description = 'Отключите бота от голосого канала или дождитесь окончания проигрывания (Проигрывание возможно только в одном голосовом канале).')
        return embed_obj
    
    embed_obj = discord.Embed(title = 'YouTube', description = f'Проигрывание "{yt.title}"')
    embed_obj.set_image(url = yt.thumbnail_url)
    
    return embed_obj
