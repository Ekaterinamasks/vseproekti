# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
lst = list(range(1, 10))


def fun(lst):
 summa = 0 
 print(lst)
 for i in range(len(lst)):
   if i % 2 == 1:
    summa=summa+lst[i]
 print(summa)


fun(lst)
