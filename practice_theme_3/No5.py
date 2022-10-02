#Задача 5. Пользователь вводит число N, а затем последовательность из N чисел. 
# Замените все нули в этой последовательности на среднее арифметическое ненулевых элементов. Полученную последовательность выведите на экран.
n = int(input("Введите кол-во чисел: "))
list = [0]*n
for elem in range(len(list)):
    list[elem] = int(input("Введите число: "))
print(*list)

sum = 0
p = n
for i in list:
    sum+=i
    if i == 0:
        p-=1
av = sum/p

for i in range(len(list)):
    if list[i] == 0:
        list[i] = av
print(*list)