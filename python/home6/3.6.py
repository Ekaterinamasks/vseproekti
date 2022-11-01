# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# n=6
a={}
n=range(6)
for i in n:
 a[i]=i+1

print(a)

def slovar(a):
    double_dict1 = {k+1:v*3+1 for (k,v) in a.items()}
    print(double_dict1)

slovar(a)

