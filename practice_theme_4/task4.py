# Пользователь вводит дату в формате ДД.ММ.ГГГГ. 
# Определите дату следующего дня. 
# Для этого напишите функцию, определяющую количество дней в месяце 
# и функцию, проверяющую, является ли год високосным.

def enter_data():
    data = input("Введите вашу дату рождения в формате ДД.ММ.ГГГГ: ")
    inf = list(map(int,data.split(".")))
    return inf

def month_check(list):
    # 1,3,5,7,8,10,12 - 31 | 4,6,9,11 - 30| 2 - 28/29
    max = 31
    if list[1] in [4,6,9,11]:
        max = 30
    if list[1] == 2:
        if list[2]%4 == 0:
            max = 29
        if list[2]%4 !=0:
            max = 28
        
    return max
 
def leap_year(list):
    answer = True
    if list[2]%4 !=0:
        answer = False
    return answer

def next_day(list,max_day):
    nextday = list
    if list[0] == max_day:
        if nextday[1] == 12:
            nextday[2]+=1
            nextday[1] = 1
        else:
            nextday[0] = 1
            nextday[1]+=1
    else:
        nextday[0]+=1
    return nextday

list = enter_data()
print(list)
max_day = month_check(list)
if_leap = leap_year(list)
print(f"количество дней в месяце = {max_day}")
print(f"Год високосный? {if_leap}")
res = next_day(list,max_day)
print(*res)



