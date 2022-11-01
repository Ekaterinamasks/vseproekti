# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint
import random

def posledovat(size, m, n):
   return [randint(m, n) for i in range(size)]

size = 10
m = 1
n = 10
origin = posledovat(size, m, n)
print(origin)

from random import random
def nepovtor_num(a,N):
 for i in range(N):
    f = True
    for j in range(N):
        if a[i] == a[j] and i != j:
            f = False
            break
    if f == True:
        print(a[i],end=' ')
print()

nepovtor_num(origin,size)