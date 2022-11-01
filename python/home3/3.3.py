# Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# НЕ СЧИТАЕТ ДРОБНУЮ ЧАСТЬ
from decimal import Decimal
from random import uniform
import math 
result = [float(Decimal(i) / 10) for i in range(-9,110,7)]
print(result)

def maxMin(num):
    nums=num[0]
    nums2=num[-1]
    # #print(f"минимальный элемент={nums2}  максимальный элемент={nums}")
    return [round(uniform(nums,nums2), 2) for i in (num)]

def drobchast(num):
    nums= [round(i - int(i), 2) for i in (num)]
    return (max(nums) - min(nums))
  


maxMin(result)
drobchast(maxMin)


# from random import uniform
# def get_real_nums (n, frst, last):
#     return [round(uniform(frst,last), 2) for i in range(n)]

# def find_diff(mynums):
#     nums = [round(x - int(x), 2) for x in (mynums)]
#     return max(nums) - min(nums)

# n = 5
# frst = 1
# last = 9
# mynums = get_real_nums(n, frst, last)

# print (mynums)
# print(find_diff(mynums))