#сортировка пузырьком - сравнение элементов 
# друг с другом (если 1>2, то их меняют местами)
# сложность сортировки: (n-1)*(n-1) = n^2-2n+1. 
# Главное - O(n^2) - цикл в цикле 
list = [3,8,-1,5,2,15,10]
# for j in range(len(list)-1):
#     for i in range(len(list)-1):
#         if list[i] > list[i+1]:
#             list[i],list[i+1] = list[i+1],list[i]
# print(list)

#чтобы не делать лишних переборов, проверок
#скорость х2 = (n^2)/2
# for j in range(len(list) - 1):
#     flag = True
#     for i in range(len(list)-1):
#         if list[i] > list[i+1]:
#             flag = False
#             list[i],list[i+1] = list[i+1],list[i]
#     if flag == True:
#         break # завершает ближайший цикл
# print(list)
# n^2/4
#еще быстрее, с каждым циклом просматриваем меньше элементов: 
for j in range(len(list) - 1):
    flag = True
    for i in range(len(list)-1-j): #поставили макс и больше ее не смотрим
        if list[i] > list[i+1]:
            flag = False
            list[i],list[i+1] = list[i+1],list[i]
    if flag == True:
        break # завершает ближайший цикл
print(list)
