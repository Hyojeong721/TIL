n = int(input())
arr = [[0]*n for _ in range(n)]
dr = [0, 1, -1]
dc = [0, -1, 1]
cnt = 1
row = 0
col = 0

for i in range(n): # 0, 1, 2, 3, 4
    for j in range(i):
        if i == 1:
            arr[0][0] = cnt
            cnt += 1
            row += dr[1]
            col += dc[1]
        else:
            if i % 2:
                arr[row][col] = cnt
                cnt += 1
                row += dr[1]
                col += dc[1]

            else:
                arr[row][col] = cnt
                cnt += 1
                row += dr[2]
                col += dc[2]
    if i != 0:
        if i % 2 == 1:
            row -= dr[1]
            col -= dc[1]
            row += 1
        else:
            row -= dr[2]
            col -= dc[2]
            col += 1

for i in range(n, 0, -1): # 54321
    for j in range(i):
        if i % 2:
                arr[row][col] = cnt
                cnt += 1
                row += dr[1]
                col += dc[1]

        else:
            arr[row][col] = cnt
            cnt += 1
            row += dr[2]
            col += dc[2]

    if i % 2:
        row -= dr[1]
        col -= dc[1]
        col += 1
    else:
        row -= dr[2]
        col -= dc[2]
        row += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()