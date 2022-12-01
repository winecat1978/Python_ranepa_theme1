a = [[1,2,3],[5,6,7]]
#print(a[0][0])
a[1][2] = 8
#print(a[1][2])

def fill(n,m):
    a = []
    c = 1
    for row in range(n):
        a.append([])
        for elem in range(m):
            a[row].append(c)
            c+=1
    return a

print(fill(3,4))

def filll(a,n,m):
    c = 1
    for row in range (n):
        a.append([])
        for elem in range (m):
            a[row].append(c)
            c+=1
    return
#изменение списка в функции и изменение их вовне
a = []
filll(a,3,4)
print(a)