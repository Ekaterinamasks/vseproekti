# МЕТОДО YIELD 
# # Код Python3 для демонстрации
# # использования ключевого слова yield
 
# # Поиск слова pythonru в тексте

# # Импорт библиотеки для работы 
# # с регулярными выражениями
# import re

# # Этот генератор создает последовательность
# # значений True: по одному на каждое
# # найденное слово pythonru
# # Также для наглядности он выводит
# # обработанные слова
# def get_pythonru (text) :
#     text = re.split('[., ]+', text)
#     for word in text:
#         print(word)
#         if word == "python.ru":
#             yield True
 
# # Инициализация строки, содержащей текст для поиска
# text = "В Интернете есть множество сайтов, \
#             но только один pythonru. \
#             Программа никогда не прочтет \
#             последнее предложение."

# # Инициализация переменной с результатом
# result = "не найден"

# # Цикл произведет единственную итерацию
# # в случае наличия в тексте pythonru и 
# # не сделает ни одной, если таких слов нет
# for j in get_pythonru(text):
#     result = "найден"
#     break
# print ('Результат поиска: %s' % result)
# \\\\\\\\\\\\\\\\\\\\\\\\
# print(eval('(5+3)*2'))
# print("2".isdigit())
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# найти поиск уникальных последовательностей
# from random import randint

# def posledovat(size, m, n):
#    return [randint(m, n) for i in range(size)]

# size = 10
# m = 1
# n = 9
# origin = posledovat(size, m, n)
# print(origin)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\
# from random import random
# def nepovtor_num(a,N):
#  for i in range(N): 
#     f = False
#     for j in range(N):
#         if a[i] == a[j] and i != j:
#             f = True
#             break
#     if f == False:
#         print(a[i],end=' ')
# print()

# nepovtor_num(origin,size)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\
# ************способ более простой!для этой задачи!!!!!!*****************
# # a=set(origin)
# print(a)
# a=list(a)
# print(a)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# напишите программу вычисления арифм выражения заданного строкой .используйте операции  +-*\
# def kalkyl(a):
#     znaki=['+','*','-','/']
#     a=[]
#     f=''
#     for i in a :
#         a.isdigit()
#         f+=i
#         f.append(int(f))
#     print(f)
#     f=list(f)

# a=5+2   
# kalkyl(a)



# OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
#              '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
 
# def parse(line):
#     num = ''
#     for i in line:
#         if i in '1234567890.':
#             num += i
#         elif num:
#             yield float(num)
#             num = ''
#         if i in OPERATORS or i in '()':
#             yield i
#     if num:
#         yield float(num)
 
# def sort(parsed):
#     tmp = []
#     for i in parsed:
#         if i in OPERATORS:
#             while tmp and tmp[-1] != '(' and OPERATORS[i][0] <= OPERATORS[tmp[-1]][0]:
#                 yield tmp.pop()
#             tmp.append(i)
#         elif i == ')':
#             while tmp:
#                 x = tmp.pop()
#                 if x == '(':
#                     break
#                 yield x
#         elif i == '(':
#             tmp.append(i)
#         else:
#             yield i
#     while tmp:
#         yield tmp.pop()
 
# def calc(sort):
#     tmp = []
#     for i in sort:
#         if i in OPERATORS:
#             y = tmp.pop()
#             x = tmp.pop()
#             tmp.append(OPERATORS[i][1](x, y))
#         else:
#             tmp.append(i)
#     return tmp[0]
 
# inp = input('Calculate: ')
# print ('Equall: ', calc(sort(parse(inp))))

# \\\\\\\\\\\\\\\\\использование метода eval
# a='(1+12)*3+(1+1)'
# print(eval(a))
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# найти сумму числе стоящих на нечетной позиции
# def suma(a):
#   return sum(a[i] for i in a if i%2==1 )
  # f = [lambda b: b+b]

  

def suma(a):
    return sum(a[i] for i in range(1,len(a),2))

a=[1,2,3,5,1,3,10,1]
print(suma(a))


