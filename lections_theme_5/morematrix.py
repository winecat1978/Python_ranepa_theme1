n = int(input("Введите n: "))
A = []
# for i in range(n):
#     A.append([0]*n)
#вариант 3
for i in range(n):
    A.append([2]*i + [1] + [0]*(n-i-1))
#вариант 1
# for i in range(n):
#     for j in range(n):
#         if i > j:
#             A[i][j] = 2
#         elif i == j:
#             A[i][j] = 1
#вариант 2
# for i in range(n):
#     for j in range(i):
#         A[i][j] = 2
#     A[i][i] = 1

for elem in A:
    print(' '.join(list(map(str, elem))))

