# найти сумму числе стоящих на нечетной позиции
def suma(a):
    return sum(a[i] for i in range(1,len(a),2))

a=[1,2,3,5,1,3,10,1]
print(suma(a))