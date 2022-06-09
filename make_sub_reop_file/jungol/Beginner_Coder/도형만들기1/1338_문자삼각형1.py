n = int(input())

arr = [[0]*n for _ in range(n)]
i = 0
cnt = 65

for N in range(n):
    j = n-1
    for k in range(i, n):
        if cnt == 91:
            cnt = 65
        arr[k][j] = chr(cnt)
        cnt += 1
        j -= 1
    i += 1

for s in range(n):
    for q in range(n):
        if arr[s][q] == 0:
            print(' ', end =' ')
        else:
            print(arr[s][q], end=' ')
    print()
