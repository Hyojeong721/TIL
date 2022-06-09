n = int(input())
arr = [[0]*n for _ in range(n)]
cnt = 65

for i in range(n):
    if i % 2 :
        for j in range(n-1, -1, -1):
            if cnt == 91:
                cnt= 65
            arr[j][i] = chr(cnt)
            cnt += 1
    else:
        for j in range(n):
            if cnt == 91:
                cnt= 65
            arr[j][i] = chr(cnt)
            cnt += 1


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()