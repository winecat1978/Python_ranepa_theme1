# Даны 4 числа. Сначала 2 стороны одного прямоугольника, потом 2 стороны другого. 
# Выведите 0, если у них одинаковая площадь. Иначе выведите любое число.
import random

a1 = int(input("Введите длину первого прямоугольника: "))
b1 = int(input("Введите ширину первого прямоугольника: "))
a2 = int(input("Введите длину второго прямоугольника: "))
b2 = int(input("Введите ширину второго прямоугольника: "))
if (a1*b1 == a2*b2):
    print(0)
else: 
    n = random.randint(0,1000)
    print(n)


