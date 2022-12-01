# Пользователь вводит число N, 
# после чего вводит N пар символ_число. 
# Создайте файл ans8.txt и запишите в отдельные строки 
# каждый символ соответствующее число раз.

N = int(input("Введите число: "))
list_nums = []
list_signs = []
for i in range (N):
    data = input("Введите символ и число: ")
    list_nums.append(int(data[2]))
    list_signs.append(data[0])

new_data = []
for i in range(N):
    line = list_signs[i]*list_nums[i]
    new_data.append(line)

file_1 = open('fileNo8.txt', 'w')
for  line in new_data:
    file_1.write(line + '\n')
file_1.close()