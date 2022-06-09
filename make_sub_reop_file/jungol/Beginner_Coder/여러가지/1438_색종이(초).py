n = int(input())
arr = [[0] * 100 for _ in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for s in range(x-1, x+9):
        for q in range(y-1, y+9):
            arr[s][q] = 1

cnt = 0
for row in range(100):
    for col in range(100):
        if arr[row][col] == 1:
            cnt += 1

print(cnt)