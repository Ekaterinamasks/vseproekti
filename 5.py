#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 
# A (3,6); B (2,1)  7,-5); B (1,-1) 
x1=float (input("Введите значение для x1= "))
y1=float (input("Введите значение для y1= "))
x2=float (input("Введите значение для x2= "))
y2=float (input("Введите значение для y2= "))
result=0
from math import sqrt
result=(sqrt((x1- x2)**2 + (y1- y2)**2))
print(result)