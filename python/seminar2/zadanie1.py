#напишите программу которая принимает на вход число n и выдает последовательность из n чисел

     # def posledovatnum(n: int) -> list: #тайпхитинги
       # num=1
       # print(num,end=" ")
      #  for i in range(1,n):
      #      num=num*-3
      #      return num

     # print(posledovatnum(5))


#def seachNum(num=7,*args, **key):
 #print(args)
 #print(key)


#seachNum(5,10,20,40,50,30, a=1,b=2)'

 #ПРИКОЛЮШКА ПИТОНА
#def fuc(x=[]):
 #   x.append(5)
  #  print(x)

#fuc()
#fuc()
#fuc()
#fuc()
#fuc()

#напиишите программу в которой пользователь будет задавать две строки
# а программа определять количетсво вхождение одной строкки в другой

#st1="привет мир"
#st2="п"
#t=0
#for i in st1:
 #   if i==st2:
 #    t+=1
#print(f" буква {st2} встречается {t} раз")

 #дано число проверить кратно ли оно 5 и 10 или 15 но не 30
# a=6

# print((a % 5  ==  0 or a %  10  == 0 or a %  15  == 0) and a % 30 != 0)
#ПРО СРЕЗЫ
#st1="dffhg erter gergeg"
#print(st1[3])


# работа со списками

# n=8
# A = [i ** 2 for i in range(1, n + 1)]
# print(A)


# А в этом примере список будет состоять из строк, считанных со стандартного ввода: 
# сначала нужно ввести число элементов списка (это значение будет использовано в качестве аргумента функции range),
#  потом — заданное количество строк:

# A = [input() for i in range(int(input()))]
# print(A)

#  этом случае строку можно считать функцией input(), после этого использовать метод строки split(),
#   возвращающий список строк, разрезав исходную строку на части по пробелам. Пример:
# A = list(map(int, input().split()))
# print(A)

