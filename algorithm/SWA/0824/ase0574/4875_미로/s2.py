import sys
sys.stdin = open('input.txt')
# 0 통로, 1 벽, 2 출발, 3 도착
# stack 이용

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = []

    #상 좌 하 우
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_row = i
                start_col = j

    result = 0
    stack = []
    stack.append((start_row, start_col))

    while stack:
        # stack에서 시작점 pop
        start_row, start_col = stack.pop()
        # 방문했다 남기기
        visited.append((start_row, start_col))

        # 현 위치에서 상하좌우 돌면서 갈수 있는 곳인지 탐색
        for i in range(4):
            new_row = start_row + dy[i]
            new_col = start_col + dx[i]
            # 틀을 벗어나지 않고
            if 0 <= new_row < N and 0 <= new_col < N:
                # 방문한 곳이 아니면서 벽이 아닌 곳이라면
                if (new_row, new_col) not in visited and (arr[new_row][new_col] != 1):
                    # 그곳이 탈출구이면 for문에서 나가기
                    if arr[new_row][new_col] == 3:
                        result = 1
                        break
                    # 탈출구가 아니라면 stack에 push
                    stack.append((new_row, new_col))
        # 다음위치에서 다시 상하좌우 돌리기
        else:
            continue
        # 탈출구 만나서 for문에서 break 걸렸으면 while에서도 break
        break

    print('#{} {}'.format(tc, result))
