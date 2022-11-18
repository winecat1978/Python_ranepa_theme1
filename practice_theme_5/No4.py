# Вводится нечётное число N. Создайте матрицу из N строк и N столбцов вида
# (N = 5)
# 1 0 0 0 1
# 0 1 0 1 0
# 0 0 1 0 0
# 0 1 0 1 0
# 1 0 0 0 1

N = int(input("Введите число N: "))
A = []
for i in range(N):
    A.append([0]*i + [1] + [0]*(N-i-1))

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            A[i][N-j-1] = 1

for elem in A:
    print(' '.join(list(map(str, elem))))