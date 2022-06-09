import sys
sys.stdin = open("input.txt")


def check_maze_route(board, N):
    """
    주어진 미로에서 출발점에서 도착점까지 갈 수 있는지 여부를 확인한다.
      - 0은 길, 1은 벽, 2는 출발점, 3은 도착점이다.
      - BFS 알고리즘을 활용한다.
    Args:
        board: 미로 (2차원 배열)
        N: 미로의 가로, 세로 길이
    Returns:
        미로의 도착점에 갈 수 있으면 True, 없으면 False
    """
    # 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 도착점에 갈 수 있는지 여부만 알면 되므로, 거리를 계산할 필요는 없다.
    visited = [[False] * N for _ in range(N)]

    # 출발점 지정
    for r in range(N):
        for c in range(N):
            if board[r][c] == '2':
                # 출발 지점을 큐에 넣는다.
                queue = [(r, c)]
                # 출발지를 방문 표시한다.
                visited[r][c] = True

    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            new_r, new_c = r + dr[i], c + dc[i]
            if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c]:
                if board[new_r][new_c] == '0':
                    visited[new_r][new_c] = True
                    queue.append((new_r, new_c))
                elif board[new_r][new_c] == '3':
                    return True

    return False


T = 10
N = 16

for _ in range(T):
    tc = int(input())
    maze = [input() for _ in range(N)]

    result = check_maze_route(maze, N)

    print("#{} {}".format(tc, int(result)))
