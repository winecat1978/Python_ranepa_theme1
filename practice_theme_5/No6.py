# Создайте файл формата .txt и запишите в него любой текст. 
# Напишите программу, которая подсчитает количество символов в файле.

new_one = open("text.txt","wt", encoding="utf-8")
print("Собака Булка укусила кота Симбу", file = new_one)
new_one.close()

file = open('text.txt',"rt")
data = file.read()
print(len(data))
file.close()