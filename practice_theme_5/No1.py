# Пользователь вводит число N и M, а потом N строк по M чисел в каждой.
# Создайте матрицу из этих чисел. 
# Вычислите наибольший элемент в каждой строке матрицы.
N = int(input("Введите N: "))
M = int(input("Введите M: "))

def fill(n,m):
    A = []
    for i in range(n):
        row = input(f"Введите элементы строки в кол-ве {m}: ").split()           
        for i in range(len(row)):
            row[i] = int(row[i])   # каждый элемента списка row преобразовали в число
        A.append(row) 
    return A 

def find_max(a):
    maxs = []
    for row in a:
        maxs.append(max(row))
    return maxs

a = fill(N,M)
print(a)
maxs = find_max(a)
print(maxs)