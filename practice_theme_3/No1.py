# Задача 1. Пользователь вводит число N, после чего вводит N чисел. 
# Какие числа этого списка превышают среднее арифметическое всех чисел?

n = int(input("Введите натуральное число N: "))
list = [0]*n
i = 1
while i <= n:
    list[i-1]=i
    i+=1
print(*list)
sum = 0
for item in list:
    sum+=item
av = sum/n
print(f"среднее значение списка = {av}")
list2 = []
for item in list:
    if item > av:
        list2.append(item)
print(*list2)


