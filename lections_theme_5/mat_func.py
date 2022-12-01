# a = []
# n = 4
# for i in range(n):
#    row = input().split()
#    for i in range(len(row)):
#        row[i] = int(row[i])
#    a.append(row)
# print(a)

#b = []
#for i in range(n):
#    b.append([int(j) for j in input().split()])

#c = []
#for i in range(n):
#    c.append(list(map(int,input().split())))


#def sumstr(a): ищет сумму в рядах
#     res = []
#     for row in a:
#         s = 0
#         for elem in row:
#             s+=elem
#         res.append(s)
#     return res

# a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(*sumstr(a))
# n = 4
# m = 3
# for i in range(n):
#     for j in range(m):
#         if i % 2 != 0:
#             a[i][j] = 1
# # распечатать матрицу
# for i in range(n):
#     if i%2 != 0:
#         for j in range(m):
#             a[i][j] = 1
# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()

# def delems(L,elem):
#     i = 0
#     while i<len(L):
#         if L[i] == elem:
#             L.pop(i) #удаляет элемент по индексу i
#         else:
#             i+=1

# def delems(L,elem):
#     while elem in L: # цикл в цикле (дольше)
#         L.remove(elem)

# X = [1,2,1,2,2,3,4,2,1]
# delems(X,2)
# print(*X)
# For i in range(len(L)) - вычисляет длину ОДИН раз

M = [[1,2,3],[3,4,5]]
#M.pop(1) # deleted row
# Ways to Print:
for row in M:
    for elem in row:
        print(elem, end=' ')
    print()

for row in M:
    print(' '.join(list(map(str,row))))