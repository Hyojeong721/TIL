import sys
sys.stdin = open("input.txt")


def get_distance(board, N):
    """
    주어진 미로의 출발지에서 도착지까지의 최소 거리를 구한다.
      - 0은 통로, 1은 벽, 2는 출발, 3은 도착이다.
    Args:
        board: 미로 (2차원 배열)
        N: 미로의 가로, 세로 길이
    Returns:
        출발지에서 도착지까지의 최소 거리 (단, 경로가 없는 경우 0)
    """
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    distances = [[0] * N for _ in range(N)]

    # 출발지 지정
    for r in range(N):
        for c in range(N):
            if board[r][c] == '2':
                # 출발 지점을 큐에 넣는다.
                queue = [(r, c)]
                # 출발지 방문을 표시하기 위해, 출발지의 거리를 1로 설정한다.
                distances[r][c] = 1

    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            new_r, new_c = r + dr[i], c + dc[i]
            # 해당 인덱스가 유효하며, 아직 방문하지 않은 경우
            if 0 <= new_r < N and 0 <= new_c < N and not distances[new_r][new_c]:
                # 해당 인덱스가 도착점인 경우
                if board[new_r][new_c] == '3':
                    # 출발지의 거리를 1로 설정했으므로, 1을 뺀 길이를 리턴한다.
                    return distances[r][c] - 1
                # 해당 인덱스가 통로인 경우
                elif board[new_r][new_c] == '0':
                    distances[new_r][new_c] = distances[r][c] + 1
                    queue.append((new_r, new_c))

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [input() for _ in range(N)]

    distance = get_distance(maze, N)
    print("#{} {}".format(tc, distance))
