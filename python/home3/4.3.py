# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n=int(input("введи десятичное число-> "))
 

def preobrazovanie(n):
 a=n
 p=1
 b=0
 while a>0:
    b=b+a%2*p
    p=p*10
    a=a//2
 print(b)
 

preobrazovanie(n)

