# Задача 3. Пользователь вводит строку из слов, разделённых пробелами.
# Сколько слов этом предложении имеют длину менее 4 символов?
line = input("Введите строку: ")
count_sym = 0
count_words = 0

for i in line:
    if i == " ":
        count_words+=1
#найти пробел - его индекс-1 = кол-во знаков, если меньше 4, то прибавляем в рез-т
#удаляем строку до пробела и потворяем
res = 0
while count_words > 0:
    a = line.find(' ')
    if a < 4:
        res+=1
    line = line[a+1:]
    count_words-=1

print(res)

    
# dog eats meat




    



