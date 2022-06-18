import sys
sys.stdin = open('input.txt')

T = int(input())


def dfs(i, j, start, cur, cnt):  # i좌표, j좌표, 시작위치, 현재위치 방넘버, 방 옮긴 횟수
    global temp, answer

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x in range(N) and y in range(N):
            if arr[x][y] == cur + 1:
                dfs(x, y, start, arr[x][y], cnt+1)

    if cnt > temp:
        temp = cnt
        answer = [(start, cnt)]
    elif cnt == temp:
        answer.append((start, cnt))
    return


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp = 1
    answer = []

    for i in range(N):
        for j in range(N):
            dfs(i, j, arr[i][j], arr[i][j], 1)
    answer.sort()
    a, b = answer[0]

    print('#{} {} {}'.format(tc, a, b))