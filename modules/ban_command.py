import discord

def string_return(member, reason):
    success = False 
    if reason == None:
        string = 'Укажите причину бана!'
    else:
        try:
            success = True
            string = f'{member} успешно забанен!'
        except:
            string = 'Недостаточно прав!'
    return success, string
