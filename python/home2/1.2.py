#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num= input("введи вещественное число")
vichislenie=sum(map(int,str((num)).replace('.',"")))

print(vichislenie)

