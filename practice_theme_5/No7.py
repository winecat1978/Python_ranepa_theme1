# Создайте файл формата .txt и запишите в него слова, 
# разделённые пробелом. Не используйте знаки препинания. 
# Напишите программу, которая подсчитает количество слов в этом файле.

new_one = open("No7.txt","wt", encoding="utf-8")
print("Собака Булка укусила кота Симбу", file = new_one)
new_one.close()

file = open('text.txt',"rt")
data = file.read()
words = data.split()

print(len(words))
file.close()