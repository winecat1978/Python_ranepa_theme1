# Даны 3 числа. Определить, имеются ли среди них равные.
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a == b or a == c or b == c: print("ДА")
else: print("НЕТ")