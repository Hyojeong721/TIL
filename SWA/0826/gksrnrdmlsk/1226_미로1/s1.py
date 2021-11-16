import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = 16
T = 10
for tc in range(1, T + 1):
    temp = int(input())
    # 재미있는 미로 만들기
    lst = [list(map(int, list(input()))) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if lst[r][c] == 2:
                start = (r, c)
            elif lst[r][c] == 3:
                end = (r, c)

    stack = [start]
    path = [[0] * (N) for _ in range(N)] # visited,,,
    result = 0 # 갈 수 있는가, 없는가!
    while stack:
        curr = stack.pop()
        path[curr[0]][curr[1]] = 1
        if curr == end: # 도착한다면!
            result = 1
        # 주위 탐색
        for i in range(4):
            if lst[curr[0] + dx[i]][curr[1] + dy[i]] == 3: # 주위에 3, 즉 도착점이 있다면 마찬가지로 끝.
                result = 1
            if lst[curr[0] + dx[i]][curr[1] + dy[i]] == 0 and path[curr[0] + dx[i]][curr[1] + dy[i]] == 0:
                stack.append((curr[0] + dx[i], curr[1] + dy[i]))

        if result == 1:
            break
    print('#{} {}'.format(tc, result))