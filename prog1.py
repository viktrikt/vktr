n = int(input())
b =[[0 for i in range(n)]for j in range(n)]

s = 1
m = 0
while m <= n/2:
    '''для заполнения слева направо'''    
    for i in range(n):
        for j in range(m,n-m):
            if i == m:
                b[i][j] = s
                s += 1
            else:
                break
    '''для заполнения сверху вниз'''
    for j in range(n-m):
        for i in range(m + 1,n-m):
            if j == n-m-1:
                b[i][j] = s
                s += 1
            else:
                break
    '''для заполнения справа налево'''
    for i in range(n-1-m, -1,-1 ):
        for j in range(-2-m, -n-1+m, -1):
            if i == (n-m-1):
                b[i][j] = s
                s += 1
            else:
                break
    '''для заполнения снизу вверх'''
    for j in range(m - n, 1, 1):
        for i in range(-2-m, m-n, -1):
            if j == m-n:
                b[i][j] = s
                s += 1
            else:
                break
    m += 1
'''вывод результата'''
for i in range(n):
    for j in range(n):
        print(b[i][j], end=' ')
    print()
