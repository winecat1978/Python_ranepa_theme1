# Пользователь вводит число N и M, 
# а потом N строк по M чисел в каждой. 
# Создайте матрицу из этих чисел. 
# Вычислите наибольший элемент в каждом столбце матрицы.
N = int(input("Введите N: "))
M = int(input("Введите M: "))

def matr(n,m):
    A = []
    for i in range(n):
        row = input(f"введите строку из {m} элементов: ").split()
        for i in range(len(row)):
            row[i] = int(row[i])
        A.append(row)
    return A

def find_max(a, m, n):
    maxs = []
    j = 0
    while j < m:
        i = 0
        biggest_in_column = 0
        column = []
        while i < n:
            column.append(a[i][j])
            i+=1
        biggest_in_column = max(column)
        maxs.append(biggest_in_column)
        j+=1
    return maxs

a = matr(N,M)
res = find_max(a,M,N)
print(res)