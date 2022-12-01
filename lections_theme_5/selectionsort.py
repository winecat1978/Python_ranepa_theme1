# SelectionSort
# ищем max/min элемент и меняем его с последним
# потом смотрим массив без этого эл-та
# сложность - О(n^2)
# remove - тоже цикл
# (n-1)(n-2)/2 = n^2/2 - 3n/2 + 1 

L = [3,8,-1,5,2,15,10]
for j in range(len(L)):
    imax = 0
    for i in range(1,len(L)-j):
        if L[i] > L[imax]:
            imax = i
    L[imax],L[len(L)-j-1] = L[len(L)-j-1],L[imax] # changed places
print(L)