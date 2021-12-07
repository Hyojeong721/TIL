n = int(input())
arr=[[0]*(n*2-1) for _ in range(n*2-1)]
dr = [1, 1, -1, -1, 0]
dc = [-1, 1, 1, -1, -1]
cnt = n-1
row = 0
col = (2*n-1)//2
ans = 65
arr[row][col] = chr(ans)
ans += 1
while cnt != 0:
    # 7시 방향
    for i in range(cnt):
        if ans == 91:
            ans = 65
        row += dr[0]
        col += dc[0]
        arr[row][col] = chr(ans)
        ans += 1
    # 5시 방향
    for i in range(cnt):
        if ans == 91:
            ans = 65
        row += dr[1]
        col += dc[1]
        arr[row][col] = chr(ans)
        ans += 1
    # 2시 방향
    for i in range(cnt):
        if ans == 91:
            ans = 65
        row += dr[2]
        col += dc[2]
        arr[row][col] = chr(ans)
        ans += 1
    cnt -= 1
    # 11시 방향
    for i in range(cnt):
        if ans == 91:
            ans = 65
        row += dr[3]
        col += dc[3]
        arr[row][col] = chr(ans)
        ans += 1

    if ans == 91:
        ans = 65
    row += dr[4]
    col += dc[4]
    arr[row][col] = chr(ans)
    ans += 1


for i in range(2*n-1):
    for j in range(2*n-1):
        if arr[i][j] == 0:
            print(' ', end=' ')
        else:
            print(arr[i][j], end=' ')
    print()
