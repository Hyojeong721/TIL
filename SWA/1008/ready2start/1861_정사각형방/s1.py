import sys
sys.stdin = open('input.txt')


# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for x in range(1, T + 1):
    N = int(input())
    board = []

    # 탐색을 용이하게 하기 위해, board를 -1로 감싼다.
    board.append([-1] * (N + 2))
    for _ in range(N):
        board.append([-1] + [int(x) for x in input().split()] + [-1])
    board.append([-1] * (N + 2))

    visited = [[False] * (N + 2) for _ in range(N + 2)]

    # max_info: (최대 길이, 처음 출발하는 방 번호)
    max_info = (0, 1000000)

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            # 이미 방문한 곳이라면 => 해당 위치를 건너뛰고 계속 탐색 진행
            if visited[r][c]:
                continue

            # is_start: 해당 위치가 시작 위치가 될 수 있다면 True, 아니면 False
            is_start = False

            for i in range(4):
                # 다른 칸에서 현재 칸으로 올 수 있다면 시작점 X
                if board[r][c] - 1 == board[r + dr[i]][c + dc[i]]:
                    is_start = False
                    break
                if board[r][c] + 1 == board[r + dr[i]][c + dc[i]]:
                    is_start = True

            if is_start:
                distance = 1
                visited[r][c] = True
                flag = True
                nr, nc = r, c

                while flag:
                    for i in range(4):
                        if board[nr][nc] + 1 == board[nr + dr[i]][nc + dc[i]]:
                            distance += 1
                            nr, nc = nr + dr[i], nc + dc[i]
                            visited[nr][nc] = True
                            break
                    # break로 빠져나오지 않음 => 더 이상 갈 수 있는 경로가 없음.
                    else:
                        # max_info보다 거리가 더 길거나, 거리가 같고 번호가 작다면 => max_info에 (거리, 번호) 저장
                        if (distance > max_info[0]
                                or (distance == max_info[0] and board[r][c] < max_info[1])):
                            max_info = (distance, board[r][c])
                        flag = False

    print("#{} {} {}".format(x, max_info[1], max_info[0]))
