# найти поиск уникальных последовательностей
from random import randint


def posledovat(size, m, n):
   return [randint(m, n) for i in range(size)]

size = 10
m = 1
n = 9
origin = posledovat(size, m, n)
print(origin)

a=set(origin)
print(a)
a=list(a)
print(a)