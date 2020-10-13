import discord

def string_return(member, reason): 
    if reason == None:
        string = 'Укажите причину бана!'
    else:
        try:
            await member.ban(reason = reason)
            string = f'{member} успешно забанен!'
        except:
            string = 'Недостаточно прав!'
    return string