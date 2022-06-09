T = int(input())
arr = [[0]*100 for _ in range(100)]

for tc in range(T):
    x, y = map(int, input().split())
    # x축 변
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            arr[i][j] = 1

x_num = 0
y_num = 0
for n in range(100):
    for m in range(100):
        if arr[n][m] == 1:
            if arr[n][m-1] + arr[n][m+1] == 1:
                x_num += 1
        if arr[m][n] == 1:
            if arr[m-1][n] + arr[m+1][n] == 1:
                y_num += 1

print(x_num+y_num)