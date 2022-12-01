import copy
a = [[1,2],[3,4]]
# b = a[:] # copying
# b.append([5,6])
# b[0][0] = 100
# #матрицу НЕЛЬЗЯ копировать срезами - изменяется исходник
# print(b)

b = copy.copy(a) # испортит А
print(b)
c = copy.deepcopy(a) # не испортит А



