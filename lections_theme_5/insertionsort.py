# Сортировка вставками

L = [3,-1,5,2,10,8,15]
# 
# for j in range(1,len(L)):
#     for i in range(j,0,-1): # oт j до 0 с шагом -1
#         if L[i] < L[i-1]:
#             L[i],L[i-1] = L[i-1],L[i]
# print(L)

for j in range(1, len(L)):
    imax = 0
    k = j
    for i in range(j-1,-1,-1):
        if L[j] < L[i]:
            k = i
    elem = L.pop(j)
    L.insert(k,elem)
print(L)
