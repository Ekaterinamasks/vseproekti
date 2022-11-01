konfet = 100
bot_take = 0
while konfet > 0:
    take = int(input ('возьми от 1 до 28 конфет => '))
    konfet -= take
    print (f'осталось {konfet} конфет')
    if konfet > 0:
        bot_take = konfet%29
        if bot_take == 0:
            bot_take = 28
        konfet -= bot_take
        print (f'а я возьму=>  {bot_take}')
        print (f'осталось {konfet} конфет')
        if konfet == 0:
            print ("в пух и прах ! прими поражение ")
    elif konfet == 0:
        print ('ура ты победил')