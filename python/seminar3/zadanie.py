# кортежи
# my_tupl = (1, 2, 3)

# множества,
# my_set=set([1,2,6,4])
# print(my_set)

# словарь dict()
# my_dict = {
#     (12): "стол",
#     (54): "кровать"
# }


# for key in my_dict:   #обращеине к ключу
#     print(key)

# for i in my_dict.items(): #обращеине к элементам в словаре вместе с ключом
#     print(i)

# for val in my_dict.values(): #обращение только к элементам словаря
#     print(val)

# for key,val in my_dict.items():  # разбиение ключа и обьекта
#     print(f"key-> {key}  val->{val}" )

# a=list(my_dict.values()) #превращение словаря в список
# print(a)


# # задача 1
# # задайте список .напишите программу которая определит присутсвует ли в заданном списке строк некторое число
a=['12','123a', '45756','asd']
for i in a:
 if '12' in i:
  print(f"12 присутствует в ->{i}")


# ЗАДАЧА 2
# напишите программу которая определит позицию второго вхождения строки в списки либо сообщит что ее нет
# a = ['12', '123a', 'asd', '45756', 'asd' ,'asdr','aeds']
# try:
#  l=[i for i, d in enumerate(a) if d =='asd']
#  print(l[1])
# except:
#     print(f"элемента нет в списке, или второго вхождения нету")

# ЗАДАЧА 3
# # РЕАЛИЗУЙТЕ АЛГОРТИМ СЛУЧАЙНЫХ ЧИСЕЛ
# import time
# a = str(time.time())
# b = a[1]+a[-6]
# print(int(b))