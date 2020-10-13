from selenium import webdriver
import discord
import bs4

def createHeadlessFirefoxBrowser(): # Браузер
     options = webdriver.FirefoxOptions()
     options.add_argument('--headless') # Добавляем опцию - работать скрытно
     return webdriver.Firefox(options=options)

def embed_return():
    driver = createHeadlessFirefoxBrowser() # Инициализируем Firefox для выполнения javascript
    driver.get('https://calculatr.ru/1-iyunja/')
    html = driver.page_source
    driver.quit()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    days = soup.select('p.hours')
    days = days[0].getText()
    mount = soup.select('p.mount')
    mount = mount[0].getText()
    embed_obj = discord.Embed(title = 'Счётчик', description = f'До окончания учёбы осталось: {days} (или {mount})')
    embed_obj.set_footer(text = '--> Данные предоставлены сервисом calculatr.ru')
    return embed_obj