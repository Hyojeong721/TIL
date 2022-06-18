import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 현재 위치를 들고 다니지 않을 때
def work(r, c, road, skill):
    # r: row, c: col, road:길이, skill: 현재 공사를 공사 진행 상태
    global route
    if road > route:
        route = road

    visited[r][c] = 1

    for d in range(4):
        next_r = r + dr[d]
        next_c = c + dc[d]

        if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
            # 현위치 보다 낮은 곳으로 이동
            if mountain[r][c] > mountain[next_r][next_c]:
                work(next_r, next_c, road + 1, skill)
            # 현위치 보다 높거나 같은 곳으로 이동
            elif skill and mountain[r][c] > mountain[next_r][next_c] - K:
                backup = mountain[next_r][next_c]
                mountain[next_r][next_c] = mountain[r][c] - 1
                work(next_r, next_c, road+1, 0) # 공사 진행
                mountain[next_r][next_c] = backup

    visited[r][c] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N: 지도 크기, K: 최대 깊이

    # 지도 정보를 입력 받는 동시에 최장 높이 찾기
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
                work(i, j, 1, 1)

    print('# {} {}'.format(tc, route))










