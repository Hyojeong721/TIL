n, m = map(int, input().split())


arr = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if i-j == i or i == j:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

if m == 1:
    for i in range(n):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()

elif m == 2:
    for i in range(n-1, -1, -1):
        print(' ' * (n - i -1), end='')
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()

elif m == 3:
    for i in range(n):
        cnt = n-1
        for j in range(i, -1, -1):
            print(arr[cnt][j], end=' ')
            cnt -= 1
        print()