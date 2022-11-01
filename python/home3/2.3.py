# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math
lst=list(range(1,8))
print(lst)


def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: results.append(numbers[0]**2)       
    return results

print(pairs_mult(lst))