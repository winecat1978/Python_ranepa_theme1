# Напишите функцию my_abs, которая возвращает модуль числа.
# Пользователь вводит несколько чисел через пробел. 
# С помощью функции my_abs превратите все отрицательные числа в этой последовательности 
# в положительные

def module(new_nums):
    ans = list(map(abs,new_nums))
    return ans

nums = input("Введите числа: ")
new_nums = list(map(int,nums.split()))

res = module(new_nums)
print(res)