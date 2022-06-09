n = int(input())
# 정사각형
arr= [[0]*n for _ in range(n)]

cnt = 1

for i in range(n):
    for j in range(n):
        arr[j][i] = cnt
        cnt += 1

for k in range(n):
    for q in range(n):
        print(arr[k][q], end=" ")
    print()