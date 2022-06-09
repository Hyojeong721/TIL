import sys
sys.stdin = open("input.txt")


# 상/우/하/좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

max_dist = 1


def dfs(board, r, c, is_cutout):
    # is_cutout: 공사 여부
    if board[r][c] == 0:
        return

    global max_dist

    for i in range(4):
        cnt_r, cnt_c = r + dr[i], c + dc[i]

        if 0 <= cnt_r < N and 0 <= cnt_c < N:
            # 1) 현재 지형보다 낮은 경우 => 공사 여부와 관계 없이 탐색을 진행한다.
            if not distances[cnt_r][cnt_c] and board[r][c] > board[cnt_r][cnt_c]:
                distances[cnt_r][cnt_c] = distances[r][c] + 1
                max_dist = max(max_dist, distances[cnt_r][cnt_c])

                dfs(board, cnt_r, cnt_c, is_cutout)
                distances[cnt_r][cnt_c] = 0

            # 2) 현재 지형과 같거나 높은 경우 => 공사를 하지 않았고, 깎아서 갈 수 있는 경우에만 탐색을 진행한다.
            else:
                if not distances[cnt_r][cnt_c] and not is_cutout and board[cnt_r][cnt_c] - K < board[r][c]:
                    distances[cnt_r][cnt_c] = distances[r][c] + 1
                    max_dist = max(max_dist, distances[cnt_r][cnt_c])
                    temp = board[cnt_r][cnt_c]
                    board[cnt_r][cnt_c] = board[r][c] - 1

                    dfs(board, cnt_r, cnt_c, True)
                    board[cnt_r][cnt_c] = temp
                    distances[cnt_r][cnt_c] = 0


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = []

    for _ in range(N):
        board.append([int(x) for x in input().split()])

    distances = [[0] * N for _ in range(N)]

    # highest: 가장 높은 봉우리의 높이
    # highest_points: 가장 높은 봉우리들의 좌표
    highest = 0
    highest_points = []

    for r in range(N):
        highest = max(highest, max(board[r]))

    for r in range(N):
        for c in range(N):
            if board[r][c] == highest:
                highest_points.append((r, c))

    # 가장 높은 봉우리 각각에서 탐색을 가장 멀리 갈 수 있는 경로를 탐색한다.
    for r, c in highest_points:
        distances[r][c] = 1
        dfs(board, r, c, False)
        distances[r][c] = 0

    print("#{} {}".format(tc, max_dist))
    max_dist = 0
