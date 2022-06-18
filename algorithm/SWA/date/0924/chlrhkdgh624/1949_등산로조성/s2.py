import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 현재 위치를 들고 다니는 경우
def work2(r, c, h, road, skill):
    global route
    if road > route:
        route = road

    visited[r][c] = 1

    for d in range(4):
        next_r = r + dr[d]
        next_c = c + dc[d]

        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N or visited[next_r][next_c]:
            continue

        if h > mountain[next_r][next_c]:
            work2(next_r, next_c, mountain[next_r][next_c], road+1, skill)
        elif skill and h > mountain[next_r][next_c] - K:
            work2(next_r, next_c, mountain[next_r][next_c] - 1, road + 1, 0)

    visited[r][c] = 0




dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N: 지도 크기, K: 최대 깊이


    mountain = []
    max_h = 0

    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in tmp:
            if max_h < j:
                max_h = j
        # 지도에 추가
        mountain.append(tmp)

    visited = [[0] * N for _ in range(N)]
    route = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:
                work2(i, j, max_h, 1, 1)

    print('#{} {}'.format(tc, route))