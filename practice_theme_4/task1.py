#Напишите функцию, которая получает на вход список из строк 
# и возвращает длину самой длинной из них.

def The_longest_str(text):
    list = text.split("." or "!" or "?")
    print(list)
    max = 0
    for elem in list:
        if len(elem) > max:
            max = len(elem)
    return max

text = input("Введите строки: ")
answer = The_longest_str(text)
print(answer)
