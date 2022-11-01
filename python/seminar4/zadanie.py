# # записать в файл все числа от 0 до n .n задается пользователем
# n = int(input("Введи число "))
# spisok=list(range(n+1))

# with open('test.txt', 'w', encoding='utf-8') as file:
#     for i in spisok:
#         file.write(f'{str(i)}\n')

# # with open('test.txt', 'r') as file: #чтение файла
# #     k = len(file.readlines())
# #     file.seek(0)  # скидывает на 0 позицию
# #     for i in range(k):
# #         a = file.readline()
# #         if a != 'n':
# #             print(a)

# with open('test.txt', 'r') as file: #еще один из способов чтения файла функция split() . отличный способ
#     read_file=file.read()
#     list_of_rows=read_file.split()
# print(list_of_rows)

# list_of_rows=list(map(int,list_of_rows)) #распаковка в инт тип
# print(list_of_rows)

# ЗАДАНИЕ 2
# задать список из n элементов заполненных числами из [-n до n]
# найдите произведение элементов на указанных позициях
# позиции сохранит в файл в одной строке одно число

# def zapolnenie_spiska(num):
#     list = []
#     i = num * -1
#     while i <= num:
#         list.append(i)
#         i += 1
#     return list


# with open ('text.txt','w') as file: #запись индексов в файл 
#     indeces=input("Давай числа через пробел")
#     indeces=indeces.split(' ')
#     for el in indeces:
#        file.write(f'{el}\n')



# def proizvedenie(num):
#     with open('text.txt', 'r') as file: 
#      read_file=file.read()
#      list_of_rows=read_file.split()
#      list_of_rows=list(map(int,list_of_rows)) #распаковка в инт тип
#      print(list_of_rows)
#      poz1=list_of_rows[0]
#      poz2=list_of_rows[1]
#      print(num[poz1] * num[poz2])


# print(zapolnenie_spiska(5))
# proizvedenie(zapolnenie_spiska(5))


