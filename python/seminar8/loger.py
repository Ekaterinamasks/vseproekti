
from data_kreate import data_bykvaklassa, data_rozgdenia, data_class, data_name, data_surname,data_yspevaemost,kabinet
def input_data():
    name = data_name()
    surname = data_surname()
    hb = data_rozgdenia()
    clas= data_class(),data_bykvaklassa()
    yspevaemost=data_yspevaemost()
    with open('jurnal.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{hb};{clas}{yspevaemost}\n\n')
            print("Данные внесены успешно")

def print_data():
    print('данные из файла\n')
    with open('jurnal.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(*data)
    return data


def put_data():
    print("в какой строчке хотите внести изменения?")
    print("Какую именно запись по счету Вы хотите изменить?")
    number_journal = int(input('Введи номер строки: '))
    
    name = data_name()
    surname = data_surname()
    hb = data_rozgdenia()
    clas= data_class(),data_bykvaklassa()
    yspevaemost=data_yspevaemost()
    data = data[:number_journal] + [f'{name};{surname};{hb};{clas}{yspevaemost}\n'] + \
            data[number_journal + 1:]
    with open('jurnal.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data))
    print('данные изменены')


def delete_data():
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal -= 1
    if number_journal > len(data):
            print("снимаю шляпу перед твоей тупостью, ты и здесь умудрился накосячить")
            number_journal = int(input('Введи номер записи: '))
    print(f'Удалить данную запись\n{data[number_journal - 1]}')
    data = data[:number_journal] + \
    data[number_journal + 1:]
    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data))
    print('Удаление прошло успешно')




