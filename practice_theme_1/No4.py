# Пользователь вводит 4 числа. 
# Найдите, на сколько максимальное из них больше, чем среднее арифметическое.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвертое число: "))

list = [a,b,c,d]
print("вы ввели числа:", list)
max = list[0]
for i in list:
    if max < i:
        max = i
print("max =", max)
average = (a+b+c+d)/len(list)
print("среднее арифметическое =", average)
difference = max - average
print("Ответ:", difference)


