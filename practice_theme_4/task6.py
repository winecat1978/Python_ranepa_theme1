# Пользователь вводит натуральные числа через пробел, 
# но некоторые из них с ошибками. 
# Выведите сумму корректно записанных чисел.
# 1 2x 311 3_14	--> 312

def summa():
    text = input("Введите числа: ")
    list1 = []
    list1 = list(map(str,text.split(" ")))
    print(list1)
    list2 = []
    i = 0
    for item in list1:
        for i in len(item):
            if item[i] in [0,1,2,3,4,5,6,7,8,9]:
                list2.append(item)

    sum = 0
    #for index in range(len(list1)):
        #try:
            #list1[index] = int(list1[index])
        #except ValueError:
            #pass
    print(list1)
    #for item in list1:
        #if isinstance(item) == True:
           # sum+=item
    #return sum

res = summa()
print(res)