user = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
sero = [0] * 5
garo = [0] * 5
dagac = [0] * 2
dagack = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]

def search(row, col, num):
    garo_cnt = 0
    sero_cnt = 0
    dagac_cnt = 0
    # 가로 세로 확인
    for i in range(5):
        if visited[row][i] == 1:
            sero_cnt += 1
            if sero_cnt ==5:
                sero[row] = 1
        if visited[i][col] == 1:
            garo_cnt += 1
            if garo_cnt == 5:
                garo[col] = 1
    # 대각선 확인
    # 정가운데 일때는 대각선 검사 두번
    if (row, col) == (2, 2):
        for i in range(5):
            if (row, col) in dagack:
                if visited[i][4 - i] == 1:
                    dagac_cnt += 1
                if dagac_cnt == 5:
                    dagac[1] = 1
        dagac_cnt = 0
        for i in range(5):
            if row - col == 0:
                if visited[i][i] == 1:
                    dagac_cnt += 1
                if dagac_cnt == 5:
                    dagac[0] = 1
    # 정가운데가 아닌경우 대각선 검사 한번만
    else:
        for i in range(5):
            if (row, col) in dagack:
                if visited[i][4 - i] == 1:
                    dagac_cnt += 1
                if dagac_cnt == 5:
                    dagac[1] = 1

            if row - col == 0:
                if visited[i][i] == 1:
                    dagac_cnt += 1
                if dagac_cnt == 5:
                    dagac[0] = 1

    if garo.count(1) + sero.count(1) + dagac.count(1) >= 3:
        return 1
    else:
        return 0

cnt = 0
ans = 0
for i in range(5):
    if ans > 0:
        break
    for j in range(5):
        if ans > 0:
            break
        num = mc[i][j]
        # 해당 숫자 자리 찾기
        for k in range(5):
            if num in user[k]:
                row = k
                col = user[k].index(num)
                visited[row][col] = 1
                res = search(row, col, num)
                cnt += 1

                if res == 1:
                    ans = cnt
                    break

print(ans)