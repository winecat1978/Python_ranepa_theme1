import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Создание пустого массива

# empty_array = np.empty([2,2], str)
# print(empty_array)
# print(empty_array.shape)
# print(empty_array.size)

# Проверка на то, является ли массив пустым

# a = np.array([])
# b = np.array([1,2])

# def check_empty(a):
#     if a.size == 0:
#         print(a, ' : Empty')
#     else:
#         print(a, ' : Not empty')

# check_empty(a)
# check_empty(b)

# Подсчет кол-ва элементов 
# a = np.array([])
# b = np.array([1,2])

# def get_elems(array):
#     return array.ndim and array.size

# print(a, 'element_count : ', get_elems(a))
# print(b, 'element_count : ', get_elems(b))

# Arrange between intervals
# a = np.arange(4,12)
# print(a)
# print(a.shape)

# c = np.arange(2,12,1.5)
# print(c)

# Change size of a massive
# c = np.arange(12,30,3)
# d = c.reshape(2,3)
# print(c)
# print(d)

# Set up random massive
# a = np.random.randint(10, size = 5)
# print(a)
# b = np.random.randint(10, size=(2,3))
# print(b)
# print(b.dtype)

#Massive of strings
# a = np.array(('Moscow', 'New York', 'London'))
# print(a)
# print(a.dtype)

# Save csv
# a = np.asarray([ [1,2,3], [4,5,6]])
# print(a)
# np.savetxt("abc.csv", a, delimiter=",")

# Get a part of a matrix
# x = np.array([[1,2],[3,4],[5,6]])
# print(x)
# y = x[:,0]
# print(y)
# z = x[1,:]
# print(z)

# Reshape
# a = np.matrix([[1,2,3,4], [5,6,7,8],[9,10,11,12]])
# c = np.reshape(a,-1) # 1 string
# b = np.reshape(a,(1,-1)) # 1 string
# d = np.reshape(a,(2,-1)) # не ясно, сколько элементов в строке
# e = np.reshape(a, (4,3))
# f = np.reshape(a, (-1,2))
# print(a)
# print(c)
# print(b)
# print(d)
# print(e)
# print(f)

# Округление
# x = np.random.random(10)
# print(x)
# np.set_printoptions(precision = 3)
# print(x)

# Сортировка (return index)
# a = np.random.randint(0,10,(3,3))
# print(a)
# b = a[a[: ,2].argsort()]
# print(b)

# Обратная матрица
# b = np.array([[2,3],[4,5]])
# print(b)
# c = np.linalg.inv(b)
# print(c)
# x = np.matrix([[10,20],[30,40]])
# print(x)
# print(x.I)

# Masks
# условие, создающий массив булевого типа
# a = np.arange(12).reshape((3,4))
# print(a)
# a_bool = a<6
# print(a_bool)
# print(a[a_bool])

# Маска с ненулевыми элементами
# a = np.arange(12).reshape((3,4))
# print(a)
# print(np.count_nonzero(a > 5))
# print((a%3 == 1).sum())
# print(np.count_nonzero(a%3 == 1))

# Перевернуть массив
# flipup = flip ud = up | down
# a = np.arange(4).reshape(2,2)
# print(a)
# b = np.flipud(a)
# print(b)
# share memory, b - link to object a
# print(np.shares_memory(a,b)) # True
# c = np.flipud(a).copy() # don't share memory but don't copy structure
# deep copy - saves everything
# print(np.shares_memory(a,c)) # False
# d = np.fliplr(a) # меняет местами слева направо элементы строки
# print(a)
# # print(d)
# e = np.flip(a) # changes everything
# j = a[::-1, :: -1] # the same, share memory true
# print(j)
# print(e)
# у двух разных срезов - память НЕ общая

# Конвертация numpy b list
# a = np.arange(10).reshape(2,5)
# print(a)
# print(a.dtype)
# print(type(a))
# print(type(a[0]))
# print(type(a[0][0]))

# b = a.tolist()
# print(b)
# print(type(b))
# print(type(b[0]))
# print(type(b[0][0]))

# Numpy where
# a = np.arange(8).reshape(2,4)
# print(a)
# b = np.where(a > 4, 0, 20)
# # if true -> 0, else: 20
# print(b)
# # & - and    | - or    ~ - not
# c = np.where((a>3) & (a <7),0,20)
# d = np.where((a>3) & (a<7),0,a) # оставляем а
# e = np.where((a>5), 0,a*4)
# print(e)
# print(c)
# print(d)

# List to numpy array
# a = [0,1,2]
# print(type(a))
# b = np.array(a,dtype = 'float32')
# c = np.asfarray(a)
# print(c.dtype)
# d = np.asarray(a, float)
# print(type(d))
# print(d.dtype)
# print(b.dtype)

# Найти общие значения между массивами
# a = np.random.randint(0,10,10)
# b = np.random.randint(0,10,10)
# print(a)
# print(b)
# print(np.intersect1d(a,b)) 
# возвращает только уникальные значения

# Даты
# today = np.datetime64('today', 'D')
# print(today)
# after2days = np.datetime64('today', 'D') + np.timedelta64(5, 'D')
# print(after2days)
# before3days = np.datetime64('today', 'D') - np.timedelta64(3, 'D')
# print(before3days)
# afterweek = np.datetime64('today', 'D') + np.timedelta64(1, 'W')
# print(afterweek)

# # Создать массив дат
# a = np.arange('2022-09-15','2022-09-25', dtype='datetime64[D]')
# print(a)
# # первая дата, конечная дата, тип данных [шаг]
# x = np.arange('2022-02', '2022-06', dtype='datetime64[M]')
# print(x)

# Рандомная матрица
# a = np.random.random((5,10))
# print(a)
# a.sort() # сортировка в порядке убывания
# print(a)

# # String to numpy array
# from io import StringIO
# content = StringIO('''1,2,36, ,8, 20, , 20 ''')
# a = np.genfromtxt(content, delimiter=",", dtype=np.int)
# print(a)

# Find the nearest elem in array
# a = np.arange(10,60,7)
# print(a)
# b = 23
# c = a.flat[np.abs(a - b).argmin()]
# # a.flat[condition]
# print(c)

# Перемещение строк
# a = np.arange(9).reshape(3,3)
# print(a)
# a[[0,1]] = a[[1,0]]
# # поменяли местами 1 и 2 строки местами
# print(a)

# Перемешивание
# a = np.arange(15)
# print(a)
# np.random.shuffle(a)
# # пересортировка
# print(a)

# Достать элемент из матрицы
# a = np.arange(27).reshape(3,3,3)
# print(a)
# print(a[1,1,2])

# Повторение массива
# a = np.array([[1,2,3]])
# print(a)
# b = np.repeat(a,3,axis=0)
# # np.repeat(что повторяем, сколько раз, по стобцам/строкам)
# print(b)

# Функции агрегации
# a = np.arange(6).reshape(2,3)
# a+=1
# print(a)
# a_min=np.min(a) # find min
# print(a_min)
# a_max=np.max(a) # find max
# print(a_max)
# a_sum = np.sum(a) # sums all elems
# print(a_sum)

# # Функции агрегации с axis = 1
# x = np.arange(10).reshape((2,5))
# print(x)
# print(x.min(axis=0))
# # сравнивает столбцы - вывел массив с меньшими элементами
# print(x.min(axis=1)) # сравнил строки - меньшие элементы каждой строки
# print(x.min()) # вывел наименьший элемент всей матрицы

# Percentile
# x = np.arange(6).reshape((2,3))
# print(x)
# print(np.percentile(x,90,0))
# массив, персентиль, применяем в строкам или столбцам
# # Median
# print(np.median(x))

# Pirson Correlation
# x = np.array([0,1,3])
# y = np.array([2,4,5])
# print(x)
# print(y)
# print(np.corrcoef(x,y))

# Считать  кол-во вхождений
# x = np.array([1,2,2,1,1,1,5,5])
# print(x)
# print(np.bincount(x))
# # массив сост из n элементов от 0 до max в массиве
# # [0-0, 1-4,2-2,3-0,4-0,5-2]

# Randint 
# x = np.random.randint(10,20,(4,2))
# print(x)

# Random choice
# x = np.random.choice(40,4, replace = False)
# # random.choice(from 1 to 39, array 4 size, replace=False - без повторов)
# # replace=True - возможно повторение 
# print(x)

# Random seed
# np.random.seed(12)
# # начальное приближение, принцип генерации чисел
# # псевдослучайная последовательность
# a=np.random.rand(4)
# print(a)
# np.random.seed(12)
# b=np.random.rand(4)
# # та же последовательность, что и при первом сиде 12
# print(b)
# c=np.random.rand(4)
# # другая последовательность 
# print(c)

# Уникальные элементы
# x = np.array([1,2,3,4,3,2,5,6,6])
# print(x)
# out, indices = np.unique(x, return_inverse=True)
# print(out)
# unique, counts = np.unique(x,return_counts=True)
# unique_dict = dict(zip(unique, counts))
# print(unique_dict)
# the same without numpy from most used to less used
# import collections
# col_counter = collections.Counter(x)
# print(col_counter)

# in1d Совпадение элементов массивов
# x = np.array([0,1,2,3,4,1])
# y = np.array([0,1,2])
# print(np.in1d(x,y))
# #булевый массив, маска 

# Поиск уникальных элементов внутри значений
# x = np.array([0,1,2,3,4,1])
# y = np.array([0,1,2])
# print(np.intersect1d(x,y))
# # массив совпавших значений
# print(np.setdiff1d(x,y))
# массив уникальных значений (нет пересечения)

# # Вырожденная матрица
# b = np.array([[2,3],[4,6]])
# # Прямоугольная матрица: элементы строки или столбца линейно зависимы 
# # с элементами других столбцов(строк)
# try: 
#     np.linalg.inv(b)
# except Exception as err:
#     print('Error : ', err)

# объединение массивов
# x = np.array([0,1,6,2,3,4,1])
# y = np.array([0,1,2,5])
# z = np.union1d(x,y)
# print(z)
# отсортировано в порядке возрастания
# только уникальные неповторяющиеся элементы

# Преобразование типов
# x = np.array([[2.0,4.0],[2.4,5.3]])
# print(x)
# y = x.astype(int)
# print(y)
# z = np.int_(x)
# print(z)
# потеря части информации - отбрасывание дробной части
# уменьшение объема информации - экономия памяти

# Array vs asarray
# x = np.matrix(np.ones((3,3)))
# print(x)
# np.array(x)[2] = 2
# print(x)
# исходная матрица остается прежней, общая память не действует
# для каждого массива память своя
# np.asarray(x)[2] = 2
# print(x)
# память общая, исходная матрица изменится

# flatten
# a = np.arange(6).reshape(2,3)
# print(a)
# b = list(a.flatten())
# # вытягивает в строку
# print(b)
# print(type(b))

# Добавить элементы в массив
# a = np.arange(4).reshape(2,-1)
# print(a)
# b = np.hstack((a, np.zeros((a.shape[0],1), dtype = a.dtype)))
# # соединение массива а и массива нулей, с формой от массива а по столбцам, 1 столбец
# print(b)
# c = np.array([[5,6]])
# print(a)
# print(c)
# Соединение массивов (должны быть одноразмерны)
# d = np.concatenate((a,c), axis = 0) # добавили строку вниз
# print(d)
# e = np.concatenate((a,c.T), axis = 1) # добавили столбец
# # не забыть траснпонировать .T
# print(e)
# f = np.concatenate((a,c), axis = None) 
# # flattening and appending
# print(f)

# Reverse 1D array
# x = np.arange(4)
# print(x)
# y = x[:: -1]
# print(y)

# Reverse 2D array
# x = np.arange(8).reshape(2,-1)
# print(x)
# y = x[:: -1]
# print(y)
# меняет местами строки

# Картинки
# from PIL import Image 
# image = Image.open('C:\\Users\\mob19\\Downloads\\домик в коломне.jpeg')
# image_np = np.asarray(Image.open('C:\\Users\\mob19\\Downloads\\домик в коломне.jpeg'))
# print(type(image_np))
# image_np.shape
# from matplotlib import pyplot as plt
# # %matplotlib inline
# plt.imshow(image_np /image_np.std(axis=0))
# plt.imshow(image_np /np.quantile(image_np,.9,axis=0))
# # высветление

# Удаление элементов массива
# a = np.array([1,3,5,4,7])
# print(a)
# indices = [2,3]
# b = np.delete(a,indices)
# print(b)
# # по индексам

# set div
# b = np.array([3,4])
# c = np.setdiff1d(a,b)
# print(c)
# ищет не входящие, не пересек. эл-ты

# Замена переменных
# через where или через маску
# a = np.random.rand(2,4)
# print(a)
# a[a>0.3] = 3
# print(a)

# Векторизация
# aa = np.array([[1,2,3,4],[2,3,4,5],[4,5,6,7],[7,8,9,10]])
# bb = np.array([[100,200,300,400],[100,200,300,400],[100,200,300,400],[100,200,300,400]])
# def vec2(a,b):
#     return a+b
# func2 = np.vectorize(vec2)
# print(func2(bb[:,1],aa[:,1]))
# # сумма двух объектов

# def get_max(a,b):
#     if(a>b):
#         return a
#     return b
# b_vectfunc = np.vectorize(get_max)
# x = [[1,2,3],[4,7,2]]
# y = [7,4,5]
# result = b_vectfunc(x,y)
# print(result)
# # возвращает большее из двух чисел по строкам
# # сравнивая массивы

# One more sort
# a = np.random.randint(1,10,9).reshape(3,3)
# print(a)
# b = np.apply_along_axis(sorted,0,a)
# print(b)

# Method Append
# a = np.array([1,2])
# b = np.array([3,4])
# print(a)
# print(b)
# c = np.append([a],[b], axis = 0)
# print(c)
# # объединяет массивы
# d = np.append([a],[b], axis = 1)
# print(d)
# добавляется вбок, продолжением в строку

# Передача среза по индексам
# a = np.array([11,22,33,44,55])
# print(a)
# idx = [4,2,0,1,3]
# #задаем последовательность индексами
# b = a[idx]
# # засунули последовательность в новый массив
# print(b)

# Module Pickle
# a = np.array([10,20])
# print(a)
# import pickle
# b = pickle.dumps(a,protocol = 4)
# # dumps -- сериализация - выглядит как бинарный файл
# # dump - сохраняет файл 
# # loads - обратно
# print(b)
# c = pickle.loads(b)
# print(c)