# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# n=int(input("введите число-> "))

def mnogiteli():
    try:
        n=int(input("введите число-> "))
        a=[]
        b=2
        while b*b<=n:
         if n%b==0:
            a.append(b)
            n//=b
         else:
          b+=1
        if n>1:
            a.append(n)
        return a
    except:
        print("ну введи ты целочисленное число!!без запитой!")
        return mnogiteli


print(mnogiteli())
