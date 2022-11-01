from tracemalloc import stop
from loger import input_data , print_data1,print_data2,put_data,delete_data

def privetstvie():
    print("Вечер в хату, бродяга! Шо делать будем?:\n" 
      "1.Маляву накатать\n"
      "2.Удаление малявы\n"
      "3.Изменение малявы\n"
      "4.Показать маляву 1 файла\n"
      "5.Показать маляву 2 файла\n"
      "6.Выход\n")
    comand=int(input("ткни цифарку-> "))

    while comand < 1 or comand > 6:
        print('Не с того ты начал')
        comand = int(input("Этить твою мать,попробуй еще раз: "))
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
        print_data1()
    elif comand==5:
        print_data2()
    else:
        print("Ну и вали")
        exit()
        
    

