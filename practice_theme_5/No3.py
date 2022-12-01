# Вводится число N. Создайте матрицу из N строк и N столбцов вида
# (N = 4)
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

N = int(input("Введите число N: "))
A = []
for i in range(N):
    A.append([0]*i + [1] + [0]*(N-i-1))

for elem in A:
    print(' '.join(list(map(str, elem))))