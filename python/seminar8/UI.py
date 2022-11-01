from loger import input_data,print_data,put_data,delete_data
def privetstvie():
    print("Добро пожаловать в журнал учеников: \n" 
      "1.Внести данные\n"
      "2.Удаление данных\n"
      "3.Изменение данных\n"
      "4.Показать все данные файла\n"
      "5.Выход\n")
    comand=int(input("укажите цифру для перехода -> "))

    while comand < 1 or comand > 5:
        print('Неверно введена команда')
        comand = int(input("выбирите от 1 до 5-> "))
    if comand == 1:
        input_data()
        privetstvie()
    elif comand == 2:
        delete_data()
        privetstvie()
    elif comand == 3:
        put_data()
        privetstvie()
    elif comand==4:
        print_data()
    else:
        print("ДО скорой встречи!")
        exit()
        
    