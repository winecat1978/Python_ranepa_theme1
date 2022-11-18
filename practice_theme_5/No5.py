# Пользователь вводит число N и M, а потом N строк по M чисел в каждой. 
# Создайте матрицу из этих чисел.
# В каждой строке замените отрицательные числа на среднее арифметическое 
# положительных чисел в этой строке.

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

def check(A, N, M):
    averages = []
    for i in range(N):
        pos_sum = 0
        pos = 0
        for j in range (M):
            if A[i][j] > 0:
                pos_sum+=A[i][j]
                pos+=1
        averages.append(pos_sum//pos)

    for a in range(N):
        for b in range(M):
            if A[a][b] < 0:
                A[a][b] = averages[a]
    return A

A = fill(N,M)
res = check(A,N,M)
for elem in res:
    print(' '.join(list(map(str,elem))))
