from data_kreate import data_name, data_adres, data_phone, data_surname


def input_data():
    name = data_name()
    surname = data_surname()
    phone = data_phone()
    address = data_adres()
    var = int(input("Выбири формат для записи\n\n"
                    "1 Вариант:\n\n"
                    "Сорокозабораперепрыжкин\n"
                    "Джон\n"
                    "+79990999399\n"
                    "г. Санкт-Петербург ул. Казявкина д13кв666\n\n"
                    "2 Вариант:\n\n"
                    "Сорокозабораперепрыжкин;Джон;+79990999399;г. Санкт-Петербург ул. Казявкина д13кв666\n\n"
                    "Выбери че тебе больше нравится: "))

    while var != 1 and var != 2:
        print('Капец ты конченый, я ж написал 1 или 2')
        var = int(input("Етить твою мать, 1 или 2?: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
            print("Поздравляю ты встал на учет в военкомат")
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')
            print("Поздравляю ты встал на учет в военкомат")


def print_data1():
    print('данные из 1 файла вот\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    return data_first


def print_data2():
    print('эт из 2 файла данные\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_second


def put_data():
    print('Ну и в каком файле ты уже накосячил?')
    data_first = print_data1()
    data_second = print_data2()
    number_file = int(input('Давай цифарку 1 или 2: '))

    while number_file != 1 and number_file != 2:
        print('ну ты и тапок!')
        number_file = int(
            input('твоя моя понимать? номер файла 1 или 2 сюда->:  '))

    if number_file == 1:
        print("Какую из писюлек по счету ты хочешь изменить?")
        number_journal = int(input('Введи номер записи: '))
        number_journal -= 1
        if number_journal > len(data_first):
            print("снимаю шляпу перед твоей тупостью, ты и здесь умудрился накосячить")
            number_journal = int(input('Введи номер записи: '))
        print(f'Изменить данную запись\n{data_first[number_journal]}')
        name = data_name()
        surname = data_surname()
        phone = data_phone()
        address = data_adres()
        data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
            data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Понял , принял, записал,наверное')
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        if number_journal > len(data_second):
            print("снимаю шляпу перед твоей тупостью, ты и здесь умудрился накосячить")
            number_journal = int(input('Введи номер записи: '))
        print(f'Изменить данную запись\n{data_second[number_journal]}')
        name = data_name()
        surname = data_surname()
        phone = data_phone()
        address = data_adres()
        data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address}\n'] + \
            data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Ну допустим записал')


def delete_data():
    print('эх, от куда удалять будем?')
    data_first = print_data1()
    data_second = print_data2()
    number_file = int(input('Go номер файла: '))

    while number_file != 1 and number_file != 2:
        print('таких тупых тут еще не было')
        number_file = int(input('Етить твою мать,1 или 2?: '))

    if number_file == 1:
        print("Какую запись стереть с лица земли?")
        number_journal = int(input('Введи номер записи: '))
        number_journal -= 1
        if number_journal > len(data_first):
            print("снимаю шляпу перед твоей тупостью, ты и здесь умудрился накосячить")
            number_journal = int(input('Введи номер записи: '))

        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + \
            data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Удаление прошло успешно')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        if number_journal > len(data_second):
            print("снимаю шляпу перед твоей тупостью, ты и здесь умудрился накосячить")
            number_journal = int(input('Введи номер записи: '))
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + \
            data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Удаление прошло успешно')
