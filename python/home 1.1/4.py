# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# не (Х или У или Z)= не Х и не У и не Z
result = True
for x in True, False:
    for y in True, False:
        for z in True, False:
            result = (not(x or y or z) == (not x and not y and not z))
            print((not(x or y or z) == (not x and not y and not z)))
