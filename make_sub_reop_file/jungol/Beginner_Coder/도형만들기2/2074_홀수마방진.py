n = int(input())
arr= [[0]*n for _ in range(n)]
row = 0
col = n//2
cnt = 1
num = n*n-1

while num != 0:
    # 첫번째 행 가운데 1넣기
    if num == n*n-1:
        arr[row][col] = cnt


    # 일단 이동
    if cnt % n == 0:
        row += 1
    else:
        row -= 1
        col -= 1
    # 이동한 경로 검사
    if row < 0:
        row = n-1
    elif col < 0:
        col = n-1

    cnt += 1
    arr[row][col] = cnt
    num -= 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()