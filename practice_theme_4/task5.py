# Число называется идеальным, если все его цифры одинаковые. 
# Найдите все идеальные числа до 1000. 
# Для этого напишите соответствующую функцию.
def perfect_nums():
    list = []
    for i in range(1,1001):
        if i%11 == 0 and i < 100:
            list.append(i)
        if i%111 == 0:
            list.append(i)
    return list

res = perfect_nums()
print(res)

