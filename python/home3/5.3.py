# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input('Введите число-> '))

def fibonachi(n):
    fibo_list = []
    a, b = 1, 1
    for i in range(n):
        fibo_list.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibo_list.insert(0, a)
        a, b = b, a - b
    return fibo_list

fibo_list = fibonachi(n)
print(fibonachi(n))
