# Задача 1. Пользователь вводит число N, после чего вводит N чисел.
# Верно ли, что они упорядочены по возрастанию?

n = int(input("Введите количество чисел: "))
list = [0]*n
i = 0

while i < len(list):
    list[i]=int(input(f"Введите число №{i+1}: "))
    i+=1
print(list)

b = 1
answer = "Да"
while b < len(list):
    if list[b]-list[b-1] == 1:
        answer = "Да"
    else:
        answer = "Нет"
        break;
    b+=1
print(answer)
    