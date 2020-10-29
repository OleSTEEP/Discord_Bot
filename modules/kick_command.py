import discord

def string_return(member, reason):
    success = False 
    if reason == None:
        string = 'Укажите причину кика!'
    else:
        try:
            success = True
            string = f'{member} успешно кикнут!'
        except:
            string = 'Недостаточно прав!'
    return success, string