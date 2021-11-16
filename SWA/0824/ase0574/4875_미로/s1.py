import sys
sys.stdin = open('input.txt')
# 0 통로, 1 벽, 2 출발, 3 도착
# 재귀함수 사용 풀이

T = int(input())

def dfs(start_row, start_col):
    global result

    if arr[start_row][start_col] == 3:
        result = 1
        return

    visited.append((start_row, start_col))

    for i in range(4):
        new_row = start_row + dx[i]
        new_col = start_col + dy[i]

        if 0 <= new_row < N and 0 <= new_col < N:
            if (new_row, new_col) not in visited and (arr[new_row][new_col] != 1):
                dfs(new_row, new_col)

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = []

    #상 좌 하 우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_row = i
                start_col = j

    result = 0
    dfs(start_row, start_col)

    print('#{} {}'.format(tc, result))
