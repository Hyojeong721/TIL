import sys
sys.stdin = open('input.txt')

def bfs(start_x, start_y):
    global result, q, visited

    q.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while q:

        point = q.pop(0)
        start_x = point[0]
        start_y = point[1]

        # 이동한 경로가 출구라면 반복문 탈출
        if maze[start_x][start_y] == 3:
            result = 1
            return visited[start_x][start_y] - 2
        # 상하좌우 탐색
        for add in range(4):
            new_x = start_x + dx[add]
            new_y = start_y + dy[add]

            # 미로를 나가지 않고
            if 0 <= new_x < N and 0 <= new_y < N:
                # 방문한 적 없고
                if visited[new_x][new_y] <= 0:
                    # 길이라면
                    if maze[new_x][new_y] != 1:
                        # 갈 수 있는 길로 저장
                        q.append([new_x, new_y])
                        # 방문한 횟수 저장
                        visited[new_x][new_y] = visited[start_x][start_y] + 1

    return 0

T = int(input())

# 0은 통로, 1은 벽, 2는 출발, 3은 도착이다.
for tc in range(1, T+1):
    N = int(input())

    # 미로의 크기 N과 N개의 줄에 걸쳐
    maze = [list(map(int, input())) for _ in range(N)]

    # 방문가능 경로 리스트 = q / 방문기록 = visited
    q = []
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # 이동경로
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]

    # 시작과 끝 좌표 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x = i
                start_y = j

    result = 0
    print("#{} {}".format(tc, bfs(start_x, start_y)))

