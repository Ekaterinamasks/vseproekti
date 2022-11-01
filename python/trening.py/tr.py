#метод set.intersection () возвращает набор который содержит сходство между двумя и более наборами
x={"apple", "banana","cherry"}
y={"google", "microsoft", "apple"}

z=x.intersection(y)

print(z)

x={"a", "b","c"}
y={"c", "d","e"}
z={"c", "g","c"}

result=x.intersection(y,z)

print(result)