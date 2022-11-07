# module time and function time()
# Сколько времени работает программа? 
# сохранить текущее время в переменной перед началом работы алгоритма
# выполнить алгоритм
# получить новое текущее время
# разность двух времен -- время работы
import time
import random
count = int(input())
starttime = time.time()
L = []
for i in range(count):
    L.append(random.randint(0,100))
print('Working time: ',time.time()-starttime)
