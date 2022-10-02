#Задача 3. Пользователь вводит числа M и N, после чего вводит M слов (имена) 
# и ещё N слов (фамилии). Все слова различны. 
# Выведите на экран все комбинации имя_фамилия, которые можно получить из этого набора.

m = int(input("Введите число имен: "))
n = int(input("Введите число фамилий: "))
m_list = ["name"]*m
n_list = ["surname"]*n
i = 0
j = 0

while i < m:
    name = input("Введите уникальное имя: ")
    if name not in m_list:
        m_list[i] = name
        i+=1

while j < n:
    surname = input("Введите уникальную фамилию: ")
    if surname not in n_list:
        n_list[j] = surname
        j+=1

print(*n_list)
print(*m_list)

combinations = ["name_surname"]*n*m
a = 0
for j in range(len(m_list)):
    for i in range(len(n_list)):
        combination = f"{m_list[j]} {n_list[i]}"
        if combination not in combinations:
            combinations[a]=combination
            a+=1

print(combinations)

