# Discord_Bot

## Русский язык
Готовый Discord бот.

### Возможности бота (Команды)
* news          (Новости)  
* time          (Время по МСК)  
* true          (Вероятность правдивости)  
* wiki          (Википедия) (`Использование: %wiki [Запрос]`)  
* ban           (Бан!) (`Использование: %ban [Участник] [Причина]`)  
* kick          (Кик!) (`Использование: %kick [Участник] [Причина]`)  
* rand          (Генератор чисел) (`Использование: %rand [От] [До]`)  
* euro          (Курс евро рублями) (`Использование: %euro [Количество]`)  
* end           (Подскажет, через сколько закончится обучение (До 31 мая))  
* dollar        (Курс доллара рублями) (`Использование: %dollar [Количество]`)  
* trl           (Google Translate) (`Использование: %trl [Текст] [Язык перевода]`)  
* weather       (Погода в населённом пункте) (`Использование: %weather [Населённый пункт]`)  
* yap           (Яндекс картинки (Отправляет в чат рандомную найденную картинку по запросу)) (`Использование: %yap [Запрос]`)  
* calc          (Калькулятор) (`Использование: %calc [Число] [Знак] [Число]`. `Использование sqrt: %calc sqrt [Число]`)  

#### Запланированые команды
* who           (Кто...)  
* goop          (Google картинки)    

### Установка и настройка
* Установите Python 3 (latest)  
* Установите `geckodriver` (Linux) и Firefox  
* В командной строке `pip install -r /путь/в/папку/с/ботом/requirements.txt`  
* В файле `main.py` впишите желаемое имя бота и ваш токен  

### Запуск
Запуск осуществлятся посредством запуска `main.py`

### Кастомизация

* Шаблон для добавления новых команд (Также присутствует в конце файла `main.py`)  
```
@client.command()  
async def command_name(ctx):  
    [Тело команды]  
    await ctx.send() # Отправка содержимого в скобках в канал  
```

## English

A ready-made Discord bot.

### Bot Features (Commands)
* news          (News)  
* time          (Moscow time)  
* true          (Probability of truthfulness)  
* wiki          (Wikipedia) (`Usage:% wiki [Request]`)  
* ban           (Ban!) (`Usage:% ban [Member] [Reason]`)  
* kick          (Kick!) (`Usage:% ban [Member] [Reason]`)
* rand          (Number Generator) (`Usage:% rand [From] [To]`)  
* euro          (Euro exchange rate in rubles) (`Usage:% euro [Quantity]`)  
* end           (Tells how long the training will end (Until May 31))  
* dollar        (Dollar exchange rate in rubles) (`Usage:% dollar [Amount]`)  
* trl           (Google Translate) (`Usage:% trl [Text] [Translation Language]`)  
* weather       (City weather) (`Usage:% weather [City]`)  
* yap           (Yandex pictures (Sends random picture to chat on request)) (`Usage:% yap [Request]`)  
* calc          (Calculator) (`Usage:% calc [Number] [Sign] [Number]`. `Usage sqrt:% calc sqrt [Number]`)  

#### Scheduled Commands
* who           (Who ...)  
* goop          (Google pictures)   

### Installation and configuration
* Install Python 3 (latest)  
* Install `geckodriver` (Linux only) and Firefox  
* On the command line, `pip install -r /path/to/bot/folder/requirements.txt`  
* In the file `main.py`, enter the desired bot name and your tocken  

### Launch
The launch is carried out by launching `main.py`

### Customization

* Template for adding new commands (Also present at the end of the `main.py` file)  
```
@ client.command ()
async def command_name (ctx):
    [Command body]
    await ctx.send () # Send parenthesized content to a pipe
```
