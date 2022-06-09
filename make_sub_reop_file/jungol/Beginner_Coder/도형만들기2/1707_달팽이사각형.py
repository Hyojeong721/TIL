n = int(input())
arr = [[0]*n for _ in range(n)]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def add_num(row ,col, idx, cnt):
    global arr
    num = n*n

    while num != 0:
        cnt += 1
        # 정상 범위이내면
        if 0 <= row < n and 0 <= col < n:
            # 숫자안채워진곳이면
            if arr[row][col] == 0:
                arr[row][col] = cnt
                # 다음 위치로
                row += dr[idx]
                col += dc[idx]

            #숫자 채워진 곳이면
            else:
                # 이전 자리로 돌아와
                row -= dr[idx]
                col -= dc[idx]
                # 방향틀어 새로운 자리로 이동
                idx += 1
                idx = idx % 4
                row += dr[idx]
                col += dc[idx]
                arr[row][col] = cnt
                row += dr[idx]
                col += dc[idx]


        # 아웃라인이면
        else:
            #다시 원래 자리로 돌아가
            row -= dr[idx]
            col -= dc[idx]
            # 방향틀어 새로운 자리로 이동
            idx += 1
            idx = idx % 4
            row += dr[idx]
            col += dc[idx]
            if arr[row][col] == 0:
                arr[row][col] = cnt
                row += dr[idx]
                col += dc[idx]
            else:
                print('break')
                break

        num -= 1
add_num(0, 0, 0, 0)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()