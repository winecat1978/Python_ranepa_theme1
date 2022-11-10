# операционные системные вызовы - выполняются ОС
# создаем переменную
# fobj = open("text.txt1","wt", encoding="utf-8")
# print("Первый элемент", file = fobj)
# fobj.close()
# wt - записать и если файла нет, то создать его и записать
# fobj = open("text.txt1","wt", encoding="utf-8")
# fobj.write("Second элемент")
# fobj.close()

file = open("vebinar_5\poem.txt","rt")
data = file.read()
print(type(data))
print(len(data))
file.close()