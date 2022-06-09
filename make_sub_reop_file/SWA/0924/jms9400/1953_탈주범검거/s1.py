import sys
sys.stdin = open('input.txt')

T = int(input())

pipes = [
    [0, 0, 0, 0],
    [-1, 1, 1, -1],  # 상0 우1 하2 좌3
    [-1, 0, 1, 0],
    [0, 1, 0, -1],
    [-1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, -1],
    [-1, 0, 0, -1],
]

# BFS
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # 세로, 가로, 맨홀세로, 맨홀가로, 소요시간
    map_arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    answer = 1
    visited[R][C] = 1
    temp = [(R, C)]

    while temp:
        x, y = temp.pop(0)
        if visited[x][y] >= L:
            break

        pi = pipes[map_arr[x][y]]  # 현재위치 파이프 가져오기
        for i in range(4):  # 사방향 탐색
            if i % 2 == 0:
                dx = x + pi[i]
                dy = y
            else:
                dx = x
                dy = y + pi[i]
            if dx not in range(N) or dy not in range(M): continue
            # 다음좌표가 방문했거나 현재와 파이프가 연결되지 않는다면!
            if visited[dx][dy] or pipes[map_arr[dx][dy]][(i+2)%4] == 0: continue

            visited[dx][dy] = visited[x][y] + 1
            answer += 1
            temp.append((dx, dy))

    print('#{} {}'.format(tc, answer))
