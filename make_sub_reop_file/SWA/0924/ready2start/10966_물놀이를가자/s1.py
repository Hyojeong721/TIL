from collections import deque
import sys
sys.stdin = open("input.txt")


to_dist = {
    'W': 0,
    'L': -1,
}
# 상/우/하/좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    distances = []

    for _ in range(N):
        distances.append([to_dist[x] for x in input().rstrip()])

    queue = deque()

    # 처음부터 물인 칸들을 큐에 넣는다.
    for r in range(N):
        for c in range(M):
            if distances[r][c] == 0:
                queue.append((r, c, 0))

    while queue:
        r, c, dist = queue.popleft()
        # 현재 위치에서 사방을 탐색한다.
        for i in range(4):
            new_r, new_c = r + dr[i], c + dc[i]

            if (0 <= new_r < N and 0 <= new_c < M
                    and distances[new_r][new_c] == -1):
                distances[new_r][new_c] = dist + 1
                queue.append((new_r, new_c, dist + 1))

    # 모든 땅에서 물로 이동하기 위한 최소 이동 횟수의 합을 구한다.
    total = 0
    for r in range(N):
        total += sum(distances[r])

    print("#{} {}".format(tc, total))
